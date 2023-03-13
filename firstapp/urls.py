from django.urls import path

# with function
from firstapp.views import HomePage, ContactPage, detail_page, page_404, \
    Global, Update, Delete, Create, search, ftest

from django.contrib.auth.views import LoginView, LogoutView

# with class
# from firstapp.views import Home

urlpatterns = [
    path('te/', ftest, name='test'),
    path('create/', Create.as_view(), name='create'),
    path('contact/', ContactPage.as_view(), name='contact'),
    path('error-404/', page_404, name='page_404'),
    path('search/', search, name='search'),
    path('<slug>/edit/', Update.as_view(), name='update'),
    path('<slug>/delete/', Delete.as_view(), name='delete'),
    path('<str:request2>/', Global.as_view(), name='all_category'),
    path('<str:category_name>/<str:news>/', detail_page, name='detail_page'),

    path('', HomePage.as_view(), name='home'),

]
