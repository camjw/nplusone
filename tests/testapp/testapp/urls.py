from django.conf.urls import re_path
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r"^one_to_one/$", views.one_to_one),
    re_path(r"^one_to_one_first/$", views.one_to_one_first),
    re_path(r"^one_to_many/$", views.one_to_many),
    re_path(r"^many_to_many/$", views.many_to_many),
    re_path(r"^many_to_many_get/$", views.many_to_many_get),
    re_path(r"^prefetch_one_to_one/$", views.prefetch_one_to_one),
    re_path(r"^prefetch_one_to_one_unused/$", views.prefetch_one_to_one_unused),
    re_path(r"^prefetch_many_to_many/$", views.prefetch_many_to_many),
    re_path(r"^many_to_many_impossible/$", views.many_to_many_impossible),
    re_path(r"^many_to_many_impossible_one/$", views.many_to_many_impossible_one),
    re_path(r"^prefetch_many_to_many_render/$", views.prefetch_many_to_many_render),
    re_path(r"^prefetch_many_to_many_unused/$", views.prefetch_many_to_many_unused),
    re_path(r"^prefetch_many_to_many_single/$", views.prefetch_many_to_many_single),
    re_path(r"^prefetch_many_to_many_no_related/$", views.prefetch_many_to_many_no_related),
    re_path(r"^select_one_to_one/$", views.select_one_to_one),
    re_path(r"^select_one_to_one_unused/$", views.select_one_to_one_unused),
    re_path(r"^select_many_to_one/$", views.select_many_to_one),
    re_path(r"^select_many_to_one_unused/$", views.select_many_to_one_unused),
    re_path(r"^prefetch_nested/$", views.prefetch_nested),
    re_path(r"^prefetch_nested_unused/$", views.prefetch_nested_unused),
    re_path(r"^select_nested/$", views.select_nested),
    re_path(r"^select_nested_unused/$", views.select_nested_unused),
]
