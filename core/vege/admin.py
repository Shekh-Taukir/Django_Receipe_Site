from django.contrib import admin
from .models import *
from django.db.models import Sum

# Register your models here.
# TaukirS-ER vid20 - Register the models that are added in the models.py file

admin.site.register(Receipe)
admin.site.register(Department)
admin.site.register(StudentID)
admin.site.register(Student)


class SubjectMarkAdmin(admin.ModelAdmin):
    list_display = ["student", "subject", "marks"]


# Start TaukirS-ER vid20 - To add the model that can be accessed through admin, need to initilize it
class ReportCardAdmin(admin.ModelAdmin):
    list_display = ["student", "student_rank", "total_marks", "date_of_generation"]
    ordering = ["student_rank"]

    def total_marks(self, obj):
        subject_marks = SubjectMarks.objects.filter(student=obj.student)
        ls_subject_mark = subject_marks.aggregate(marks=Sum("marks"))
        return ls_subject_mark["marks"]


# End TaukirS-ER vid20

admin.site.register(Subject)
admin.site.register(SubjectMarks, SubjectMarkAdmin)
# TaukirS-ER vid20 - register of model reportCard
admin.site.register(ReportCard, ReportCardAdmin)
