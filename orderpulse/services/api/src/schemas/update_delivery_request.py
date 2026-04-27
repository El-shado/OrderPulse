from typing import Literal

from pydantic import BaseModel, Field


DeliveryStatus = Literal[
    "SCHEDULED",
    "IN_TRANSIT",
    "OUT_FOR_DELIVERY",
    "DELIVERED",
    "FAILED_ATTEMPT",
]


class UpdateDeliveryRequest(BaseModel):
    orderId: str = Field(..., min_length=1)
    deliveryId: str = Field(..., min_length=1)
    status: DeliveryStatus
    updatedAt: str = Field(..., min_length=1)
    source: str = Field(..., min_length=1)
    messageId: str = Field(..., min_length=1)
