from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required

from .forms import AdvertisementForm

from .models import Advertisement



def index(request):
    advertisements = Advertisement.objects.all()
    context = {
        'advertisements': advertisements
    }
    return render(request=request, template_name='first_app/index.html', context=context)

def top_sellers(request):
    return render(request=request, template_name='first_app/top-sellers.html')

@login_required(login_url=reverse_lazy('login'))
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
    return render(request=request, template_name='first_app/advertisement-post.html', context=context)

def advertisement_detail(request, pk):
    advertisement = Advertisement.objects.get(id=pk)
    context = {'adv' : advertisement}
    return render(request, 'first_app/advertisement.html', context)
