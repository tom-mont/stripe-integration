# This creates a subscription for a new customer on stripe
import helper_functions


def main():
    stripe_customer = helper_functions.create_stripe_customer(
        "Tom Montgomery", "tom.b.montgomery@gmail.com")

    stripe_price = helper_functions.create_stripe_price("ZAR", 1500, {"interval": "month"}, {
        "name": "Price working"})

    stripe_payment_method = helper_functions.attach_stripe_payment_method(
        stripe_customer.id)

    result = helper_functions.create_stripe_subscription(
        stripe_customer.id,
        "ZAR",
        "Subscription working",
        [{"price": f'{stripe_price.id}'}],
        stripe_payment_method.id)
    print(result)


if __name__ == "__main__":
    main()
