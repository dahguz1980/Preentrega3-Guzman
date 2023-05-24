from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Grade, Subject, Student, Teacher
from django.contrib import messages


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
            messages.success(request, "Materia agregada satisfactoriamente.")
            return redirect(reverse("GradeApp:subjects"))
    else:  # GET
        form = SubjectForm()

    return render(request, "GradeApp/add_subject.html", {"form": form})


def teachers(request):
    teachers = Teacher.objects.all()
    contexto = {"teachers": teachers}
    return render(request, "GradeApp/teachers.html", contexto)


def add_teacher(request):
    from .form import TeacherForm

    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Profesor agregado satisfactoriamente.")
            return redirect(reverse("GradeApp:teachers"))
    else:  # GET
        form = TeacherForm()

    return render(request, "GradeApp/add_teacher.html", {"form": form})


def students(request):
    students = Student.objects.all()
    contexto = {"students": students}
    return render(request, "GradeApp/students.html", contexto)


def add_student(request):
    from .form import StudentForm

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Estudiante agregado satisfactoriamente.")
            return redirect(reverse("GradeApp:students"))
    else:  # GET
        form = StudentForm()

    return render(request, "GradeApp/add_student.html", {"form": form})


def grades(request):
    grades = Grade.objects.all()
    contexto = {"grades": grades}
    return render(request, "GradeApp/grades.html", contexto)


def add_grade(request):
    from .form import GradeForm

    if request.method == "POST":
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Calificación agregada satisfactoriamente.")
            return redirect(reverse("GradeApp:grades"))
    else:  # GET
        form = GradeForm()

    return render(request, "GradeApp/add_grade.html", {"form": form})
