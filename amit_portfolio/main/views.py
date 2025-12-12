from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, Http404, JsonResponse
from django.conf import settings
from django.views.decorators.http import require_http_methods
from .models import Profile, Skill, Education, Project, Contact
from .forms import ContactForm
import os

def home(request):
    # Get profile data
    try:
        profile = Profile.objects.first()
    except Profile.DoesNotExist:
        profile = None
    
    # Get skills grouped by type
    technical_skills = Skill.objects.filter(skill_type='technical')
    soft_skills = Skill.objects.filter(skill_type='soft')
    tools = Skill.objects.filter(skill_type='tools')
    
    # Get education and projects
    education = Education.objects.all()[:3]  # Latest 3
    projects = Project.objects.filter(is_featured=True)[:6]  # Featured projects
    
    # Contact form
    contact_form = ContactForm()
    
    context = {
        'profile': profile,
        'technical_skills': technical_skills,
        'soft_skills': soft_skills,
        'tools': tools,
        'education': education,
        'projects': projects,
        'contact_form': contact_form,
    }
    
    return render(request, 'main/index.html', context)


@require_http_methods(["GET", "POST"])
def contact(request):
    if request.method == 'POST':
        # Handle AJAX request
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            form = ContactForm(request.POST)
            if form.is_valid():
                contact_instance = form.save()
                return JsonResponse({
                    'success': True,
                    'message': 'Thank you for your message! I\'ll get back to you soon.'
                })
            else:
                return JsonResponse({
                    'success': False,
                    'message': 'Please correct the errors in the form.',
                    'errors': form.errors
                })
        
        # Handle regular form submission
        else:
            form = ContactForm(request.POST)
            if form.is_valid():
                contact_instance = form.save()
                messages.success(request, 'Thank you for your message! I\'ll get back to you soon.')
                return redirect('main:home')
            else:
                messages.error(request, 'Please correct the errors below.')
                return redirect('main:home')
    
    return redirect('main:home')


def download_cv(request):
    try:
        profile = Profile.objects.first()
        if profile and profile.cv_file:
            file_path = profile.cv_file.path
            if os.path.exists(file_path):
                with open(file_path, 'rb') as fh:
                    response = HttpResponse(fh.read(), content_type="application/pdf")
                    response['Content-Disposition'] = f'inline; filename="{profile.name}_CV.pdf"'
                    return response
        raise Http404("CV not found")
    except Profile.DoesNotExist:
        raise Http404("Profile not found")