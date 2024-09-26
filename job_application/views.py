from django.shortcuts import render
from .forms import ApplicationForm #the dot at the beginning is because we want to import from the same directory, not the root directory


def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data["first_name"] # dictionary created by Django which pics the names from the HTML
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]
            print(first_name)
    return render(request, "index.html")
