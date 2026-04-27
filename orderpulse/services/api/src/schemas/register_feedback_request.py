from typing import Optional

from pydantic import BaseModel, Field


class RegisterFeedbackRequest(BaseModel):
    orderId: str = Field(..., min_length=1)
    customerId: str = Field(..., min_length=1)
    rating: int = Field(..., ge=1, le=5)
    comment: Optional[str] = None
