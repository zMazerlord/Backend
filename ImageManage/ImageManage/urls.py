from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
# функция для возврата картинки
from upload_app.views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('url_hex/', home_page),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)