from django.urls import path
from .controllers import RoomView


urlpatterns = [
    path('home', RoomView.as_view())
]
