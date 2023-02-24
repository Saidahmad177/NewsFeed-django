from django.urls import path

# with function
from firstapp.views import HomePage, ContactPage, detail_page, page_404, Global
# with class
# from firstapp.views import Home

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('contact/', ContactPage.as_view(), name='contact'),
    path('error-404/', page_404, name='page_404'),

    path('<str:request2>/', Global.as_view(), name='all_category'),
    path('<str:category_name>/<slug:news>/', detail_page, name='detail_page'),


]
