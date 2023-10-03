from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Review(models.Model):

    class Meta:
        verbose_name_plural = 'Product Reviews'

    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=False, blank=False,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=80, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.product}'
