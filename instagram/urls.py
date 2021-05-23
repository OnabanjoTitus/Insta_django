from django.conf.urls.static import static
from django.urls import path

from InstagramDjango import settings
from .views import index, NewImage, UserSignUp

urlpatterns = [

    path('', index, name='all'),
    path('', NewImage, name='homepage'),
    path('signup/', UserSignUp.as_view(), name='signUp'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
