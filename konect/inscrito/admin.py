from django.contrib import admin
from .models import *

@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    pass
