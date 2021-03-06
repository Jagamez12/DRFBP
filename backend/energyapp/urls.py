from django.views.generic import TemplateView
from django.urls import path, include, re_path
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('code/', include('codes_verification.urls')),
]

#urlpatterns += [re_path(r"^.*", TemplateView.as_view(template_name = 'index.html'))]