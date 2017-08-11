from django.contrib import admin
from .models import *

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "date","date_updated"]
    list_display_links = ["title"]
    #list_editable = ["title"]
    list_filter = ["date", "title"]

    search_fields = ["title", "content", "keywords"]
    class Meta:
        model = Blog


admin.site.register(Person)
admin.site.register(Blog, PostModelAdmin)
admin.site.register(PersonalProjects)
admin.site.register(Company)
admin.site.register(CompanyProjects)
admin.site.register(Education)
admin.site.register(TechnicalSkill)
admin.site.register(Skills)
#admin.site.register(Blog)
admin.site.register(TagsforBlog)
admin.site.register(Comment)
admin.site.register(Subscriber)
