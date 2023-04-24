from django.contrib import admin
from .forms import UserCreationForm
from .models import User,Profile


@admin.register(User)
class AccountAdmin(admin.ModelAdmin):
	form = UserCreationForm
    
	list_display = ["username",
					"email",
                    "first_name",
                    "last_name",
                    "date_joined",
                    ]
	list_filter = ['date_joined',
                   'first_name',
                   'last_name',
                   ]
	fieldsets = (
        (None, {'fields': ('email',
						   'username',
                           'password',
						   'phone_number',
                           'user_permissions',
                           'groups',
                           'first_name',
                           'last_name',)}),
        ('Permissions', {'fields': ('is_admin',
                                    'is_active',
                                    'is_superuser',)}),
    )
	search_fields = ['first_name',
                     'last_name',
                     "email",
                     ]
	ordering = ('email',)
	add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password'),
        }),
    )



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	class Meta:
		model = Profile
