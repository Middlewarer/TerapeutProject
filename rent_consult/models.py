from django.db import models

class ConsultationRequest(models.Model):
    class ContactMethod(models.TextChoices):
        TELEGRAM = "telegram", "Telegram"
        WHATSAPP = "whatsapp", "WhatsApp"
        PHONE = "phone", "Телефон"
        EMAIL = "email", "Email"
        OTHER = "other", "Другое"

    name = models.CharField(max_length=120)
    contact_method = models.CharField(max_length=20, choices=ContactMethod.choices)
    contact = models.CharField(max_length=255, unique=True)
    topic = models.CharField(max_length=255)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    was_conducted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.contact_method}) {self.created_at}"
