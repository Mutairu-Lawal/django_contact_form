from django.db import models

# Create your models here.


class Users(models.Model):

    GENERAL_ENQUIRY = 'general'
    SUPPORT_REQUEST = 'support'

    QUERY_TYPE_CHOICES = {
        GENERAL_ENQUIRY: GENERAL_ENQUIRY,
        SUPPORT_REQUEST: SUPPORT_REQUEST
    }

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    messages = models.TextField()
    query_type = models.CharField(max_length=15, choices=QUERY_TYPE_CHOICES)
    consent = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        auto_now_add=True,)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name}"

    class Meta:
        verbose_name_plural = 'users'
