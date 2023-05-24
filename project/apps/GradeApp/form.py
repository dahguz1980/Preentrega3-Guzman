from django import forms
from .models import Grade, Student, Subject, Teacher


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ["name", "description", "teacher"]


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["name", "lastname", "email"]


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "lastname", "email"]


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ["student", "subject", "grade"]
