from django.urls import path
from projects import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.project_list),
    path('sign_up/', views.sign_up),
    path('sign_in/',views.sign_in),
    path('contact/',views.contact),
    path('about/',views.about),
    path('download/',views.download),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)