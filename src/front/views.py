from django.shortcuts import render

# Create your views here.
def front_index(request):
    return render(request, "projet_patrick/index.html")