from abc import ABC, abstractmethod
from typing import Any, Dict


class EventPublisher(ABC):
    @abstractmethod
    def publish(self, event: Dict[str, Any]) -> None:
        raise NotImplementedError
