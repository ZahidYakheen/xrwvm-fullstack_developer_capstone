from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'djangoapp'
urlpatterns = [
    # path for login
    path(route='login', view=views.login_user, name='login'),
    
    # path for logout
    path(route='logout', view=views.logout_user, name='logout'),
    
    # path for registration
    path(route='register', view=views.registration, name='register'),
    
    # path for dealer reviews view
    path(route='get_cars', view=views.get_cars, name ='getcars'),
    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
