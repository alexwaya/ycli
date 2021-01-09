from django.urls import path
from . import views

urlpatterns = [

    path("", views.events_index, name="blog_index"),

    path("<int:pk>/", views.event_detail, name="event_detail"),

    path("<int:pk>/apply/", views.apply_event, name="apply_event"),

    # path("<int:pk>/", views.blog_detail, name="blog_detail"),
    # path("<category>/", views.blog_category, name="blog_category"),
]