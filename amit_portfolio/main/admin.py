from django.contrib import admin
from .models import Contact, Profile, Skill, Education, Project

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email']
    readonly_fields = ['created_at']
    ordering = ['-created_at']
    
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected messages as read"
    
    actions = [mark_as_read]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'tagline', 'email']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'tagline', 'about', 'profile_image')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'location')
        }),
        ('Social Links', {
            'fields': ('github_url', 'linkedin_url')
        }),
        ('CV', {
            'fields': ('cv_file',)
        }),
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'skill_type', 'proficiency']
    list_filter = ['skill_type']
    search_fields = ['name']
    ordering = ['skill_type', 'name']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'start_date', 'end_date', 'is_current']
    list_filter = ['is_current', 'start_date']
    search_fields = ['degree', 'institution']
    ordering = ['-start_date']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_date', 'is_featured']
    list_filter = ['is_featured', 'start_date']
    search_fields = ['title', 'description']
    ordering = ['-start_date']
    
    fieldsets = (
        ('Project Information', {
            'fields': ('title', 'description', 'image')
        }),
        ('Technical Details', {
            'fields': ('technologies',)
        }),
        ('Links', {
            'fields': ('github_url', 'live_url')
        }),
        ('Timeline', {
            'fields': ('start_date', 'end_date')
        }),
        ('Display Options', {
            'fields': ('is_featured',)
        }),
    )