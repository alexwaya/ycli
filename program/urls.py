from django.urls import path
from . import views

urlpatterns = [

	#path("apply/", views.apply_program, name=apply_program),

	path("", views.program_view, name="programs"),

	path("<int:pk>/", views.program_detail, name="program_detail"),
	path("<int:pk>/apply/", views.apply_program, name="apply_program"),
	
    # path("", views.blog_index, name="blog_index"),
    # path("<int:pk>/", views.blog_detail, name="blog_detail"),
    path("<category>/", views.program_category, name="program_category"),
]