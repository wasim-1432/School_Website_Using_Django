from django.contrib import admin
from .models import Student, Exam, SubjectMark

class SubjectMarkInline(admin.TabularInline):
    model = SubjectMark
    extra = 1

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_no', 'name', 'class_name')
    search_fields = ('roll_no', 'name')
    inlines = [SubjectMarkInline]

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('name', 'max_marks', 'date')
    search_fields = ('name',)
