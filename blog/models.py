from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length = 100)
	description = models.TextField(max_length = 1000)
	date = models.DateField(auto_now = False, auto_now_add = False)

	def __str__(self):
		return self.title
