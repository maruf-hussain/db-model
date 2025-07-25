from django.urls import path
from .views  import  *

urlpatterns = [
    path('myapp/',  get_products,  name='get_products'),
]
