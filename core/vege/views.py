from django.shortcuts import render, redirect
from vege.models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q, Sum


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


def get_student(request):
    queryset = Student.objects.all()

    # ranks = Student.objects.annotate(marks=Sum("studentmarks__marks")).order_by(
    #     "-marks", "-student_age"
    # )

    # for rank in ranks:
    #     print(rank.marks)

    if request.GET.get("search"):
        search = request.GET.get("search")
        queryset = queryset.filter(
            Q(student_name__icontains=search)
            | Q(department__department__icontains=search)
            | Q(student_id__student_id__icontains=search)
            | Q(student_email__icontains=search)
            | Q(student_age__icontains=search)
        )

    # contact_list = Contact.objects.all()
    paginator = Paginator(queryset, 15)  # Show 25 contacts per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, "reports/students.html", {"queryset": page_obj})


# TaukirS-ER vid20 - imported the method to generate the data when view is loaded
from .seed import generate_report_card


def see_marks(request, student_id):
    # TaukirS-ER vid20 - call the method to generate the data for ReportCard MOdel
    # generate_report_card()
    queryset = SubjectMarks.objects.filter(student__student_id__student_id=student_id)
    total_marks = queryset.aggregate(total_marks=Sum("marks"))

    return render(
        request,
        "reports/see_marks.html",
        {
            "queryset": queryset,
            "total_marks": total_marks,
        },
    )
