from datetime import datetime, timezone
from typing import Any, Dict

from services.api.src.schemas.create_order_request import CreateOrderRequest
from services.api.src.schemas.create_order_response import CreateOrderResponse
from services.api.src.repositories.order_repository import OrderRepository
from services.api.src.adapters.event_publisher import EventPublisher
from services.api.src.observability.logger import log_json


class CreateOrderUseCase:
    def __init__(
        self,
        order_repository: OrderRepository,
        event_publisher: EventPublisher,
        logger: Any,
    ) -> None:
        self.order_repository = order_repository
        self.event_publisher = event_publisher
        self.logger = logger

    def execute(self, request: CreateOrderRequest) -> CreateOrderResponse:
        existing_order = self.order_repository.get_by_order_id(request.orderId)
        if existing_order is not None:
            raise ValueError("Order already exists")

        order_record: Dict[str, Any] = {
            "orderId": request.orderId,
            "customerId": request.customerId,
            "status": "CREATED",
            "items": [item.model_dump() for item in request.items],
            "email": request.email,
            "phone": request.phone,
            "createdAt": datetime.now(timezone.utc).isoformat(),
        }

        self.order_repository.create(order_record)

        event = {
            "eventId": f"evt_{request.orderId}",
            "eventType": "order.created",
            "occurredAt": datetime.now(timezone.utc).isoformat(),
            "correlationId": request.orderId,
            "source": "orderpulse.api",
            "data": {
                "orderId": request.orderId,
                "customerId": request.customerId,
                "status": "CREATED",
            },
        }

        self.event_publisher.publish(event)

        log_json(
            self.logger,
            action="create_order",
            orderId=request.orderId,
            eventType="order.created",
            result="success",
        )

        return CreateOrderResponse(
            orderId=request.orderId,
            status="CREATED",
            message="Order created successfully",
        )
