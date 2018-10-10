"""Classes for melon orders."""
class AbstractMelonOrder():
	"""Blueprints for all you MelonOrder Shipping Needs"""

	def __init__(self, species, qty, country_code = "USA"):
		self.species = species
		self.qty = qty
		self.country_code = country_code
		self.shipped = False	
	
	def get_total(self):
		"""Calculate price, including tax."""
		if self.country_code != "USA":
			# self.order_type = "international"
			self.tax = 0.17	
			if self.qty < 10:
				self.fee = 3
			else:
				self.fee = 0
		else:
			# self.order_type = "domestic"
			self.tax = 0.08
			self.fee = 0

		base_price = 5
		if self.species == "christmas melon":
			total = ((1 + self.tax) * self.qty * (base_price * 1.5)) + self.fee
		else:
			total = ((1 + self.tax) * self.qty * base_price) + self.fee
		return total

	def mark_shipped(self):
		"""Record the fact than an order has been shipped."""

		self.shipped = True


	def get_country_code(self):
		"""Return the country code."""

		return self.country_code


class DomesticMelonOrder(AbstractMelonOrder):
	"""A melon order within the USA."""


class InternationalMelonOrder(AbstractMelonOrder):
	"""An international (non-US) melon order."""

	# def add_shipping_fee(self):
	# 	if super().qty < 10:
	# 		total = super().get_total(self) + 3
	# 		return total

