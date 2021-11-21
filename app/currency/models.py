from django.db import models


class Rate(models.Model):
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sale = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField()
    type = models.CharField(max_length=3)  # noqa
    source = models.CharField(max_length=25)


class ContactUs(models.Model):
    email_from = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=1000)
