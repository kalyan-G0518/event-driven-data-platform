from datetime import datetime, timezone
from enum import Enum
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


# -------------------------
# ENUMS
# -------------------------

class EventType(str, Enum):
    LOGIN = "login"
    SEARCH = "search"
    PRODUCT_VIEW = "product_view"
    ADD_TO_CART = "add_to_cart"
    REMOVE_FROM_CART = "remove_from_cart"
    PURCHASE = "purchase"
    PAYMENT = "payment"
    REVIEW = "review"


class DeviceType(str, Enum):
    WEB = "web"
    MOBILE = "mobile"


class ProductCategory(str, Enum):
    ELECTRONICS = "electronics"
    FASHION = "fashion"
    HOME = "home"
    BEAUTY = "beauty"
    GROCERY = "grocery"
    SPORTS = "sports"


class PaymentMethod(str, Enum):
    CREDIT_CARD = "credit_card"
    DEBIT_CARD = "debit_card"
    PAYPAL = "paypal"
    APPLE_PAY = "apple_pay"
    GOOGLE_PAY = "google_pay"
    CASH_ON_DELIVERY = "cash_on_delivery"


# -------------------------
# EVENT MODEL
# -------------------------

class CommerceEvent(BaseModel):

    event_id: UUID = Field(default_factory=uuid4)

    event_type: EventType

    event_timestamp: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    ingestion_timestamp: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    user_id: int

    session_id: UUID = Field(default_factory=uuid4)

    product_id: Optional[int] = None

    category: Optional[ProductCategory] = None

    quantity: int = 1

    unit_price: float = 0.0

    payment_method: Optional[PaymentMethod] = None

    country: str

    city: str

    device: DeviceType

    platform: str

    event_source: str = "web"

    is_member: bool = False