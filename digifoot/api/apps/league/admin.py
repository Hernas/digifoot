from django.contrib import admin
from digifoot.api.apps.league.models import PlayerModel, MatchModel, GoalModel


admin.site.register(GoalModel)
admin.site.register(MatchModel)
admin.site.register(PlayerModel)