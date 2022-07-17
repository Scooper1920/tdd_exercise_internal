from django.contrib import admin
from xword_data.models import User,Puzzle,Clue,Entry


admin.site.register(User)
admin.site.register(Puzzle)
admin.site.register(Clue)
admin.site.register(Entry)
