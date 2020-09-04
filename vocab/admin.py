from django.contrib import admin

# Register your models here.
from .models import Word, Definition, Example

admin.site.register(Word)
admin.site.register(Definition)
admin.site.register(Example)