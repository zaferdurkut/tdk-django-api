from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from dotenv import load_dotenv
import os
from rest_framework_swagger.views import get_swagger_view


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(dotenv_path=BASE_DIR)


schema_view = get_swagger_view(title='TDK Django Rest API')


urlpatterns = [
    path(r'', include('api.urls')),
    # path(str(os.getenv('DJANGO_ADMIN_URL')), admin.site.urls),
    url(r'^api-docs$', schema_view),

]