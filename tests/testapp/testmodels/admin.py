from django.contrib import admin

from .models import Address, Allergy, Hobby, Occupation, Pet, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass


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
