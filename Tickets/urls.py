from django.urls import path
from .views import home
from .views import Create, ListPosts
#from .views import CustomLoginView

urlpatterns = [
    path('', home, name="home"),
    path('create', Create.as_view(), name="create"),
    path('list', ListPosts.as_view(), name= "list"),
]


