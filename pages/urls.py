from django.urls import path

from .views import (
    DiscussionPageView,
    ForumPageView, 
    HomePageView, 
    AboutPageView, 
    SkillsPageView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("forum/", ForumPageView.as_view(), name="forum"),
    path("discussion/", DiscussionPageView.as_view(), name="discussion"),
    path("skill/", SkillsPageView.as_view(), name="skill"),
]
