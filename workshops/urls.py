from django.urls import path
from . import views

urlpatterns = [

    path("", views.workshops_index, name="blog_index"),

    path("<int:pk>/", views.workshops_detail, name="workshops_detail"),

    path("<int:pk>/apply/", views.apply_workshop, name="apply_workshop"),

    # path("<int:pk>/", views.blog_detail, name="blog_detail"),
    # path("<category>/", views.blog_category, name="blog_category"),
]