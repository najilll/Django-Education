from django.contrib import admin

# Register your models here.
from . models import Graphics_Design
admin.site.register(Graphics_Design)

from . models import Digital_Marketing
admin.site.register(Digital_Marketing)


from . models import Writing_Translation
admin.site.register(Writing_Translation)


from . models import Music_Audio
admin.site.register(Music_Audio)




from . models import Teachers

from . models import SocialAccounts
class SocialAccountsInline(admin.StackedInline):
    model = SocialAccounts
    extra = 1

@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    inlines = [SocialAccountsInline]

admin.site.register(SocialAccounts)


from . models import Contact
admin.site.register(Contact)




from . models import Blog
admin.site.register(Blog)