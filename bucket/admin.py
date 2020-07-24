from django.contrib import admin
from .models import Bucket

class BucketAdmin(admin.ModelAdmin):
	readonly_fields = ('created',)

admin.site.register(Bucket, BucketAdmin)
