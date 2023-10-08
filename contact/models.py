from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):

    class Meta:
        verbose_name_plural = 'Contact Us Submissions'

    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, null=False, blank=False)
    reason = models.CharField(max_length=100, choices=[], null=False,
                              blank=False)
    content = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    response_sent = models.BooleanField(default=False, null=False, blank=False)

    def __str__(self):
        return f'{self.user} - {self.reason}'
