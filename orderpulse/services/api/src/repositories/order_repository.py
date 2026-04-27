from abc import ABC, abstractmethod
from typing import Any, Dict, Optional


class OrderRepository(ABC):
    @abstractmethod
    def get_by_order_id(self, order_id: str) -> Optional[Dict[str, Any]]:
        raise NotImplementedError

    @abstractmethod
    def create(self, order_data: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError
