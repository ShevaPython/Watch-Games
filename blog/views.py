from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from .models import Post
from django.views.generic import ListView
from .forms import EmailPostForm


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 6
    template_name = 'blog/blog-list.html'


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED,
                             slug=post, publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request,
                  'blog/blog-detail.html',
                  {'post': post})


def post_share(request, post_id):
    post = get_object_or_404(Post,
                             id=post_id,
                             status=Post.Status.PUBLISHED)
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            recipient_email = [cd['recipient_email']]
            subject = (F"{cd['username']} recommends your read "
                       F"{post.title}")
            message = (F"{post.title} at {post_url} \n\n"
                       F"{cd['username']} comments {cd['message']}")
            send_mail(subject, message, cd['my_email'],recipient_email)
            sent = True

    else:
        form = EmailPostForm()

    return render(request, 'blog/share-post.html', {'post': post,
                                                    'form': form,
                                                    'sent': sent})
