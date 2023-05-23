from django.db import models


class Subject(models.Model):
    """Model definition for Subject."""

    name = models.CharField(max_length=50)
    description = models.TextField()
    teacher = models.ForeignKey("Teacher", on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Subject."""

        db_table = "app_subject"
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"

    def __str__(self):
        return self.name


# Create your models here.
class Teacher(models.Model):
    """Model definition for Teacher."""

    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()

    class Meta:
        """Meta definition for Teacher."""

        db_table = "app_teacher"
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"

    def __str__(self):
        return self.name + " " + self.lastname


class Student(models.Model):
    """Model definition for Student."""

    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()

    class Meta:
        """Meta definition for Student."""

        db_table = "app_student"
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return self.name + " " + self.lastname


class Grade(models.Model):
    """Model definition for Grade."""

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.IntegerField()

    class Meta:
        """Meta definition for Grade."""

        db_table = "app_grade"
        verbose_name = "Grade"
        verbose_name_plural = "Grades"

    def __str__(self):
        return self.student.name + " " + self.student.lastname + " " + self.subject.name + " " + str(self.grade)
