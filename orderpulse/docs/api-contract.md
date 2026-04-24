# OrderPulse - API Contract

## Purpose
This document defines the core public API contract for OrderPulse.

## Core APIs
- `POST /orders`
- `POST /deliveries/update`
- `GET /orders/{id}`
- `POST /feedback`

---

## 1. POST /orders

### Purpose
Create a new purchase order in the system.

## Business Meaning
This endpoint represents the moment when a new order enters the platform and becomes available for tracking, event publication, and downstream processing.

4

### Request
```json
{
  "orderId": "ord_001",
  "customerId": "cust_100",
  "items": [
    {
      "sku": "SKU-1",
      "qty": 2
    }
  ],
  "email": "buyer@example.com",
  "phone": "+46700000000"
}
```

### Success Response
Status: `201 Created`

```json
{
  "orderId": "ord_001",
  "status": "CREATED",
  "message": "Order created successfully"
}
```

### Errors
## Returned when the payload is malformed or missing required fields.
```json
{
  "errorCode": "INVALID_REQUEST",
  "message": "The request payload is invalid"
}
```
- `400 Bad Request`
- `409 Conflict` 
- `500 Internal Server Error`

### Notes
- This endpoint should publish the order.created event after successful persistence.
- This endpoint must not send notifications directly in the synchronous request path.

---

## 2. POST /deliveries/update

### Purpose
Update the delivery status of an existing order.

## Business Meaning
This endpoint represents an external delivery update arriving from a logistics partner or operational system.

### Request
```json
{
  "orderId": "ord_001",
  "deliveryId": "del_001",
  "status": "OUT_FOR_DELIVERY",
  "updatedAt": "2026-04-10T09:30:00Z",
  "source": "partner-system",
  "messageId": "msg_001"
}
```

### Allowed Status Values
- `SCHEDULED`
- `IN_TRANSIT`
- `OUT_FOR_DELIVERY`
- `DELIVERED`
- `FAILED_ATTEMPT`

### Success Response
Status: `200 OK`

```json
{
  "orderId": "ord_001",
  "deliveryId": "del_001",
  "status": "OUT_FOR_DELIVERY",
  "message": "Delivery status updated successfully"
}
```

### Errors
- `400 Bad Request`
- `404 Not Found`
- `422 Unprocessable Entity`
- `500 Internal Server Error`

### Notes
- This endpoint should publish the delivery.updated event after a valid update.
- This endpoint must support idempotent handling for repeated updates with the same messageId.

---

## 3. GET /orders/{id}

### Purpose
Retrieve the current order status view.

## Business Meaning
This endpoint provides the customer-facing or operations-facing visibility view of an order.

### Path Parameter
- `id`: order identifier

### Success Response
Status: `200 OK`

```json
{
  "orderId": "ord_001",
  "customerId": "cust_100",
  "orderStatus": "CREATED",
  "delivery": {
    "deliveryId": "del_001",
    "status": "OUT_FOR_DELIVERY",
    "updatedAt": "2026-04-10T09:30:00Z"
  },
  "feedback": {
    "submitted": false
  }
}
```

### Errors
- `404 Not Found`
- `500 Internal Server Error`

### Notes
- This endpoint should return a simplified read model, not raw storage internals.
- The response should be useful to both customer support and operational users.

---

## POST /feedback

### Purpose
Register post-delivery customer feedback.

## Business Meaning
This endpoint captures the customer's experience after delivery and closes the order lifecycle with a feedback signal.

### Request
```json
{
  "orderId": "ord_001",
  "customerId": "cust_100",
  "rating": 5,
  "comment": "Delivery was on time and communication was clear"
}
```

### Success Response
Status: `201 Created`

```json
{
  "orderId": "ord_001",
  "feedbackStatus": "RECEIVED",
  "message": "Feedback recorded successfully"
}
```

### Errors
- `400 Bad Request`
- `404 Not Found`
- `422 Unprocessable Entity`
- `500 Internal Server Error`

### Notes
- This endpoint should publish the feedback.received event after successful persistence.
- This endpoint should not expose internal validation logic directly in the response.

---

## Validation Rules

### 1. Schema Validation
Checks:
- required fields
- field types
- basic payload structure

### 2. Business Validation
Checks:
- order existence
- valid delivery status transitions
- feedback allowed only after delivery completion
- duplicate update handling through idempotency

---

### Error Format

## All errors should follow a consistent response format:
```json
{
  "errorCode": "SOME_ERROR_CODE",
  "message": "A clear human-readable explanation"
}
```

---

## Observability Identifiers
Each request or event flow should be traceable using:
- `requestId`
- `correlationId`
- `orderId`
- `eventId`
