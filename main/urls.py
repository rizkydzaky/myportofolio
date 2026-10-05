from django.urls import path

from main.views import (
    show_experience,
    show_main,
    show_projects,
    create_project,
    create_project_ajax,
    update_project,
    create_experience,
    create_experience_ajax,
    update_experience,
    delete_experience,
    get_experiences_json,
    get_projects_json,
    delete_project,
    register,
    login_user,
    logout_user,
    toggle_star,
)

app_name = "main"


urlpatterns = [
    path(
        "",
        show_main,
        name="show_main",
    ),

    # =========================
    # PROJECT
    # =========================

    path(
        "projects/",
        show_projects,
        name="show_projects",
    ),

    path(
        "projects/add/",
        create_project,
        name="create_project",
    ),

    path(
        "projects/add-ajax/",
        create_project_ajax,
        name="create_project_ajax",
    ),

    path(
        "projects/<uuid:project_id>/edit/",
        update_project,
        name="update_project",
    ),

    path(
        "api/projects/",
        get_projects_json,
        name="get_projects_json",
    ),

    path(
        "projects/<uuid:project_id>/delete/",
        delete_project,
        name="delete_project",
    ),

    path(
        "projects/<uuid:project_id>/star/",
        toggle_star,
        name="toggle_star",
    ),

    # =========================
    # EXPERIENCE
    # =========================

    path(
        "experience/",
        show_experience,
        name="show_experience",
    ),

    path(
        "experience/add/",
        create_experience,
        name="create_experience",
    ),

    path(
        "api/experiences/",
        get_experiences_json,
        name="get_experiences_json",
    ),

    path(
        "api/experiences/create/",
        create_experience_ajax,
        name="create_experience_ajax",
    ),

    path(
        "experience/<uuid:experience_id>/edit/",
        update_experience,
        name="update_experience",
    ),

    path(
        "experience/<uuid:experience_id>/delete/",
        delete_experience,
        name="delete_experience",
    ),

    # =========================
    # AUTHENTICATION
    # =========================

    path(
        "register/",
        register,
        name="register",
    ),

    path(
        "login/",
        login_user,
        name="login",
    ),

    path(
        "logout/",
        logout_user,
        name="logout",
    ),
]
