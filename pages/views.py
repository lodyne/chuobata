from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "pages/home.html"

class AboutPageView(TemplateView):
    template_name = "pages/about.html"

class ForumPageView(TemplateView):
    template_name = "pages/forum.html"

class DiscussionPageView(TemplateView):
    template_name = "pages/discussion.html"

class SkillsPageView(TemplateView):
    template_name = "pages/skills.html"