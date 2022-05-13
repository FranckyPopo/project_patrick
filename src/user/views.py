from django.shortcuts import render

# Create your views here.

def projet_patrick_about(request):
    return render(request, "projet_patrick/about.html")

def projet_patrick_property(request):
    return render(request, "projet_patrick/property-grid.html")

def projet_patrick_blog(request):
    return render(request, "projet_patrick/blog-grid.html")

def projet_patrick_property_single(request):
    return render(request, "projet_patrick/property-single.html")

def projet_patrick_blog_single(request):
    return render(request, "projet_patrick/blog-single.html")

def projet_patrick_agents_grid(request):
    return render(request, "projet_patrick/agents-grid.html")

def projet_patrick_agents_single(request):
    return render(request, "projet_patrick/agent-single.html")

def projet_patrick_contact(request):
    return render(request, "projet_patrick/contact.html")

