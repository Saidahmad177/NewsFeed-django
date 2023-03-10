from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from users.models import Profile
from firstapp.models import NewsBase, Category, AllUser
from firstapp.forms import FormContact, CommentsForm

from django.views.generic import ListView, TemplateView, DeleteView, UpdateView, CreateView
from news.custom_permisson import OnlyLoggedSuperUser, PermissionUser


# This is  Home Page View
class HomePage(LoginRequiredMixin, ListView):
    model = NewsBase
    template_name = 'firstapp/first.html'
    context_object_name = 'newsbase'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['all_element'] = NewsBase.published.all()
        context['local_news'] = NewsBase.published.filter(category__name='local').order_by('-publish_time')[:5]
        context['newsbase'] = NewsBase.published.all().order_by('-publish_time')[:5]
        context['global_news'] = NewsBase.published.filter(category__name='global').order_by('-publish_time')[:5]
        context['technology'] = NewsBase.published.filter(category__name='technology').order_by('-publish_time')[:5]
        context['sport'] = NewsBase.published.filter(category__name='sport').order_by('-publish_time')[:5]
        context['user'] = self.request.user

        return context


# This is all Category View
class Global(TemplateView):
    template_name = 'firstapp/categorys.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_name = kwargs['request2']
        category = get_object_or_404(Category, name=category_name)
        context['category'] = category

        context['all_category_data'] = NewsBase.published.filter(category__name=category_name).order_by('-publish_time')

        return context


# class Global(ListView):
#     category_model = NewsBase
#     template_name = 'firstapp/update.html'
#     context_object_name = 'global_news'
#
#     def get_queryset(self):
#         data = self.category_model.published.all().filter(category__name='Global')
#         return data


# This is Create function View
class Create(PermissionUser, CreateView):
    create_data = NewsBase
    template_name = 'CRUD/create.html'
    fields = ('title', 'slug', 'body', 'image', 'category', 'status')
    success_url = 'home'

    def get_queryset(self):
        return self.create_data.published.all()


# This is Update_function View
class Update(UpdateView):
    update_data = NewsBase
    template_name = 'CRUD/update.html'
    fields = ('title', 'body', 'image', 'category', 'status',)
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return self.update_data.published.all()


# This is Delete function View
class Delete(DeleteView):
    delete_data = NewsBase
    template_name = 'CRUD/delete.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return self.delete_data.published.all()


# This is Contact page View
class ContactPage(View):
    template_name = 'firstapp/contact.html'

    def get(self, request, *args, **kwargs):
        form = FormContact()
        context = {
            'form': form
        }
        return render(request, 'firstapp/contact.html', context)

    def post(self, request, *args, **kwargs):
        form = FormContact(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return render(request, 'firstapp/contact.html', {'contact_send': True})

            else:
                return render(request, 'firstapp/contact.html', {'error_message': True})


# This is 404 page View
def page_404(request):
    return render(request, '404.html')


# This is detail page View


def detail_page(request, news, category_name):

    data = get_object_or_404(NewsBase, slug=news, category__name=category_name, status=NewsBase.Status.published)
    comments = data.comments.filter(active=True)
    comment_count = comments.count()

    if request.method == 'POST':
        comment_form = CommentsForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.news = data
            new_comment.user = request.user
            new_comment.save()

    else:
        comment_form = CommentsForm()

    context = {
        'data': data,
        'comments': comments,
        'comment_form': comment_form,
        'comment_count': comment_count,

    }
    print(data.category)
    return render(request, 'firstapp/detail_page.html', context)

# it's with make function view
# def detail_page(request, news, category_name):
#     user = request.user
#     if request.method == 'GET':
#         data = get_object_or_404(NewsBase, slug=news, category__name=category_name, status=NewsBase.Status.published)
#         context = {
#             'data': data,
#             'user': user,
#         }
#         print(data.category)
#         return render(request, 'firstapp/detail_page.html', context)
