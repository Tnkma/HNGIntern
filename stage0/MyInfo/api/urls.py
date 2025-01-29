from django.urls import path
from .views import Info

urlpatterns = [
    path('api/', Info.as_view(), name='myinfo'),
]