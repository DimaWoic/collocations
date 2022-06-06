from django.urls import path
from .views import UserLoginView, UserLogoutView, CollocationsIndexView


urlpatterns = [
    path('', CollocationsIndexView.as_view(), name='index'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
