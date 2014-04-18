from django.db import models

class User(models.Model):
	"""
	This model replaces the default User
	"""
	name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=60)
	last_4_digits = models.CharField(max_length=4, blank=True, null=True)
	stripe_id = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.email