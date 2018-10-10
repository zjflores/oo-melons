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

		if self.country_code == "USA":
			# self.order_type = "domestic"
			self.tax = 0.08
		else:
			# self.order_type = "international"
			self.tax = 0.17		
	
		base_price = 5
		total = (1 + self.tax) * self.qty * base_price

		return total

	def mark_shipped(self):
		"""Record the fact than an order has been shipped."""

		self.shipped = True


	# def get_country_code(self):
	# 	"""Return the country code."""

	# 	return self.country_code


class DomesticMelonOrder(AbstractMelonOrder):
	"""A melon order within the USA."""


class InternationalMelonOrder(AbstractMelonOrder):
	"""An international (non-US) melon order."""

	def get_country_code(self):
		"""Return the country code."""

		return self.country_code
