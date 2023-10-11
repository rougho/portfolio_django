from django.urls import path
from projects import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "projects"

urlpatterns = [
    path('', views.home),
    path('sign_up/', views.sign_up,name="signup"),
    path('sign_in/',views.sign_in, name="signin"),
    path('contact/',views.contact, name="contact"),
    path('about/',views.about, name="about"),
    path('download/',views.download, name="download"),
    path('projects/', views.projects, name="projects"),
    path('projects/<int:pk>', views.project_detail, name="project_detail")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)