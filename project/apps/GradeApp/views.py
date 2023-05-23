from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Subject, Student, Teacher


# Create your views here.
def index(request):
    subjects = Subject.objects.first()
    students = Student.objects.first()
    teachers = Teacher.objects.first()

    contexto = {
        "there_are_subjets": subjects != None,
        "there_are_teacher": teachers != None,
        "there_are_students": students != None,
    }

    return render(request, "GradeApp/index.html", contexto)


def subjects(request):
    subjects = Subject.objects.all()
    contexto = {"subjects": subjects}
    return render(request, "GradeApp/subjects.html", contexto)


def add_subject(request):
    from .form import SubjectForm

    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("GradeApp:subjects"))
    else:  # GET
        form = SubjectForm()

    return render(request, "GradeApp/add_subject.html", {"form": form})
