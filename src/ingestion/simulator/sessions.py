import random

from src.ingestion.schemas.event import EventType


def generate_session_flow() -> list[EventType]:
    """
    Generates a realistic sequence of events
    representing one user session.
    """

    flow = []

    # 90% of users log in
    if random.random() < 0.9:
        flow.append(EventType.LOGIN)

    # Everyone searches
    flow.append(EventType.SEARCH)

    # User views 1-5 products
    for _ in range(random.randint(1, 5)):
        flow.append(EventType.PRODUCT_VIEW)

    # 60% add something to cart
    if random.random() < 0.6:
        flow.append(EventType.ADD_TO_CART)

        # 70% of carts convert
        if random.random() < 0.7:
            flow.append(EventType.PURCHASE)
            flow.append(EventType.PAYMENT)

    # 20% leave a review after purchase
    if (
        EventType.PURCHASE in flow
        and random.random() < 0.2
    ):
        flow.append(EventType.REVIEW)

    return flow