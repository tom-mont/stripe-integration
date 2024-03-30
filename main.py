# This script prints "Hello world"
import stripe
from dotenv import load_dotenv
import os
load_dotenv()
stripe.api_key = os.getenv("STRIPE_API_KEY")
# [{"price": f'{stripe_price_id}'}]


def main():
    result = create_stripe_subscription(
        os.getenv("STRIPE_CUSTOMER_ID"),
        "ZAR",
        "Testing",
        [{"price": f'{os.getenv("STRIPE_PRICE_ID")}'}]
    )
    print(result)


def create_stripe_subscription(customer, currency, description, items):
    return stripe.Subscription.create(
        customer=customer,  # os.getenv("STRIPE_CUSTOMER_ID"),
        currency=currency,  # ZAR
        items=items,  # must be an array of prices referencing a stripe price ID
        description=description,
    )


def create_stripe_price(currency, unit_amongst, recurring, product_data):
   # https://docs.stripe.com/api/prices/create
    return stripe.Price.create(
        currency=currency,
        unit_amount=unit_amongst,
        recurring=recurring,
        product_data=product_data
    )


def create_stripe_customer(name, email):
    return stripe.Customer.create(
        name=name,
        email=email,
    )


if __name__ == "__main__":
    main()
