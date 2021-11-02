from django.contrib import admin

from .models import User, Pet, Allergy, Occupation, Address, Hobby

class HobbyInline(admin.TabularInline):
    model = Hobby
    extra = 1

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [HobbyInline]

class UserInline(admin.TabularInline):
    model = User
    extra = 1

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    inlines = [UserInline]


@admin.register(Allergy)
class AllergyAdmin(admin.ModelAdmin):
    pass

@admin.register(Occupation)
class OccupationAdmin(admin.ModelAdmin):
    inlines = [UserInline]


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    inlines = [UserInline]

@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    pass