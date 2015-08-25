from django.contrib import admin
from tournament import models

@admin.register(models.Competition)
class CompetitionAdmin(admin.ModelAdmin):
    pass

@admin.register(models.GauntletRound)
class GauntletRoundAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Block)
class BlockAdmin(admin.ModelAdmin):
    pass

