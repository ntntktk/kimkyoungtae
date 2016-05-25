from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Post
from .forms import PostForm

def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', {
        'post_list': post_list,
        })

def post_detail(request):
    return render(request, 'blog.views.post_detail')

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if forms.is_valid():
            post = form.save()
            return redirect('blog.views.index')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {
        'form': form,
        })