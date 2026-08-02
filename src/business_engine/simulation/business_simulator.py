from src.business_engine.catalogs.customer_catalog import CustomerCatalog
from src.business_engine.catalogs.product_catalog import ProductCatalog

from src.business_engine.simulation.shopping_context import ShoppingContext
from src.business_engine.simulation.preference_engine import PreferenceEngine

from src.ingestion.schemas.event import (
    CommerceEvent,
    EventType,
    PaymentMethod,
)

from uuid import uuid4
import random


class BusinessSimulator:
    """
    Main orchestration engine responsible
    for generating realistic shopping sessions.
    """

    def __init__(self):

        self.customer_catalog = CustomerCatalog()

        self.product_catalog = ProductCatalog()

    def generate_session(self):

        customer = self.customer_catalog.get_random_customer()

        context = ShoppingContext(customer=customer)

        context.preferred_category = (
            customer["preferred_category"]
        )

        product = (
            self.product_catalog
            .get_random_product_by_category(
                context.preferred_category
            )
        )

        context.selected_product = product

        session_id = uuid4()

        flow = [
            EventType.LOGIN,
            EventType.SEARCH,
            EventType.PRODUCT_VIEW,
            EventType.ADD_TO_CART,
            EventType.PURCHASE,
            EventType.PAYMENT,
        ]

        events = []

        for event_type in flow:

            payment = None
            quantity = 1

            if event_type == EventType.PURCHASE:

                quantity = random.randint(1, 3)

                payment = random.choice(
                    list(PaymentMethod)
                )

            event = CommerceEvent(

                event_type=event_type,

                user_id=int(customer["customer_id"]),

                session_id=session_id,

                product_id=int(product["product_id"]),

                category=product["category"],

                quantity=quantity,

                unit_price=float(
                    product["selling_price"]
                ),

                payment_method=payment,

                country=customer["country"],

                city=customer["city"],

                device="web",

                platform="Chrome",

                is_member=(
                    customer["membership"]
                    != "Bronze"
                ),
            )

            events.append(event)

        return events