from django.shortcuts import render

def index(request):
    return render(
        request,
        "home.html",
        {
            "title": "Django example",
        },
    )


def classi(request):
    return render(
        request,
        "Classification.html",
        {
            "title": "Classifier les photos",
        },
    )