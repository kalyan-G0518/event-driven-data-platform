import random

from src.ingestion.schemas.event import (
    CommerceEvent,
    EventType,
    PaymentMethod,
)
from src.ingestion.simulator.products import get_random_product
from src.ingestion.simulator.sessions import generate_session_flow
from src.ingestion.simulator.users import generate_user


def generate_session(user_id: int):
    """
    Generate all events for a single user session.
    """

    user = generate_user(user_id)
    flow = generate_session_flow()
    from uuid import uuid4
    session_id = uuid4()
    

    for event_type in flow:

        product = get_random_product()

        payment_method = None
        quantity = 1

        if event_type == EventType.PURCHASE:
            payment_method = random.choice(list(PaymentMethod))
            quantity = random.randint(1, 3)

        event = CommerceEvent(
            event_type=event_type,
            user_id=user.user_id,
            product_id=product.product_id,
            category=product.category,
            session_id=session_id,
            quantity=quantity,
            unit_price=product.price,
            payment_method=payment_method,
            country=user.country,
            city=user.city,
            device=user.device,
            platform=user.platform,
            is_member=user.is_member,
        )

        yield event