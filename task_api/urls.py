"""Project URL Configuration."""

from django.contrib import admin
from django.urls import include, path
from decouple import config

# from django.conf import settings
# import debug_toolbar

ADMIN_URL = config('ADMIN_URL')
urlpatterns = [
    path('', include('taskapp.urls')),
    path(ADMIN_URL, admin.site.urls),
]

# if settings.DEBUG:
#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns
