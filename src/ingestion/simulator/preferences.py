import random


CUSTOMER_PREFERENCES = {

    "Electronics": 0.25,

    "Fashion": 0.18,

    "Home & Kitchen": 0.10,

    "Beauty": 0.08,

    "Sports": 0.08,

    "Books": 0.05,

    "Gaming": 0.06,

    "Furniture": 0.04,

    "Automotive": 0.04,

    "Groceries": 0.12,
}


def choose_preferred_category():

    categories = list(CUSTOMER_PREFERENCES.keys())

    weights = list(CUSTOMER_PREFERENCES.values())

    return random.choices(
        categories,
        weights=weights,
        k=1
    )[0]