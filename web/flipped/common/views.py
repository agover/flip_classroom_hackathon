from django.shortcuts import render
import core.models

# Create your views here.

def home(request):
    feed = core.models.VideoPage.objects.order_by('-upload_date')[:5]
    return render(request,'common/home.html', {'feed':feed})


