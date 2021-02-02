from django.urls import path
from .views import SignUpView

from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),

    path("my-applications/", views.my_applications_view, name="my-applications"),
]



