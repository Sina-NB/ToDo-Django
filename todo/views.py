from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import TaskModel
from .forms import TaskForm


# Create your views here.
class ListTaskView(View):

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        tasks = TaskModel.objects.filter(user=request.user)
        context = {"tasks": tasks}
        return render(request, "todo/list_task.html", context)


class DeleteTaskView(View):

    @method_decorator(login_required)
    def get(self, request, pk, *args, **kwargs):
        task = get_object_or_404(TaskModel, id=pk)
        task.delete()
        return redirect("/")


class CompleteTaskView(View):

    @method_decorator(login_required)
    def get(self, request, pk, *args, **kwargs):
        task = get_object_or_404(TaskModel, id=pk)
        task.completed = True
        task.save()
        return redirect("/")


class NotCompleteTaskView(View):

    @method_decorator(login_required)
    def get(self, request, pk, *args, **kwargs):
        task = get_object_or_404(TaskModel, id=pk)
        task.completed = False
        task.save()
        return redirect("/")


class CreateTaskView(View):

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
        return redirect("/")


class UpdateTaskView(View):

    @method_decorator(login_required)
    def get(self, request, pk, *args, **kwargs):
        task = get_object_or_404(TaskModel, id=pk)
        form = TaskForm(instance=task)
        context = {"form": form}
        return render(request, "todo/update_task.html", context)

    @method_decorator(login_required)
    def post(self, request, pk, *args, **kwargs):
        task = get_object_or_404(TaskModel, id=pk)
        form = TaskForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
