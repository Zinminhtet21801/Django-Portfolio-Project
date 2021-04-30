from django.shortcuts import render, get_object_or_404
from .models import blogProject
# Create your views here.
def blogHome(request):
    blogs = blogProject.objects.all()
    return render(request,'blog/blogHome.html',{'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(blogProject,pk = blog_id)
    return render(request,'blog/detail.html',{'blog':blog})
