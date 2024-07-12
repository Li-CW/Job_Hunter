from rest_framework import generics
from interview.models.subject import Subject, SubjectSerializer


class SubjectListView(generics.ListCreateAPIView):

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def create(self, request, *args, **kwargs):
        pass


class SubjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def put(self, request, *args, **kwargs):
        pass

    def patch(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        pass
