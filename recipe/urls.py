from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from vege.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("recipes/", include("vege.urls")),
    path("delete-recipe/<id>/", delete_recipe, name="delete_recipe"),
    path("update-recipe/<id>/", update_recipe, name="update_recipe"),
    path('login/', login_page, name="login_page"),
    path('register/', register_page, name="register_page"),
    path('logout/', logout_page, name="logout_page"),


    path("", include("vege.urls")),  # Root URL now points to the vege app
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    
urlpatterns += staticfiles_urlpatterns()