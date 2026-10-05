import datetime

from django.shortcuts import get_object_or_404, redirect, render
from main.models import Experience, Project
from main.forms import ProjectForm, ExperienceForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.views.decorators.http import require_POST


def is_editor(user):
    return user.is_authenticated and user.groups.filter(name="Editor").exists()


def show_main(request):
    last_login = request.COOKIES.get("last_login", "Belum pernah login")

    context = {
        "name": "Rizky Dzaky",
        "npm": "2506657301",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Mahasiswa Sistem Informasi Universitas Indonesia yang tertarik pada"
            " pengembangan perangkat lunak dan pendidikan."
        ),
        "last_login": last_login,
    }

    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Rizky Dzaky",
        "is_editor": is_editor(request.user),
    }

    return render(request, "experience.html", context)


def show_projects(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Rizky Dzaky",
        "title_query": title_query,
        "form": ProjectForm(),
    }

    return render(request, "project.html", context)


def get_experiences_json(request):
    search_query = request.GET.get("search", "").strip()

    experiences = Experience.objects.all().order_by("-started_at")

    if search_query:
        experiences = experiences.filter(
            title__icontains=search_query
        )

    data = []

    for experience in experiences:
        data.append({
            "id": str(experience.id),
            "title": experience.title,
            "description": experience.description,
            "category": experience.category,
            "category_display": experience.get_category_display(),
            "thumbnail": experience.thumbnail,
            "started_at": experience.started_at.strftime("%d %B %Y"),
            "ended_at": (
                experience.ended_at.strftime("%d %B %Y")
                if experience.ended_at
                else None
            ),
            "is_ongoing": experience.is_ongoing,
        })

    return JsonResponse(data, safe=False)


def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.prefetch_related("starred_by").all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    data = []

    for project in projects:
        starred_users = project.starred_by.all()

        is_starred = (
            request.user in starred_users
            if request.user.is_authenticated
            else False
        )

        starred_by_names = ", ".join(
            [user.username for user in starred_users]
        )

        data.append({
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "tech_stack": project.tech_stack,
                "project_url": project.project_url,
                "project_image_url": project.project_image_url,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)


@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Rizky Dzaky",
        "form": form,
    }

    return render(request, "projects_form.html", context)


@login_required(login_url="/login/")
def update_project(request, project_id):
    if not request.user.is_superuser and not is_editor(request.user):
        raise PermissionDenied

    project = get_object_or_404(Project, pk=project_id)
    form = ProjectForm(request.POST or None, instance=project)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Project berhasil diperbarui!")
        return redirect("main:show_projects")

    context = {
        "name": "Rizky Dzaky",
        "form": form,
        "project": project,
    }

    return render(request, "projects_form.html", context)


@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Rizky Dzaky",
        "form": form,
    }

    return render(request, "experience_form.html", context)


@login_required(login_url="/login/")
def update_experience(request, experience_id):
    if not request.user.is_superuser and not is_editor(request.user):
        raise PermissionDenied

    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience berhasil diperbarui!")
        return redirect("main:show_experience")

    context = {
        "name": "Rizky Dzaky",
        "form": form,
        "experience": experience,
    }

    return render(request, "experience_form.html", context)


@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if not request.user.is_superuser:
        raise PermissionDenied

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")


@login_required(login_url="/login/")
def delete_project(request, project_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")


@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")


def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Rizky Dzaky",
        "form": form,
    }

    return render(request, "register.html", context)


def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        messages.success(request, "Berhasil login!")

        response = redirect("main:show_main")

        response.set_cookie(
            "last_login",
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        )

        return response

    context = {
        "name": "Rizky Dzaky",
        "form": form,
    }

    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    messages.success(request, "Kamu berhasil logout.")

    response = redirect("main:show_main")
    response.delete_cookie("last_login")

    return response


@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {
                "message": (
                    "Hanya pemilik portofolio yang dapat "
                    "menambahkan proyek."
                )
            },
            status=403,
        )

    form = ProjectForm(request.POST)

    if form.is_valid():
        project = form.save()

        return JsonResponse(
            {
                "message": "Proyek berhasil ditambahkan.",
                "pk": str(project.id),
            },
            status=201,
        )

    return JsonResponse(
        {
            "errors": form.errors.get_json_data(),
        },
        status=400,
    )


@require_POST
def create_experience_ajax(request):
    if not request.user.is_authenticated:
        return JsonResponse(
            {
                "message": (
                    "Kamu harus login untuk menambahkan experience."
                )
            },
            status=403,
        )

    if not request.user.is_superuser:
        return JsonResponse(
            {
                "message": (
                    "Hanya pemilik portofolio yang dapat "
                    "menambahkan experience."
                )
            },
            status=403,
        )

    form = ExperienceForm(request.POST)

    if form.is_valid():
        experience = form.save()

        return JsonResponse(
            {
                "message": "Experience berhasil ditambahkan.",
                "id": str(experience.id),
            },
            status=201,
        )

    return JsonResponse(
        {
            "message": "Data experience tidak valid.",
            "errors": form.errors.get_json_data(),
        },
        status=400,
    )
