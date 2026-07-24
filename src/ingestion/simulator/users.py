from dataclasses import dataclass
import random
from faker import Faker

from src.ingestion.schemas.event import DeviceType

fake = Faker()


@dataclass(frozen=True)
class User:
    user_id: int
    country: str
    city: str
    device: DeviceType
    platform: str
    is_member: bool


def generate_user(user_id: int) -> User:
    """
    Generates a realistic e-commerce user.
    """

    device = random.choice(
        [
            DeviceType.WEB,
            DeviceType.MOBILE
        ]
    )

    if device == DeviceType.WEB:
        platform = random.choice(
            [
                "Chrome",
                "Firefox",
                "Edge",
                "Safari"
            ]
        )
    else:
        platform = random.choice(
            [
                "Android",
                "iOS"
            ]
        )

    return User(
        user_id=user_id,
        country=fake.country(),
        city=fake.city(),
        device=device,
        platform=platform,
        is_member=random.random() < 0.35
    )