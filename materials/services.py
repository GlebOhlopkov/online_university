import stripe

from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_url_stripe_sessions(course):
    stripe_product = stripe.Product.create(name=course.name)
    stripe_price = stripe.Price.create(
        currency="rub",
        unit_amount=course.price * 100,
        product_data={"name": stripe_product.name},
    )
    stripe_session = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[{"price": stripe_price['id'], "quantity": 1}],
        mode="payment",
    )
    stripe_session_data = {'url': stripe_session['url'],
                           'id': stripe_session['id']}
    return stripe_session_data
