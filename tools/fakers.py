import time

from faker import Faker
import random

fake = Faker()

def get_random_email():
    return f"test.{time.time()}@example.com"

def get_random_name():
    return f"{fake.first_name()}"
