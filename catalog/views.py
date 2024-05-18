from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    TemplateView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from catalog.models import Product


class ProductListView(ListView):
    model = Product


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        print(f"name: {name}, phone: {phone}, message: {message}")

        return render(request, self.template_name)


class ProductDetailsView(DetailView):
    model = Product
