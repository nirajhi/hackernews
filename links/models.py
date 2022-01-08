from django.db import models
from django.conf import settings
# Create your models here.

class Link(models.Model):
	url = models.URLField()
	description = models.TextField(blank=True)
	posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
	# posted_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	# created_at = models.DateTimeField(auto_now_add=True)
	# updated_at = models.DateTimeField(auto_now=True)


class Vote(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	link = models.ForeignKey('links.Link', related_name="votes", on_delete=models.CASCADE)


# Link.objects.create(url='http://www.google.com', description='Google')
# Link.objects.create(url='http://www.youtube.com', description='Youtube')