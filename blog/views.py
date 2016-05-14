from django.shortcuts import render
from django.utils import timezone
from .forms import PostForm

from .models import Post
from django.shortcuts import render, get_object_or_404

from django.shortcuts import redirect




def post_list(request,curpage=1):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    # 0, 10
    # 10, 20
    # 20, 30

    start_offset = (int(curpage)-1)*10
    end_offset = int(curpage)*10

    posts = Post.objects.all().order_by('-id')[start_offset:end_offset]

    allposts = Post.objects.all()

    ''' totalpages '''
    total_page = allposts.__len__() / 10 + 1

    o_pages = []
    for i in range(total_page):
        o_pages.append(i+1)


    return render(request, 'blog/post_list.html', {'posts': posts, 'allposts': allposts, 'total_page' : int(total_page), 'o_pages': o_pages, 'curpage' :int(curpage)})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):


    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_list')

    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})











