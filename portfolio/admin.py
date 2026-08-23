from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "technology", "created_at")
    search_fields = ("title", "technology", "description")
    list_filter = ("created_at",)
    ordering = ("-created_at",)
