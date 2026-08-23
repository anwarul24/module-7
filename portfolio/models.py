from django.db import models


class Project(models.Model):
    """
    Represents a single project shown on the portfolio site.
    """
    title = models.CharField(max_length=150)
    description = models.TextField(help_text="Short description of the project")
    technology = models.CharField(
        max_length=200,
        help_text="Comma separated list of technologies, e.g. Django, HTML, CSS"
    )
    github_link = models.URLField(help_text="Link to the public GitHub repository")
    image = models.ImageField(
        upload_to="project_images/",
        blank=True,
        null=True,
        help_text="Optional screenshot / thumbnail for the project"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def technology_list(self):
        """Return the technology field split into a clean list for templates."""
        return [tech.strip() for tech in self.technology.split(",") if tech.strip()]
