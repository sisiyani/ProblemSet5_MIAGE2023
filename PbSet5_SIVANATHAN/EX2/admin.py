from django.contrib import admin
from .models import *

class QuotesAdmin(admin.ModelAdmin):
    # the tuple on the right contains the columns we want to have displayed in the admin site
    list_display = ('id', 'content', 'author')

# Register your models here.
admin.site.register(Person)
admin.site.register(Quotes,QuotesAdmin)