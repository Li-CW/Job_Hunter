from django.contrib import admin
from interview.models.question import Question
from interview.models.subject import Subject
from interview.models.job import Job
from interview.models.company import Company
from interview.models.interview import Interview


class InterviewAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "company", "job", "classification")
    ordering = ("-created_at",)
    search_fields = ["title"]
    list_per_page = 10
    list_display_links = ("title",)


admin.site.register(Question)
admin.site.register(Subject)
admin.site.register(Job)
admin.site.register(Company)
admin.site.register(Interview, InterviewAdmin)
