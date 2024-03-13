from django.contrib import admin
from .models import Country, State

# Register your models here.

class StateInline(admin.TabularInline):
    model = State
    fields = ["name","code"]
    extra = 3

class CountryAdmin(admin.ModelAdmin):
    fields = ["name","code"]
    list_display = ["name","code","id"]
    inlines = [StateInline]

class StateAdmin(admin.ModelAdmin):
    fields = ["name","code", "country"]
    list_display = ["name","code","country"]

admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)