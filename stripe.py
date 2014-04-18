import stripe

stripe.api_key = "sk_test_zl9IWWHkI2JUvGnaLyiSSmxH"

stripe.Plan.create(
	amount=2000,
	interval='month',
	name= 'Amazing Gold Plan',
	currency='usd',
	id='gold')