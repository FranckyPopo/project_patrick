from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from user import views
from front.views import front_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', front_index, name='page_index'),
    path('about', views.projet_patrick_about, name='page_about'),
    path('property', views.projet_patrick_property, name='page_property'),
    path('blog', views.projet_patrick_blog, name='page_blog'),
    path('property-single', views.projet_patrick_property_single, name='property_single'),
    path('blog-single', views.projet_patrick_blog_single, name='blog_single'),
    path('blog-grid', views.projet_patrick_agents_grid, name='agent_grid'),
    path('agent-single', views.projet_patrick_agents_single, name='agent_single'),
    path('contact', views.projet_patrick_contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT
    )
