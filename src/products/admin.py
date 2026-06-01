from django.contrib import admin

from .forms import TagForm
from .models import Category, Comment, Product, Tag


# Register the Category model with the admin site
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created_at")
    prepopulated_fields = {"slug": ("name",)}


# Register the Product model with the admin site
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "average_rating", "rating_count", "created_at")
    list_select_related = ("category",)
    form = TagForm


# Register the Comment model with the admin site
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("product", "user", "guest_name", "rating", "created_at")
    list_filter = ("rating", "created_at")
    search_fields = ("guest_name", "guest_email", "text", "user__username")


# Register the Tag model with the admin site
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at", "description")
    list_filter = ("name", "created_at")
    search_fields = ("name", "created_at")