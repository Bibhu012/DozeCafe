from django.urls import path
#from django.urls import include
from . import views

urlpatterns = [
    #path('', include('calc.urls')),
    path('', views.home, name = 'home'),
    path('add',views.add, name='add')
]
