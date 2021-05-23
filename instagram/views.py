from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic


from instagram.models import ImageUpload


def index(request):
    if request.method == 'POST':
        form = NewImage(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all')
    images = ImageUpload.objects.all()
    form = NewImage()
    context = {
        "images": images,
        "form": form
    }
    return render(request, "index.html", context)


class NewImage(ModelForm):
    class Meta:
        model = ImageUpload
        fields = "__all__"


class UserSignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
