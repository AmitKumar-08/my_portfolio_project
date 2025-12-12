from django.db import models
from django.core.validators import RegexValidator

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"{self.name} - {self.email}"


class Profile(models.Model):
    name = models.CharField(max_length=100, default="Amit")
    tagline = models.CharField(max_length=200, default="Full Stack Developer")
    about = models.TextField()
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    cv_file = models.FileField(upload_to='cv/', blank=True, null=True)
    
    # Social Links
    github_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.name


class Skill(models.Model):
    SKILL_TYPES = [
        ('technical', 'Technical'),
        ('soft', 'Soft Skills'),
        ('tools', 'Tools & Technologies'),
    ]
    
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(default=80, help_text="Proficiency level (0-100)")
    skill_type = models.CharField(max_length=20, choices=SKILL_TYPES, default='technical')
    icon = models.CharField(max_length=50, blank=True, help_text="CSS icon class")
    
    def __str__(self):
        return self.name


class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    location = models.CharField(max_length=100, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    grade = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    is_current = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.degree} - {self.institution}"


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    technologies = models.CharField(max_length=300, help_text="Comma-separated list")
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-start_date']
    
    def __str__(self):
        return self.title
    
    def get_technologies_list(self):
        return [tech.strip() for tech in self.technologies.split(',') if tech.strip()]