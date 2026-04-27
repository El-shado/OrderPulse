from typing import Optional

from pydantic import BaseModel, Field


class DeliveryView(BaseModel):
    deliveryId: str = Field(..., min_length=1)
    status: str = Field(..., min_length=1)
    updatedAt: str = Field(..., min_length=1)


class FeedbackView(BaseModel):
    submitted: bool
    rating: Optional[int] = None
    comment: Optional[str] = None


class GetOrderResponse(BaseModel):
    orderId: str = Field(..., min_length=1)
    customerId: str = Field(..., min_length=1)
    orderStatus: str = Field(..., min_length=1)
    delivery: Optional[DeliveryView] = None
    feedback: FeedbackView
