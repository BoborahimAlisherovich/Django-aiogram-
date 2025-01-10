from django.contrib import admin

# Register your models here.

from .models import BotUser,Feedback




@admin.register(BotUser)
class RezidentAdmin(admin.ModelAdmin):
    list_display = ('name', 'user_id', 'username','create_at','id')
    search_fields = ('name',)  



@admin.register(Feedback)
class RezidentAdmin(admin.ModelAdmin):
    list_display = ( 'body','user_id', 'create_at','id')
    search_fields = ('body',)  
   
   