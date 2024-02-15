from django.views import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# Create your views here.
class IndexView(View):

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return HttpResponse("Index View")
