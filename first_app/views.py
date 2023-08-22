from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import AdvertisementForm

from .models import Advertisement



def index(request):
    advertisements = Advertisement.objects.all()
    context = {
        'advertisements': advertisements
    }
    return render(request=request, template_name='index.html', context=context)

def top_sellers(request):
    return render(request=request, template_name='top-sellers.html')

def advertisement_post(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main-page')

            return redirect(url)
    else:
        form = AdvertisementForm()

    context = {
        'form': form
    }
    return render(request=request, template_name='advertisement-post.html', context=context)
