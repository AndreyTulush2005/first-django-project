from django.shortcuts import render
from .models import Advertisement

def index(request):
    advertisements = Advertisement.objects.all()
    context = {
        'advertisements': advertisements
    }
    return render(request=request, template_name='index.html', context=context)

def top_sellers(request):
    return render(request=request, template_name='top-sellers.html')