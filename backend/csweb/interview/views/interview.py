from rest_framework import generics
from interview.models.interview import (
    Interview,
    InterviewSerializer,
    InterviewSerializer_list,
)
from utils.base_view import BaseView



class InterviewListView(BaseView, generics.ListCreateAPIView):
    queryset = Interview.objects.all().defer("body")
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return InterviewSerializer
        return InterviewSerializer_list
    def perform_create(self, serializer):
        serializer.save(author_id=self.request.user.id)

class InterviewDetailView(BaseView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
    def put(self, request, *args, **kwargs):
        pass

    def patch(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        pass