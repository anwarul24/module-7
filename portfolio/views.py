from django.shortcuts import render, get_object_or_404
from .models import Project


def home(request):
    """Homepage: name, profile picture, intro, skills, nav."""
    context = {
        "skills": [
            "Python", "Django", "HTML5", "CSS3",
            "JavaScript", "Git & GitHub", "MySQL/SQLite",
        ],
    }
    return render(request, "portfolio/home.html", context)


def about(request):
    """Bonus: About page with more detail about the developer."""
    return render(request, "portfolio/about.html")


def project_list(request):
    """Projects page: shows all projects as cards."""
    projects = Project.objects.all()
    return render(request, "portfolio/projects.html", {"projects": projects})


def project_detail(request, pk):
    """Project details page: /projects/<id>/"""
    project = get_object_or_404(Project, pk=pk)
    return render(request, "portfolio/project_detail.html", {"project": project})


def contact(request):
    """Bonus: simple contact page."""
    return render(request, "portfolio/contact.html")
