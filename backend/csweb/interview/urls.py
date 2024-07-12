from django.urls import path, include
from interview.views.question import QuestionDetailView, QuestionListCreateView
from interview.views.subject import SubjectListView, SubjectDetailView
from interview.views.company import CompanyListView, CompanyDetailView
from interview.views.job import JobListView, JobDetailView
from interview.views.interview import InterviewListView, InterviewDetailView

urlpatterns = [
    path("user/", include("user.urls")),
    path("question/", QuestionListCreateView.as_view(), name="problem-list-create"),
    path("question/<int:pk>/", QuestionDetailView.as_view(), name="problem-detail"),
    path("subject/", SubjectListView.as_view(), name="subject-list"),
    path("subject/<int:pk>/", SubjectDetailView.as_view(), name="subject-detail"),
    path("company/", CompanyListView.as_view(), name="company-list"),
    path("company/<int:pk>/", CompanyDetailView.as_view(), name="company-detail"),
    path("job/", JobListView.as_view(), name="job-list"),
    path("job/<int:pk>/", JobDetailView.as_view(), name="job-detail"),
    path("", InterviewListView.as_view(), name="interview-list"),
    path("<int:pk>/", InterviewDetailView.as_view(), name="interview-detail"),
]
