from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
# Register your models here.
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author', 'publication_year')


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('username', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_staff', 'is_superuser', 'is_active')}
        ),
    )
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Book, BookAdmin)

class Command(BaseCommand):
    help = 'Set up initial user groups and permissions'

    def handle(self, *args, **kwargs):
        # Define groups and their permissions
        groups_permissions = {
            'Editors': ['can_create', 'can_edit'],
            'Viewers': [],
            'Admins': ['can_create', 'can_edit', 'can_delete'],
        }

        for group_name, permissions in groups_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Group "{group_name}" created'))
            else:
                self.stdout.write(self.style.WARNING(f'Group "{group_name}" already exists'))

            for perm_codename in permissions:
                try:
                    permission = Permission.objects.get(codename=perm_codename)
                    group.permissions.add(permission)
                    self.stdout.write(self.style.SUCCESS(f'Permission "{perm_codename}" added to group "{group_name}"'))
                except Permission.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f'Permission "{perm_codename}" does not exist'))

        self.stdout.write(self.style.SUCCESS('Groups and permissions setup complete'))


admin.site.register(Group)
admin.site.register(Permission)
