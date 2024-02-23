from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import TaskModel
from .forms import TaskForm


# Create your views here.
class ListTaskView(View):
    """
    List tasks class based view. this view accepts only 'get' method.
    """

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        """
        The 'get' method is implemented in this function.
        """
        tasks = TaskModel.objects.filter(user=request.user)
        context = {"tasks": tasks}
        return render(request, "todo/list_task.html", context)


class DeleteTaskView(View):
    """
    Delete task class based view. this view accepts only 'get' method.
    """

    @method_decorator(login_required)
    def get(self, request, pk, *args, **kwargs):
        """
        The 'get' method is implemented in this function.
        """
        task = get_object_or_404(TaskModel, id=pk)
        task.delete()
        return redirect("/")


class CompleteTaskView(View):
    """
    Complete task class based view. this view accepts only 'get' method.
    """

    @method_decorator(login_required)
    def get(self, request, pk, *args, **kwargs):
        """
        The 'get' method is implemented in this function.
        """
        task = get_object_or_404(TaskModel, id=pk)
        task.completed = True
        task.save()
        return redirect("/")


class NotCompleteTaskView(View):
    """
    Not complete task class based view. this view accepts only 'get' method.
    """

    @method_decorator(login_required)
    def get(self, request, pk, *args, **kwargs):
        """
        The 'get' method is implemented in this function.
        """
        task = get_object_or_404(TaskModel, id=pk)
        task.completed = False
        task.save()
        return redirect("/")


class CreateTaskView(View):
    """
    Create task class based view. this view accepts only 'post' method.
    """

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        """
        The 'post' method is implemented in this function.
        """
        form = TaskForm(data=request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
        return redirect("/")


class UpdateTaskView(View):
    """
    Update task class based view. this view accepts 'get' and 'post' methods.
    """

    @method_decorator(login_required)
    def get(self, request, pk, *args, **kwargs):
        """
        The 'get' method is implemented in this function.
        """
        task = get_object_or_404(TaskModel, id=pk)
        form = TaskForm(instance=task)
        context = {"form": form}
        return render(request, "todo/update_task.html", context)

    @method_decorator(login_required)
    def post(self, request, pk, *args, **kwargs):
        """
        The 'post' method is implemented in this function.
        """
        task = get_object_or_404(TaskModel, id=pk)
        form = TaskForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
