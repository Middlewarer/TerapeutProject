from django.db import models

class Consultation(models.Model):
    title = models.CharField(max_length=255)

class Application(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    date_of_purchasing = models.DateTimeField(auto_now_add=True)
    consultation = models.OneToOneField(Consultation, on_delete=models.PROTECT, related_name='consultation')