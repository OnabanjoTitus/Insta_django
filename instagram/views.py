from django.shortcuts import render

# Create your views here.
from instagram.models import ImageUpload


def index(request):
    images = ImageUpload.objects.all()
    context = {
        "images": images
    }
    return render(request, "index.html", context)
