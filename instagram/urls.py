from django.conf.urls.static import static
from django.urls import path

from InstagramDjango import settings
from .views import index, NewImage, UserSignUp
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', index, name='all'),
    path('', NewImage, name='homepage'),
    path('signup/', UserSignUp.as_view(), name='signUp'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
