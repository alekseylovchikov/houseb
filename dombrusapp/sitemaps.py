from django.contrib.sitemaps import Sitemap
from.models import Project


class ProjectSitemap(Sitemap):

    def items(self):
        return Project.objects.all()
