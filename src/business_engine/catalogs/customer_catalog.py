import random
import pandas as pd


class CustomerCatalog:
    """
    Loads Customer Master into memory.
    """

    def __init__(
        self,
        customer_path="data/master/customers"
    ):

        self.customers = pd.read_parquet(customer_path)

        print(
            f"Loaded {len(self.customers)} customers."
        )

    def get_random_customer(self):

        return self.customers.sample(1).iloc[0]

    def get_customer_by_id(
        self,
        customer_id
    ):

        customer = self.customers[
            self.customers["customer_id"] == customer_id
        ]

        if customer.empty:
            return None

        return customer.iloc[0]

    def get_customers_by_membership(
        self,
        membership
    ):

        return self.customers[
            self.customers["membership"] == membership
        ]

    def get_customers_by_category(
        self,
        category
    ):

        return self.customers[
            self.customers["preferred_category"] == category
        ]