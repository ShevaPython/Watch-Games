from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

from .models import Post
from django.views.generic import ListView
from .forms import EmailPostForm, CommendForm, SearchForm
from django.views.decorators.http import require_POST
from taggit.models import Tag


# class PostListView(ListView):
#     queryset = Post.published.all()
#     context_object_name = 'posts'
#     paginate_by = 6
#     template_name = 'blog/blog-list.html'

def post_list(request, tag_slug=None):
    """Список всех постов"""
    post_list = Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])
    # Постраничная разбивка с 3 постами на страницу
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # Если page_number не целое число, то
        # выдать первую страницу
        posts = paginator.page(1)
    except EmptyPage:
        # Если page_number находится вне диапазона, то
        # выдать последнюю страницу результатов
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/blog-list.html',
                  {'posts': posts,
                   'tag': tag})


def post_detail(request, year, month, day, post):
    """Детальная информация о посте"""
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED,
                             slug=post, publish__year=year,
                             publish__month=month,
                             publish__day=day)
    # Список активных комментариев к этому посту
    comments = post.comments.filter(active=True)
    comment_form = CommendForm()

    if request.method == 'GET' and 'query' in request.GET:
        search_form = SearchForm(request.GET)

        if search_form.is_valid():
            search_query = search_form.cleaned_data['query']



            # Перенаправьте на страницу post_search с параметром запроса
            return redirect('blog:post_search', query=search_query)
    else:
        search_form = SearchForm()
    # Список схожих постов
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')) \
                        .order_by('-same_tags', '-publish')[:4]
    return render(request,
                  'blog/blog-detail.html',
                  {'post': post,
                   'comment_form': comment_form,
                   'comments': comments,
                   'similar_posts': similar_posts,
                   'search_form':search_form})


def post_share(request, post_id):
    """Поделиться постом"""
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
            send_mail(subject, message, cd['my_email'], recipient_email)
            sent = True

    else:
        form = EmailPostForm()

    return render(request, 'blog/share-post.html', {'post': post,
                                                    'form': form,
                                                    'sent': sent})


@require_POST
def post_comment(request, post_id):
    """Оставить коментарий"""
    post = get_object_or_404(Post,
                             id=post_id,
                             status=Post.Status.PUBLISHED)
    comment = None
    # Клментарий был отправлен
    form = CommendForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(request, 'blog/comment.html', {'post': post,
                                                 'form': form,
                                                 'comment': comment})


def post_search(request):
    search_form = SearchForm()
    query = request.GET.get('query')
    results = []
    if request.method == 'GET' and 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_vector = SearchVector('title', weight='A') + \
                            SearchVector('body', weight='B')
            search_query = SearchQuery(query)
            results = Post.published.annotate(
                search=search_vector,
                rank=SearchRank(search_vector, search_query)
            ).filter(rank__gte=0.3).order_by('-rank')
    return render(request, 'blog/search-post.html',
                  {'search_form': search_form,
                   'query': query,
                   'results': results})
