from django.contrib import admin
from main.models import *


# Register your models here.
class WelcomeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Welcome, WelcomeAdmin)


class AboutUsAdmin(admin.ModelAdmin):
    pass


admin.site.register(AboutUs, AboutUsAdmin)


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)


class ContactAdmin(admin.ModelAdmin):
    pass


admin.site.register(Contact, ContactAdmin)


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)


class FeedbackAdmin(admin.ModelAdmin):
    pass


admin.site.register(Feedback, FeedbackAdmin)


class ReserveAdmin(admin.ModelAdmin):
    pass


admin.site.register(Reserve, ReserveAdmin)