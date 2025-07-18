from django.db.models import Q
from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    PermissionRequiredMixin
)
from django.views.generic import ListView, DetailView 
from .models import Book

# Create your views here.
class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = "book_list" 
    template_name = "books/book_list.html"
    login_url = "account_login"

class BookDetailView(
    LoginRequiredMixin, 
    PermissionRequiredMixin,
    DetailView):
    model = Book
    context_object_name = "book"
    template_name = "books/book_detail.html"
    login_url = "account_login"
    permission_required = "books.special_status"
    queryset = Book.objects.all().prefetch_related('reviews__author',)

class SearchResultsListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/book_list.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Book.objects.filter(
            Q(title__icontains="beginner") | Q(title__icontains="api")
        )
