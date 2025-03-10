from admin_auto_filters.filters import AutocompleteFilter
from django.contrib import admin

from .models import Address, Allergy, Hobby, Occupation, Pet, User


class PetInline(admin.TabularInline):
    model = Pet
    extra = 1


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [PetInline]
    search_fields = ("name",)


class UserFilter(AutocompleteFilter):
    title = "User"
    field_name = "user"


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    model = Pet
    autocomplete_fields = ["user"]
    list_display = ["get_user_name"]
    list_filter = [UserFilter]

    @admin.display(description="User")
    def get_user_name(self, obj):
        return obj.user.name

    get_user_name.admin_order_field = "user"


@admin.register(Allergy)
class AllergyAdmin(admin.ModelAdmin):
    pass


@admin.register(Occupation)
class OccupationAdmin(admin.ModelAdmin):
    pass


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    pass
