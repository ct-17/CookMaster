from django.conf.urls import url
from django.views.generic import FormView
from .forms import PostModelForm
from .views import (
    post_model_create_view,
    post_model_detail_view,
    post_model_delete_view,
    post_model_list_view,
    post_model_update_view,
    home,
    food_list,
    list_food_all,
    )

urlpatterns = [
    url(r'^$', post_model_list_view, name='list'),
    url(r'^home/$', home, name='home'),
    url(r'^food_list/$', food_list, name='food_list'),
    url(r'^list_all_food/$', list_food_all, name='list_food_all'),
    #url(r'^create/$', FormView.as_view(template_name="blog/post.html",form_class= PostModelForm), name='create'),
    url(r'^create/$', post_model_create_view, name='create'),
    url(r'^(?P<id>\d+)/$', post_model_detail_view, name='detail'),
    url(r'^(?P<id>\d+)/delete/$', post_model_delete_view, name='delete'),
    url(r'^(?P<id>\d+)/edit/$', post_model_update_view, name='update'),
]
