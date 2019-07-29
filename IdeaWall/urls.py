from django.urls import path, re_path
from django.views.generic import ListView, DetailView
from blog.models import Post

urlpatterns = [
                path('', ListView.as_view(
                                    queryset=Post.objects.all().order_by("-date")[:25],
                                    template_name="IdeaWall/IdeaWall.html")),

		re_path(r'^(?P<pk>\d+)$', DetailView.as_view(
                                    model = Post,
                                    template_name="IdeaWall/post.html")),
	    ]
