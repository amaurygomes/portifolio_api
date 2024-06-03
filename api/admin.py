from django.contrib import admin
from .models import PageInfo, Technology, Social, KnowTechs




@admin.register(PageInfo)
class PageInfoAdmin(admin.ModelAdmin):

    list_display = ('name',)

    filter_horizontal = ('technologies', 'socials')
    fieldsets = (
        (None, {
            'fields': ('name', 'introduction', 'profilePicture')
        }),
        ('Associations', {
            'fields': ('technologies', 'socials')
        }),
    )

    def has_add_permission(self, request):
        
        if PageInfo.objects.exists():
            return False
        return True

    def changelist_view(self, request, extra_context=None):
        
        if PageInfo.objects.exists():
            instance = PageInfo.objects.first()
            return self.change_view(request, object_id=str(instance.id))
        return super(PageInfoAdmin, self).changelist_view(request, extra_context)

    def has_delete_permission(self, request, obj=None):
       
        return False

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'startDate')

@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')

@admin.register(KnowTechs)
class KnowTechsAdmin(admin.ModelAdmin):
    filter_horizontal = ('techs',)

    def has_add_permission(self, request):
        
        if KnowTechs.objects.exists():
            return False
        return True

    def changelist_view(self, request, extra_context=None):
        
        if KnowTechs.objects.exists():
            instance = KnowTechs.objects.first()
            return self.change_view(request, object_id=str(instance.id))
        return super(KnowTechsAdmin, self).changelist_view(request, extra_context)

    def has_delete_permission(self, request, obj=None):
        
        return False
    
    
