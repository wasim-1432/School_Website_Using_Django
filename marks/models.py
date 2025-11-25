# marks/models.py
from django.db import models

class Student(models.Model):
    roll_no = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200, blank=True)
    mother_name = models.CharField(max_length=200, blank=True)
    class_name = models.CharField(max_length=50, blank=True)
    session = models.CharField(max_length=20, blank=True)
    dob = models.DateField(null=True, blank=True)
    adm_no = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.roll_no} - {self.name}"

class Exam(models.Model):
    name = models.CharField(max_length=100)   # e.g., Term-1, Annual
    max_marks = models.PositiveIntegerField(default=100)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class SubjectMark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='marks')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='exam_marks')
    subject = models.CharField(max_length=100)
    mark_obtained = models.PositiveIntegerField()
    max_mark = models.PositiveIntegerField(default=100)
    grade = models.CharField(max_length=3, blank=True)

    def __str__(self):
        return f"{self.student.roll_no} | {self.subject} : {self.mark_obtained}"

