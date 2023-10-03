from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Review(models.Model):

    class Meta:
        verbose_name_plural = 'Product Reviews'

    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.product}'
