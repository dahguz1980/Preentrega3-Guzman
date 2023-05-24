from django.urls import path

from . import views


app_name = "GradeApp"

urlpatterns = [
    path("", views.index, name="index"),
    path("subjects/", views.subjects, name="subjects"),
    path("add_subject/", views.add_subject, name="add_subject"),
    path("teachers/", views.teachers, name="teachers"),
    path("add_teacher/", views.add_teacher, name="add_teacher"),
    path("students/", views.students, name="students"),
    path("add_student/", views.add_student, name="add_student"),
    path("grades/", views.grades, name="grades"),
    path("add_grade/", views.add_grade, name="add_grade"),
]
