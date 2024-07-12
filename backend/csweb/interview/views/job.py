from rest_framework import generics
from interview.models.job import Job, JobSerializer


class JobListView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    def create(self, request, *args, **kwargs):
        pass

class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
