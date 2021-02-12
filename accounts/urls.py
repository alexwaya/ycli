from django.urls import path
from .views import SignUpView

from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),

    path("dashboard/", views.my_dashboard_view, name="my_dashboard_view"),

    path("dashboard/applications/", views.my_applications_view, name="my_applications_view"),
    
]



