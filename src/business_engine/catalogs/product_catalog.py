import random
import pandas as pd


class ProductCatalog:
    """
    Loads the Product Master into memory.
    """

    def __init__(
        self,
        product_path="data/master/products"
    ):

        self.products = pd.read_parquet(product_path)

        print(
            f"Loaded {len(self.products)} products."
        )

    def get_random_product(self):

        return self.products.sample(1).iloc[0]

    def get_product_by_id(self, product_id):

        product = self.products[
            self.products["product_id"] == product_id
        ]

        if product.empty:
            return None

        return product.iloc[0]

    def get_products_by_category(self, category):

        return self.products[
            self.products["category"] == category
        ]

    def get_products_by_brand(self, brand):

        return self.products[
            self.products["brand"] == brand
        ]
        
    def get_random_product_by_category(
        self,
        category,
    ):
    
        """
        Returns a random product from the given category.
        Falls back to any product if the category is empty.
        """

        products = self.products[
            self.products["category"] == category
        ]

        if len(products) == 0:
            return self.get_random_product()

        return products.sample(1).iloc[0]