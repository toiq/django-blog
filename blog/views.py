# from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Post

# Create your views here.


def post_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get("page", 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    # posts = Post.published.all()
    return render(request, "blog/post/list.html", {"posts": posts})


def post_detail(request, year, month, day, post):
    # try:
    #     post = Post.objects.get(id)
    # except Post.DoesNotExist:
    #     raise Http404("No post found.")
    post = get_object_or_404(
        Post,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
        status=Post.Status.PUBLISHED,
    )
    return render(request, "blog/post/detail.html", {"post": post})
