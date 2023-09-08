from typing import Any, List, Optional, Tuple, Union
from django.contrib import admin
from django.http.request import HttpRequest
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("key", "name", "url", "created", "updated")
    ordering = ("name",)
    search_fields = ("name", "key")

    def get_readonly_fields(self, request,objt= None):
        if request.user.groups.filter(name="Personal").exists():
            return ("key", "name")
        else:
            return ("created", "updated")

admin.site.register(Link, LinkAdmin)
