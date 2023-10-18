from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    """
    Class extends djangos ModelAdmion class
    """
    list_display = (
        'product',
        'user',
        'title',
        'content',
        'created_at',
    )
    ordering = ('product',)


admin.site.register(Review, ReviewAdmin)
