from django.shortcuts import render
from posts.models import Post
from django.views.generic import TemplateView

class PostListTemplate(TemplateView):
  template_name="post-list.html"
  def get_context_data(self, **kwargs):
    context=super().get_context_data(**kwargs)
    post_data=Post.objects.all()
    context["data"]=post_data
    return context


# Create your views here.
def post_list_view(request):
  post_data=Post.objects.all()
  context={
    "data": post_data
  }
  return render(request, "post-list.html", context)

def portfolio_view(request):
  return render(request, "portfolio.html")