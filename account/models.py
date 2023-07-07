from django.db import models


'''
Overriding the default djoser user model
'''
class AccountUser(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

