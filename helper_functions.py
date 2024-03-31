import stripe
from dotenv import load_dotenv
import os
load_dotenv()
stripe.api_key = os.getenv("STRIPE_API_KEY")


def create_stripe_customer(name, email):
    # https://docs.stripe.com/api/customers/create
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
    # https://docs.stripe.com/api/payment_methods/attach
    return stripe.PaymentMethod.attach(
        "pm_card_visa",
        customer=customer_id
    )


def create_stripe_subscription(customer, currency, description, items, default_payment_method):
    # https://docs.stripe.com/api/subscriptions/create
    return stripe.Subscription.create(
        customer=customer,  
        currency=currency, 
        items=items,  # must be an array of prices referencing a stripe price ID
        description=description,
        default_payment_method=default_payment_method
    )

