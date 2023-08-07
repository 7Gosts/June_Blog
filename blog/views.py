from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from django.core.paginator import Paginator


# Create your views here.

def hello_world(request):
    return HttpResponse("Hello World!")


def article_content(request):
    atc = Article.objects.all()[0]
    title = atc.title
    brief = atc.brief
    content = atc.content
    a_id = atc.article_id
    date = atc.publish_date
    re_str = 'title: %s,brief_content: %s' \
             'content: %s, article_id: %s, publish_date: %s' % (title,
                                                                brief,
                                                                content,
                                                                a_id,
                                                                date)
    return HttpResponse(re_str)


def get_index_page(request):
    all_article = Article.objects.all()
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1
    pg = Paginator(all_article, 3)
    p_num = pg.num_pages
    print('page num: ', pg.num_pages)
    pa_list = pg.page(page)
    if pa_list.has_next():
        next_page = page + 1
    else:
        next_page = page
    if pa_list.has_previous():
        pre_page = page - 1
    else:
        pre_page = page
    tp5 = Article.objects.order_by('-publish_date')[:2]
    return render(request, 'blog/index.html',
                  {
                      'article_list': pa_list,
                      'page_num': range(1,p_num+1),
                      'curr_page': page,
                      'next_page': next_page,
                      'previous_page': pre_page,
                      'top5_articles': tp5   # 最近五篇文章
                  }
                  )
    pass


def get_detail_page(request, article_id):
    all_article = Article.objects.all()
    curr = None
    pre_inx = 0
    next_inx = len(all_article)
    pre_art = None
    next_art = None
    for index, article in enumerate(all_article):
        if index == 0:
            pre_inx = 0
            next_inx = index + 1
        elif index == len(all_article) - 1:
            next_inx = index
            pre_inx = index - 1
        else:
            pre_inx = index - 1
            next_inx = index + 1
        if article.article_id == article_id:
            curr = article
            pre_art = all_article[pre_inx]
            next_art = all_article[next_inx]
            break

    section_list = curr.content.split('\n')
    return render(request, 'blog/detail.html',
                  {
                      'curr_article': curr,
                      'section_list': section_list,
                      'pre_art': pre_art,
                      'next_art': next_art
                  }
                  )
