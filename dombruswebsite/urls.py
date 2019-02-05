from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from dombrusapp import views

urlpatterns = [
    path(r'^tinymce/', include('tinymce.urls')),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('brusovye', views.brus, name='brus'),
    path('bani', views.bani, name='bani'),
    path('karkasnye', views.karkas, name='karkas'),
    path('contacts', views.contacts, name='contacts'),
    path('search', views.search, name='search'),
    path('project/<int:project_id>', views.project, name='project'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
