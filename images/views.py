from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Image
from .forms import ImageCreateFrom
from actions.utils import create_action
from WatchGames.utils_redis.redis_utils import get_redis_connection

r = get_redis_connection()


@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImageCreateFrom(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_image = form.save(commit=False)
            new_image.user = request.user
            new_image.save()
            create_action(request.user, 'bookmarked image', new_image)
            messages.success(request,
                             'Image added successfully')
            return redirect(new_image.get_absolute_url())
    else:
        # скомпоновать форму с данными,
        # предоставленными букмарклетом методом GET
        form = ImageCreateFrom(data=request.GET)
    return render(request,
                  'images/image/create.html',
                  {'section': 'images',
                   'form': form})


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    # увеличить общее число просмотров изображения на 1
    total_views = r.incr(f'image:{image.id}:views')
    # увеличить рейтинг изобажения на 1
    r.zincrby('image_ranking', 1, image.id)
    return render(request, 'images/image/detail.html', {'section': 'images',
                                                        'image': image,
                                                        'total_views': total_views})


@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.user_like.add(request.user)
                create_action(request.user, 'likes', image)
            else:
                image.user_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except Image.DoesNotExist:
            pass
        return JsonResponse({'status': 'error'})


@login_required
def image_list(request):
    images = Image.objects.all()
    paginator = Paginator(images, 5)
    page = request.GET.get('page')
    images_only = request.GET.get('images_only')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, то доставить первую страницу
        images = paginator.page(1)
    except EmptyPage:
        if images_only:
            # Если AJAX-запрос и страница вне диапазона,
            # то вернуть пустую страницу
            return HttpResponse('')
        # Если страница вне диапазона,
        # то вернуть последнюю страницу результатов
        images = paginator.page(paginator.num_pages)
    if images_only:
        return render(request,
                      'images/image/list_images.html',
                      {'section': 'images',
                       'images': images})
    return render(request,
                  'images/image/list.html',
                  {'section': 'images',
                   'images': images})


@login_required
def image_ranking(request):
    # получить словарь рейтинга изображений
    image_ranking = r.zrange('image_ranking', 0, -1,
                             desc=True)[:10]
    image_ranking_ids = [int(id) for id in image_ranking]
    print("Image Ranking IDs:", image_ranking_ids)
    # получить наиболее просматриваемые изображения
    most_viewed = list(Image.objects.filter(
        id__in=image_ranking_ids))
    most_viewed.sort(key=lambda x: image_ranking_ids.index(x.id))
    # Добавим отладочную информацию
    print("Most Viewed Images:", most_viewed)
    return render(request,
                  'images/image/ranking.html',
                  {'section': 'images',
                   'most_viewed': most_viewed})
