from src.ingestion.schemas.event import (
    CommerceEvent,
    DeviceType,
    EventType,
    ProductCategory,
)

event = CommerceEvent(
    event_type=EventType.PRODUCT_VIEW,
    user_id=1001,
    product_id=501,
    category=ProductCategory.ELECTRONICS,
    quantity=1,
    unit_price=999.99,
    country="USA",
    city="Tampa",
    device=DeviceType.WEB,
    platform="Chrome",
)

print(event.model_dump_json(indent=4))