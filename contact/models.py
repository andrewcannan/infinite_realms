from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):

    class Meta:
        verbose_name_plural = 'Contact Us Submissions'

    reason_choices = [
            ('', '--- Select Reason for Contact ---'),
            ('products', 'Inquiries about Products'),
            ('support', 'Customer Support or Technical Assistance'),
            ('feedback', 'Feedback or Suggestions'),
            ('wholesale', 'Wholesale or Bulk Orders'),
            ('privacy', 'Privacy Concerns or Data Requests'),
            ('marketing', 'Marketing or Advertising Inquiries'),
            ('orders', 'Recent Orders (Please include order number)') 
            ('general', 'General Questions or Comments'),
        ]

    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, null=False, blank=False)
    reason = models.CharField(max_length=100, null=False, blank=False,
                              choices=reason_choices)
    content = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    response_sent = models.BooleanField(default=False, null=False, blank=False)

    def __str__(self):
        return f'{self.user} - {self.reason}'
