from django.shortcuts import render
from front.models import SliderSite

# Create your views here.
def front_index(request):
    sliders = SliderSite.objects.all()
    return render(request, "projet_patrick/index.html", context={"sliders": sliders})




