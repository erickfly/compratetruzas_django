from django.contrib import admin
from .models import Genre, Movie

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id','name','film_style')


class MovieAdmin(admin.ModelAdmin):
    exclude = ('date_created', )
    list_display = ('id','title','stock','daily_rate')
    

admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)