# marks/views.py
from django.shortcuts import render, get_object_or_404
from .models import Student, SubjectMark, Exam
from django.http import HttpResponse
# for PDF: from django.template.loader import render_to_string
# and WeasyPrint if used

def marksheet_view(request):
    context = {}

    if request.method == "POST":
        roll = request.POST.get('roll_no', '').strip()

        if not roll:
            context['error'] = "Roll number daalein."
        else:
            student = Student.objects.filter(roll_no=roll).first()

            if not student:
                context['error'] = f"{roll} No record found for"
            else:
                # Fetch marks
                marks = student.marks.select_related('exam').all().order_by('exam__name', 'subject')

                # Calculate totals 
                total_obtained = sum(m.mark_obtained for m in marks)
                total_max = sum(m.max_mark for m in marks)

                context.update({
                    'student': student,
                    'marks': marks,
                    'total_obtained': total_obtained,
                    'total_max': total_max
                })

    return render(request, "marks_lookup.html", context)

# Example: PDF generation with WeasyPrint (install weasyprint)
def marksheet_pdf(request, roll):
    student = get_object_or_404(Student, roll_no=roll)
    marks = student.marks.select_related('exam').all()
    html = render_to_string('marksheet_print.html', {'student': student, 'marks': marks})
    # WeasyPrint
    from weasyprint import HTML
    pdf = HTML(string=html).write_pdf()
    return HttpResponse(pdf, content_type='application/pdf')

def add_marks(request):
    students = Student.objects.all()
    exams = Exam.objects.all()

    if request.method == "POST":
        student_id = request.POST.get("student")
        exam_id = request.POST.get("exam")

        student = Student.objects.get(id=student_id)
        exam = Exam.objects.get(id=exam_id)

        # subjects list — 
        subjects = request.POST.getlist("subject")
        obtained_list = request.POST.getlist("obtained")
        max_list = request.POST.getlist("max_mark")
        grade_list = request.POST.getlist("grade")

        for s, o, m, g in zip(subjects, obtained_list, max_list, grade_list):
            SubjectMark.objects.create(
                student=student,
                exam=exam,
                subject=s,
                mark_obtained=o,
                max_mark=m,
                grade=g
            )

        return render(request, "success.html", {"msg": "Marks Added Successfully!"})

    return render(request, "add_marks.html", {
        "students": students,
        "exams": exams
    })

