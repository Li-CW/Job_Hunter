from django.shortcuts import render


def index(request):

    return render(request, "jobhunter.html")

# 404
def page_not_found(request, exception):
    return render(request, "index.html")

# 500
def page_error(request):
    return render(request, "index.html")
