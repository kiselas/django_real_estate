from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'full_price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor', 'city', 'state', )
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'state')
    list_per_page = 25
admin.site.register(Listing, ListingAdmin)
