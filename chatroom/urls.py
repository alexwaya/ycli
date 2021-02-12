from django.urls import path
from . import views

urlpatterns = [
    path("chats/", views.chat_index, name="chat_index"),
    path("chat/<int:pk>/", views.chat_detail, name="chat_detail"),

    path("issue/", views.raise_issue, name="raise_issue"),

    #path("<category>/", views.chat_category, name="chat_category"),
]