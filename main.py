# This script prints "Hello world"
import stripe
from dotenv import load_dotenv
import os
load_dotenv()
stripe.api_key = os.getenv("STRIPE_API_KEY")


def main():
    print(os.getenv("STRIPE_CUSTOMER_ID"))


def create_stripe_customer(name, email):
    return stripe.Customer.create(
        name="Tom Montgomery",
        email="tom.b.montgomery@gmail.com",
    )


if __name__ == "__main__":
    main()
