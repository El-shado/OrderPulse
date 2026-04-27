from pydantic import BaseModel, Field


class CreateOrderResponse(BaseModel):
    orderId: str = Field(..., min_length=1)
    status: str = Field(..., min_length=1)
    message: str = Field(..., min_length=1)
