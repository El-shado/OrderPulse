from typing import List

from pydantic import BaseModel, EmailStr, Field


class OrderItem(BaseModel):
    sku: str = Field(..., min_length=1)
    qty: int = Field(..., gt=0)


class CreateOrderRequest(BaseModel):
    orderId: str = Field(..., min_length=1)
    customerId: str = Field(..., min_length=1)
    items: List[OrderItem] = Field(..., min_length=1)
    email: EmailStr
    phone: str = Field(..., min_length=8)
