from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    exclude = ['user']
    search_fields = ['name', 'phonenumber', 'email']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(Contact, ContactAdmin)
