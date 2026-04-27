from typing import Any, Dict

from services.api.src.schemas.create_order_request import CreateOrderRequest
from services.api.src.use_cases.create_order import CreateOrderUseCase
from services.api.src.observability.logger import get_logger


class InMemoryOrderRepository:
    def __init__(self) -> None:
        self.storage: Dict[str, Dict[str, Any]] = {}

    def get_by_order_id(self, order_id: str):
        return self.storage.get(order_id)

    def create(self, order_data: Dict[str, Any]) -> Dict[str, Any]:
        self.storage[order_data["orderId"]] = order_data
        return order_data


class ConsoleEventPublisher:
    def publish(self, event: Dict[str, Any]) -> None:
        print({"published_event": event})


logger = get_logger("orderpulse.create_order")


def handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    body = event.get("body", {})
    request = CreateOrderRequest(**body)

    use_case = CreateOrderUseCase(
        order_repository=InMemoryOrderRepository(),
        event_publisher=ConsoleEventPublisher(),
        logger=logger,
    )

    result = use_case.execute(request)

    return {
        "statusCode": 201,
        "body": result.model_dump(),
    }
