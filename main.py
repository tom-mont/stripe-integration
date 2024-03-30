# This script prints "Hello world"
import stripe
from dotenv import load_dotenv
import os
load_dotenv()
stripe.api_key = os.getenv("STRIPE_API_KEY")
# [{"price": f'{stripe_price_id}'}]


def main():
    stripe_customer = create_stripe_customer(
        "Tom Montgomery", "tom.b.montgomery@gmail.com")

    stripe_price = create_stripe_price("ZAR", 1500, {"interval": "month"}, {
        "name": "Price working"})

    result = attach_stripe_payment_method(stripe_customer)

    print(result)

# creates a stripe payment method and sets it to default


# def create_stripe_payment_method():
#     return stripe.PaymentMethod.create(
#         amount=1000,
#         currency="zar",
#         payment_method="pm_card_visa",
#     )

def create_stripe_customer(name, email):
    return stripe.Customer.create(
        name=name,
        email=email,
    )


def create_stripe_price(currency, unit_amongst, recurring, product_data):
   # https://docs.stripe.com/api/prices/create
    return stripe.Price.create(
        currency=currency,
        unit_amount=unit_amongst,
        recurring=recurring,
        product_data=product_data
    )


def attach_stripe_payment_method(customer_id):
    return stripe.PaymentMethod.attach(
        "pm_card_visa",
        # os.getenv("STRIPE_CUSTOMER_ID")
        customer=customer_id
    )


def create_stripe_subscription(customer, currency, description, items, default_payment_method):
    return stripe.Subscription.create(
        customer=customer,  # os.getenv("STRIPE_CUSTOMER_ID"),
        currency=currency,  # ZAR
        items=items,  # must be an array of prices referencing a stripe price ID
        description=description,
        default_payment_method=default_payment_method
        #     create_stripe_subscription(
        #     os.getenv("STRIPE_CUSTOMER_ID"),
        #     "ZAR",
        #     "Testing",
        #     [{"price": f'{os.getenv("STRIPE_PRICE_ID")}'}]
        #     # add default_payment_method: STRIPE_PAYMENT_METHOD_ID
        # )
    )

# create_stripe_subscription(customer=os.getenv("STRIPE_CUSTOMER_ID"),
#                                         currency="zar",
#                                         description="Test",
#                                         items=[
#                                             {"price": f'{os.getenv("STRIPE_PRICE_ID")}'}],
#                                         default_payment_method=os.getenv("STRIPE_PAYMENT_METHOD_ID"))


if __name__ == "__main__":
    main()
