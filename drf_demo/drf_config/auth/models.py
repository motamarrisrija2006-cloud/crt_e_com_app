from django.db import models

# Create your models here.
class UserModel(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=8)
    phone = models.CharField(max_length=12)

    class Meta:
        app_label = 'auth'