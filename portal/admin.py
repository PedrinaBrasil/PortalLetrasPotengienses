from django.contrib import admin
from .models import *
from .forms import *
# Register your models here.
# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "publised_date",  "created", "updated")
    exclude = []
    form = BookForm

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "gender", "created", "updated")
    exclude = []
    form = AuthorForm