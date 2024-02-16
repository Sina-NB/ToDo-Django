from django.contrib import admin
from .models import TaskModel


# Register your models here.
@admin.register(TaskModel)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["user", "title", "completed", "created_date"]
