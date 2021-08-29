from .views import HomePageView, AboutView
from django.urls import path
urlpatterns=[
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
]