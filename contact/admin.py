from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'email', 'reason',
                       'content', 'created_at',)

    fields = ('user', 'email', 'reason',
              'content', 'created_at', 'response_sent')

    list_display = (
        'user',
        'reason',
        'created_at',
        'response_sent'
    )

    ordering = ('response_sent', 'created_at')


admin.site.register(Contact, ContactAdmin)
