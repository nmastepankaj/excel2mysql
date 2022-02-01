from django.urls import path,include
from converter import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index,name="index"),
    path('index', views.index,name="index"),
    path('about', views.about,name="about"),
    path('contact', views.contact,name="contact"),
    path('uploadcsv', views.csv_upload,name="uploadcsv"),
    path('convertcsv/<file_name>', views.csv_convert,name="convertcsv"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)