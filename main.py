# This script prints "Hello world"
import stripe
from dotenv import load_dotenv
import os
load_dotenv()


def main():
    # stripe.api_key = ""
    # stripe.Customer.create(
    # name="Jenny Rosen",
    # email="jennyrosen@example.com",
    # )
    # stripe.api_key = os.environ["STRIPE_API_KEY"]
    print(os.getenv("STRIPE_API_KEY"))


if __name__ == "__main__":
    main()
