from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from .views import index, top_sellers, advertisement_post, advertisement_detail

urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers', top_sellers, name='top-sellers'),
    path('advertisement-post', advertisement_post, name='adv_post'),
    path('advertisement/<int:pk>', advertisement_detail, name='adv_detail')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

