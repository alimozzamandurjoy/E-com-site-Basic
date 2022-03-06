from django.urls import URLPattern, path
from .import views
from .views import *

urlpatterns= [

    path("",views.index, name='index'),
    path('<int:id>/',views.detail,name='detail'),

]