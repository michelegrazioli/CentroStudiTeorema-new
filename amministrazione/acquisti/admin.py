from django.contrib import admin
from amministrazione.acquisti.models import *

# Register your models here.


admin.site.register(Acquisto)
admin.site.register(PreventivoAcquisto)
admin.site.register(OrdineAcquisto)
admin.site.register(DDTAcquisto)
admin.site.register(FatturaPassiva)