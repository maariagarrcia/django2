from django.contrib import admin
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("key", "name", "url", "created", "updated")
    ordering = ("name",)
    search_fields = ("name", "key")

admin.site.register(Link, LinkAdmin)
