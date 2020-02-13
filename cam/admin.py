from django.contrib import admin
from .models import Camera, Emplacement, EmplacementCamera, Reparation, Site, Fournisseur


class CameraEmp(admin.StackedInline):
    model = EmplacementCamera
    extra = 0
    ordering = ('camera',)  


class CameraAdmin(admin.ModelAdmin):
    list_display = ('nom', ) #'date_installaion', 'reference',)
    list_filter = ('emplacements',)
    ordering = ('nom',)
    search_fields = ('nom', 'reference')
    inlines = [CameraEmp,]


class ReparationAdmin(admin.ModelAdmin):
    list_display = ('camera', 'date_reparation', 'frais', 'descriptif',)
    ordering = ('camera',)
    search_fields = ('camera',)


class EmplacementAdmin(admin.ModelAdmin):
    model = Emplacement
    inlines = [CameraEmp,]
    search_fields = ('nom',)
    list_display = ('nom', 'site',)
    list_filter = ('site',)
   

class SiteAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    ordering = ('nom',)
    search_fields = ('nom',) 


class FournisseurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'société', 'date_livraison',)
    search_fields = ('nom', 'prenom', 'societé')


admin.site.register(Site, SiteAdmin)
admin.site.register(Emplacement, EmplacementAdmin)
admin.site.register(Camera, CameraAdmin)
admin.site.register(Reparation, ReparationAdmin)
admin.site.register(Fournisseur, FournisseurAdmin)
