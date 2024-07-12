from rest_framework import generics
from interview.models.question import (
    Question,
    QuestionSerializer,
    QuestionSerializer_exclude_answer,
)
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from utils.base_view import BaseView


class QuestionListCreateView(BaseView, generics.ListCreateAPIView):
    queryset = Question.objects.defer("answer")
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return QuestionSerializer
        return QuestionSerializer_exclude_answer
    def perform_create(self, serializer):
        serializer.save(author_id=self.request.user.id)
        

class QuestionDetailView(BaseView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def put(self, request, *args, **kwargs):
        pass

    def patch(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        pass
