from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import TemplateView

# Create your views here.

def index(request):
	return render(request,'index.html')

class LiveVideoFaceDetect(TemplateView):
    template_name = 'video.html'

    def post(self, request, *args, **kwargs):
        return JsonResponse(status=200, data={'message': 'Face detected'})
