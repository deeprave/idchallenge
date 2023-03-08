from django.contrib import admin
from django.apps import apps

for model in apps.get_app_config('api').get_models():
    try:
        class ApiModelAdmin(admin.ModelAdmin):
            list_display = ['id', 'description']

        admin.site.register(model, ApiModelAdmin)
    except admin.sites.AlreadyRegistered:
        pass
