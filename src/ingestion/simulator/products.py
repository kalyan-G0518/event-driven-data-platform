from dataclasses import dataclass
from typing import List
import random

from src.ingestion.schemas.event import ProductCategory


@dataclass(frozen=True)
class Product:
    product_id: int
    name: str
    category: ProductCategory
    price: float


PRODUCT_CATALOG: List[Product] = [
    Product(1001, "iPhone 16", ProductCategory.ELECTRONICS, 999.99),
    Product(1002, "Samsung Galaxy S25", ProductCategory.ELECTRONICS, 899.99),
    Product(1003, "MacBook Air M4", ProductCategory.ELECTRONICS, 1299.99),
    Product(1004, "Sony WH-1000XM6", ProductCategory.ELECTRONICS, 399.99),

    Product(2001, "Nike Air Max", ProductCategory.FASHION, 149.99),
    Product(2002, "Adidas Ultraboost", ProductCategory.FASHION, 179.99),
    Product(2003, "Levi's 511 Jeans", ProductCategory.FASHION, 69.99),

    Product(3001, "Dyson Vacuum", ProductCategory.HOME, 499.99),
    Product(3002, "Philips Air Fryer", ProductCategory.HOME, 199.99),

    Product(4001, "Organic Coffee Beans", ProductCategory.GROCERY, 14.99),
    Product(4002, "Protein Powder", ProductCategory.GROCERY, 39.99),

    Product(5001, "Dumbbell Set", ProductCategory.SPORTS, 89.99),
    Product(5002, "Yoga Mat", ProductCategory.SPORTS, 24.99),

    Product(6001, "Face Wash", ProductCategory.BEAUTY, 12.99),
    Product(6002, "Sunscreen SPF50", ProductCategory.BEAUTY, 18.99),
]


def get_random_product() -> Product:
    """Return a random product from the catalog."""
    return random.choice(PRODUCT_CATALOG)