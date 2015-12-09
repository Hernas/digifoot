from django.contrib import admin
from digifoot.api.apps.users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'created_at')
    list_display_links = ('email', 'name',)

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_filter = ('is_superuser',)
    fieldsets = (
        (None, {'fields': ('email',)}),
        ('Personal', {'fields': ('name',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = fieldsets
    search_fields = ('email',)
    ordering = ('email', '-created_at',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)