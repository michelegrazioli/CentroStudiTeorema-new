from django.contrib import admin
from amministrazione.vendite.models import RecordVendita, RecordDDTVendita, RecordFatturaAttiva, RecordOrdineVendita, RecordPreventivoVendita, Vendita, OrdineVendita, PreventivoVendita, DDTVendita, FatturaAttiva

# Register your models here.

class RecordVenditaInline(admin.TabularInline):
    model = RecordVendita
    extra = 5

class RecordPreventivoVenditaInline(admin.TabularInline):
    model = RecordPreventivoVendita
    extra = 5

class RecordOrdineVenditaInline(admin.TabularInline):
    model = RecordOrdineVendita
    extra = 5

class RecordDDTVenditaInline(admin.TabularInline):
    model = RecordDDTVendita
    extra = 5

class RecordFatturaAttivaInline(admin.TabularInline):
    model = RecordFatturaAttiva
    extra = 5

class VenditaAdmin(admin.ModelAdmin):
    inlines = [RecordVenditaInline]

class PreventivoVenditaAdmin(admin.ModelAdmin):
    inlines = [RecordPreventivoVenditaInline]

class OrdineVenditaAdmin(admin.ModelAdmin):
    inlines = [RecordOrdineVenditaInline]

class DDTVenditaAdmin(admin.ModelAdmin):
    inlines = [RecordDDTVenditaInline]

class FatturaAttivaAdmin(admin.ModelAdmin):
    inlines = [RecordFatturaAttivaInline]


admin.site.register(Vendita, VenditaAdmin)
admin.site.register(PreventivoVendita, PreventivoVenditaAdmin)
admin.site.register(OrdineVendita, OrdineVenditaAdmin)
admin.site.register(DDTVendita, DDTVenditaAdmin)
admin.site.register(FatturaAttiva, FatturaAttivaAdmin)
