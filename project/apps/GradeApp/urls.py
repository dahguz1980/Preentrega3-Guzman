from django.urls import path

from .views import index, subjects, add_subject


app_name = "GradeApp"

urlpatterns = [
    path("", index, name="index"),
    path("subjects/", subjects, name="subjects"),
    path("add_subject/", add_subject, name="add_subject"),
]
