from django.forms import ModelForm
from django.shortcuts import render, redirect

# Create your views here.
from instagram.models import ImageUpload


def index(request):
    if request.method == 'POST':
        form = NewImage(request.POST)
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
