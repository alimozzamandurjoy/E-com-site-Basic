from re import search
from django.contrib import admin
from .models import Products, Order
# Register your models here.

admin.site.site_header= "Durjoy Shopping"
admin.site.site_title= "Durjoy's E-com"
admin.site.index_title= "Manage Shop"



class ProductAdmin(admin.ModelAdmin):

    def change_discription_to_default(self,request,quryset):
        quryset.update(description="default")
    #change_discription_to_default.short_description= 'Default Des'
    
    list_display= ('title','price','description')
    search_fields= ('title',)
    actions= ('change_discription_to_default',)
    list_editable= ('price',)
admin.site.register(Products,ProductAdmin)
admin.site.register(Order)