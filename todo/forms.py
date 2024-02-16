from django import forms
from .models import TaskModel


class TaskForm(forms.ModelForm):
    """
    Task model form. this form only contains title field so
    it is necessary to add user automatically.
    """

    class Meta:
        model = TaskModel
        fields = ["title"]
