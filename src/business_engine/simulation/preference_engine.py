import random


class PreferenceEngine:
    """
    Generates shopping preferences for customers.
    """

    CATEGORY_WEIGHTS = {
        "Electronics": 0.22,
        "Fashion": 0.18,
        "Beauty": 0.08,
        "Sports": 0.08,
        "Books": 0.05,
        "Furniture": 0.05,
        "Home & Kitchen": 0.12,
        "Groceries": 0.12,
        "Gaming": 0.05,
        "Automotive": 0.05,
    }

    @classmethod
    def choose_category(cls):

        return random.choices(
            population=list(cls.CATEGORY_WEIGHTS.keys()),
            weights=list(cls.CATEGORY_WEIGHTS.values()),
            k=1,
        )[0]