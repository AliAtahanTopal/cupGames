from django.contrib import admin
from .models import Account
from .models import Category
from .models import Game
from .models import Score
from .models import Comment
from .models import Statistic
from .models import Badge
from .models import Suggestion


# Register your models here.
admin.site.register(Account)
admin.site.register(Category)
admin.site.register(Game)
admin.site.register(Score)
admin.site.register(Comment)
admin.site.register(Statistic)
admin.site.register(Badge)
admin.site.register(Suggestion)