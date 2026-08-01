from dataclasses import dataclass
from typing import Optional, List


@dataclass
class ShoppingContext:
    customer: dict

    preferred_category: Optional[str] = None

    recommended_products: Optional[List[dict]] = None

    selected_product: Optional[dict] = None

    quantity: int = 1

    purchase_probability: float = 0.0

    campaign: Optional[str] = None

    warehouse_id: Optional[str] = None