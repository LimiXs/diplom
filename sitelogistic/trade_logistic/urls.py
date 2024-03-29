from django.urls import path, re_path, register_converter, include

from . import views
from . import converters
from .views import *

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    # path('', views.index, name='home'),
    path('', TradeLogisticHome.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('get-exel/', views.get_excel, name='get_excel'),
    path('add-page/', AddPage.as_view(), name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('upload-file/', views.upload_file, name='upload_file'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', TradeLogisticCategory.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', views.show_tag_postlist, name='tag'),
    # path('doc-info/', views.get_doc_info, name='doc_info'),
    path('doc-info/', DocsListView.as_view(), name='doc_info'),
    path('download/<str:path_doc>/', views.download, name='download'),
    path('erip-info/', views.erip_info, name='erip_info'),
    path('happy-birthdays/', views.show_happy_birthdays, name='happy_birthdays')
]
