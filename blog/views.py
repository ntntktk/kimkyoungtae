from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render, get_object_or_404
from .models import Post
from .forms import PostForm, PostSimpleForm, CommentForm, CommentForm2
from django.contrib import messages

def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', {
        'post_list': post_list,
        })

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html',{
        'post': post,
        })

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if forms.is_valid():
            post = form.save()
            messages.success(request, '새로운 포스팅을 등록했습니다.')
            return redirect(post)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {
        'form': form,
        })

def comment_new(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = CommentForm2(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post)
    else:
        form = CommentForm2()
    return render(request, 'blog/comment_form.html', {
        'form': form
        })