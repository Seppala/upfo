from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class upUser(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=40)
	email = models.EmailField()
	# shot = models.ImageField(upload_to='userimage')

	def __str__(self):
		return self.name

	class Admin: pass