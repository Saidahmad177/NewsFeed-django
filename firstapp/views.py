from django.shortcuts import render, get_object_or_404
from firstapp.models import NewsBase, Category
from firstapp.forms import FormContact
from django.template import loader
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView


# def home(request):
#     category = Category.objects.all()
#     newsbase = NewsBase.published.all().order_by('-publish_time')[:5]
#     local_news = NewsBase.published.filter(category__name='Mahalliy')[1:3]
#     local_one = NewsBase.published.filter(category__name='Mahalliy')[:1]
#
#     context = {
#         'newsbase': newsbase,
#         'category': category,
#         'local_news': local_news,
#         'local_one': local_one,
#     }
#
#     return render(request, 'firstapp/first.html', context)

class HomePage(ListView):
    model = NewsBase
    template_name = 'firstapp/first.html'
    context_object_name = 'newsbase'

    def get_context_data(self, ** kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['local_news'] = NewsBase.published.filter(category__name='local').order_by('-publish_time')[:5]
        context['newsbase'] = NewsBase.published.all().order_by('-publish_time')[:5]
        context['global_news'] = NewsBase.published.filter(category__name='global').order_by('-publish_time')[:5]
        context['technology'] = NewsBase.published.filter(category__name='technology').order_by('-publish_time')[:5]
        context['sport'] = NewsBase.published.filter(category__name='sport').order_by('-publish_time')[:5]

        return context


class Global(TemplateView):
    template_name = 'firstapp/categorys.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_name = kwargs['request2']
        category = get_object_or_404(Category, name=category_name)
        context['category'] = category

        context['all_category_data'] = NewsBase.published.filter(category__name=category_name).order_by('-publish_time')

        return context


class oddiy(ListView):
    model = NewsBase
    template_name = 'oddiy.html'
    context_object_name = 'oddiy'

    def get_queryset(self):
        return self.model.published.all().filter(category__name='Sport').order_by('-publish_time')



# class Global(ListView):
#     category_model = NewsBase
#     template_name = 'firstapp/global.html'
#     context_object_name = 'global_news'
#
#     def get_queryset(self):
#         data = self.category_model.published.all().filter(category__name='Global')
#         return data


class ContactPage(TemplateView):
    template_name = 'contact.html'

    def get(self, request, *args, **kwargs):
        form = FormContact()
        context = {
            'form': form
        }
        return render(request, 'contact.html', context)

    def post(self, request, *args, **kwargs):
        form = FormContact(request.POST)
        context = {
            'form': form
        }
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse('dfsadlkfj')

        return render(request, 'contact.html', context)


def page_404(request):
    return render(request, '404.html')


def detail_page(request, news, category_name):
    data = get_object_or_404(NewsBase, slug=news, category__name=category_name, status=NewsBase.Status.published)
    context = {
        'data': data
    }
    return render(request, 'firstapp/detail_page.html', context)


# def about(request):
#     return render(request, 'firstapp/about/about.html')


# def yangi(request, request2):
#     yangi_data = get_object_or_404(NewsBase, category__name=request2, status=NewsBase.published.all)
#     # category_data = get_object_or_404(Category, name=request2)
#
#     context = {
#         'yangi_data': yangi_data,
#         # 'category_data': category_data,
#     }
#     return render(request, 'global.html', context)


# class Yangi(TemplateView):
#     data = NewsBase.published.all()
#     template_name = 'categorys.html'
