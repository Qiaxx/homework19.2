from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView

from catalog.models import Product, Blog


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


class BlogListView(ListView):
    model = Blog


class BlogDetailsView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'slug', 'content', 'preview', 'published', 'views_count')
    success_url = reverse_lazy('catalog:post_list')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.slug = slugify(new_post.title)
            new_post.save()
            return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'slug', 'content', 'preview', 'published', 'views_count')
    success_url = reverse_lazy('catalog:post_list')

    def get_success_url(self):
        return reverse('catalog:post_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
