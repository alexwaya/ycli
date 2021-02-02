from django.urls import path
from . import views

urlpatterns = [
    path("", views.chat_index, name="chat_index"),
    path("<int:pk>/", views.chat_detail, name="chat_detail"),

    path("start/", views.raise_issue, name="raise_issue"),

    #path("<category>/", views.chat_category, name="chat_category"),
]