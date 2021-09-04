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
    # Admin Controls, visit localhost:8000/admin to login
    path('admin/', admin.site.urls),

    # List all Pizzas in the db
    path('pizzas/', api_all_pizza_view, name = "details"),

    # List individual Pizzas as per slug
    path('pizza/<slug>', api_indiv_pizza_view, name = "detail"),

    # Update an individual Pizza as per the slug
    path('pizza/update/<slug>', api_update_pizza_view, name = "update"),

    # Delete an individual Pizza as per the slug
    path('pizza/delete/<slug>', api_delete_pizza_view, name = "delete"),

    # Create a Pizza
    path('createPizza', api_create_pizza_view, name = "create"),

    # List all Pizzas with a specific Size
    path('pizza/all_size/<size>', api_size_filter_pizza_view, name = "sizeFilter"),

    # List all Pizzas with a specific Type
    path('pizza/all_type/<type>', api_type_filter_pizza_view, name = "typeFilter"),
]
