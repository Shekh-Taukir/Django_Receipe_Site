from django.shortcuts import render, redirect
from vege.models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/login/")
def receipes(request):
    if request.method == "POST":
        data = request.POST

        name = data.get("name")
        description = data.get("description")
        image = request.FILES.get("image")

        print(name + " - " + str(description) + " & File : " + str(image))
        Receipe.objects.create(
            name=name,
            description=description,
            image=image,
        )
        print(Receipe.objects.all())
        return redirect("/receipes/")
    queryset = Receipe.objects.all()

    if request.GET.get("search"):
        queryset = queryset.filter(name__icontains=request.GET.get("search"))

    context = {"receipes": queryset}

    return render(request, "receipes.html", context)


@login_required(login_url="/login/")
def update_receipe(request, id):
    queryset = Receipe.objects.get(id=id)
    if request.method == "POST":
        data = request.POST

        name = data.get("name")
        description = data.get("description")
        image = request.FILES.get("image")

        queryset.name = name
        queryset.description = description

        if image:
            queryset.image = image

        queryset.save()
        return redirect("/receipes/")

    context = {"receipe": queryset}
    return render(request, "update_receipes.html", context)


@login_required(login_url="/login/")
def delete_receipe(request, id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect("/receipes/")


def register_page(request):
    if request.method == "POST":
        data = request.POST

        first_name = data.get("first_name")
        last_name = data.get("last_name")
        username = data.get("username")
        password = data.get("password")

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, "Username already taken")
            return redirect("/register")

        user = User.objects.create(
            first_name=first_name, last_name=last_name, username=username
        )
        user.set_password(password)
        user.save()
        messages.info(request, "Account created successfully")
        return redirect("/register/")

    return render(request, "register.html")


def login_page(request):
    if request.method == "POST":
        data = request.POST

        username = data.get("username")
        password = data.get("password")

        user = User.objects.filter(username=username)

        if not user.exists():
            messages.error(request, "Invalid Username")
            return redirect("/login")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, "Invalid Username OR Password")
            return redirect("/login")
        else:
            login(request=request, user=user)

            return redirect("/receipes")

    return render(request, "login.html")


def logout_page(request):
    logout(request)
    return redirect("/login/")
