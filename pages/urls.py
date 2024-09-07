from django.urls import path
from pages import views
from pages.views import HomePageView

urlpatterns=[ 

    path("",views.HomePageView.as_view())
]