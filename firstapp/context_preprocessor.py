from firstapp.models import NewsBase, Category


def latest_news_sidebar(request):
    latest_news_data = NewsBase.published.all().order_by('-publish_time')[:10]
    category_data = Category.objects.all()

    context = {
        'latest_news_data': latest_news_data,
        'category_data': category_data
    }
    return context
