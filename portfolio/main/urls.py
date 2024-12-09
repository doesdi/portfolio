from django.urls import path
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    path('', cache_page(60)(home), name='home'),
    path('about/', about, name = 'about'),
    path('reviews/', cache_page(60)(reviews), name = 'reviews'),
    path('logout/', Logout_user, name="logout"),
    path('login/', LoginUser.as_view(), name="login"),
    path('reg/', Register, name="reg"),

]