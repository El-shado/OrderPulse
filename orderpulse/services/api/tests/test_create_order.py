from services.api.src.handlers.create_order_handler import handler


mock_event = {
    "body": {
        "orderId": "ord_999",
        "customerId": "cust_555",
        "email": "test@elva-candidate.com",
        "phone": "+46700000000",
        "items": [
            {"sku": "AWS-BOOK", "qty": 1},
            {"sku": "SERVERLESS-MUG", "qty": 2}
        ]
    }
}

print("--- Starting Local Execution ---")


try:
    response = handler(mock_event, None)
    
    print("\n--- Response From Handler ---")
    print(f"Status Code: {response['statusCode']}")
    print(f"Body: {response['body']}")
    
except Exception as e:
    print(f"\n[Error]: {e}")

print("\n--- Execution Finished ---")