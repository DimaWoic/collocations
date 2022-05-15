from django.urls import path
from .views import UserLoginView, UserLogoutView, CollocationsIndexView


urlpatterns = [
    path('index/', CollocationsIndexView.as_view(), name='index'),
    path('', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
