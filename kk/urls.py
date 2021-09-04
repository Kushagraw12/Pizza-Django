"""kk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from webapp.views import (
    api_all_pizza_view,
    api_indiv_pizza_view,
    api_update_pizza_view,
    api_delete_pizza_view,
    api_create_pizza_view,
    api_size_filter_pizza_view,
    api_type_filter_pizza_view
)

app_name = "pizza"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pizzas/', api_all_pizza_view, name = "details"),
    path('pizza/<slug>', api_indiv_pizza_view, name = "detail"),
    path('pizza/update/<slug>', api_update_pizza_view, name = "update"),
    path('pizza/delete/<slug>', api_delete_pizza_view, name = "delete"),
    path('createPizza', api_create_pizza_view, name = "create"),
    path('pizza/all_size/<size>', api_size_filter_pizza_view, name = "sizeFilter"),
    path('pizza/all_type/<type>', api_type_filter_pizza_view, name = "typeFilter"),
]
