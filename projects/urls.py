from django.urls import path
from projects import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('sign_up/', views.sign_up),
    path('sign_in/',views.sign_in),
    path('contact/',views.contact),
    path('about/',views.about),
    path('download/',views.download),
    path('projects/', views.projects),
    path('projects/<int:pk>', views.project_detail)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)