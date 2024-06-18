from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    TemplateView,
    DetailView,
    CreateView,
    UpdateView,
)

from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product, Version, Category
from catalog.services import get_cached_categories


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        print(f"name: {name}, phone: {phone}, message: {message}")

        return render(request, self.template_name)


class ProductListView(ListView):
    model = Product
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = context["products"]
        context["categories"] = Category.objects.all()

        for product in products:
            current_version = product.versions.filter(is_current=True).first()
            if current_version:
                product.current_version = {
                    "version_number": current_version.version_number,
                    "version_name": current_version.version_name,
                }
            else:
                product.current_version = None

        return context


class ProductDetailsView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFromset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == "POST":
            context_data["formset"] = VersionFromset(
                self.request.POST, instance=self.object
            )
        else:
            context_data["formset"] = VersionFromset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = super().get_context_data()
        formset = context_data["formset"]
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return super().render_to_response(
                self.get_context_data(form=form, formset=formset)
            )
        product = form.save()
        user = self.request.user
        product.user = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_details")

    def get_success_url(self):
        return reverse("catalog:product_details", args=[self.kwargs.get("pk")])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFromset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == "POST":
            context_data["formset"] = VersionFromset(
                self.request.POST, instance=self.object
            )
        else:
            context_data["formset"] = VersionFromset(instance=self.object)
        return context_data

    def get_form_class(self):
        user = self.request.user
        if user == self.object.user:
            return ProductForm
        elif (
            user.has_perm("product.can_cancel_publish_product")
            and user.has_perm("product.can_change_description_product")
            and user.has_perm("product.can_change_category_product")
        ):
            return ProductModeratorForm
        else:
            raise PermissionDenied

    def form_valid(self, form):
        context_data = super().get_context_data()
        formset = context_data["formset"]
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return super().render_to_response(
                self.get_context_data(form=form, formset=formset)
            )


class ProductByCategoryView(ListView):
    model = Product
    template_name = "catalog/products_by_category.html"
    context_object_name = "products_by_category"

    def get_queryset(self):
        category_id = self.kwargs.get("category_id")
        return Product.objects.filter(category_id=category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.get(id=self.kwargs.get("category_id"))
        context["categories"] = Category.objects.all()
        return context


class CategoryListView(ListView):
    model = Category
    context_object_name = "categories"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()

        return context

    def get_queryset(self):
        return get_cached_categories()
