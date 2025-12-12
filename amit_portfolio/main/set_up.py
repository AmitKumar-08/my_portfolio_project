# Run this file with: python manage.py shell < main/setup_data.py

from main.models import Profile, Skill, Education, Project
from datetime import datetime

# Create or update profile
profile, created = Profile.objects.get_or_create(
    id=1,
    defaults={
        'name': 'Amit',
        'tagline': 'Full Stack Developer',
        'about': 'Passionate about creating amazing web experiences with clean code and modern technologies.',
        'email': 'amit@example.com',
        'phone': '+91-1234567890',
        'location': 'India',
        'github_url': 'https://github.com/amit',
        'linkedin_url': 'https://linkedin.com/in/amit',
    }
)

if created:
    print("✓ Profile created successfully!")
else:
    print("✓ Profile already exists!")

# Create skills
skills_data = [
    {'name': 'Django', 'proficiency': 85, 'skill_type': 'technical', 'icon': 'fab fa-python'},
    {'name': 'SQL', 'proficiency': 80, 'skill_type': 'technical', 'icon': 'fas fa-database'},
    {'name': 'Core Java', 'proficiency': 95, 'skill_type': 'technical', 'icon': 'fab fa-java'},
    {'name': 'JDBC', 'proficiency': 90, 'skill_type': 'technical', 'icon': 'fas fa-plug'},
    {'name': 'JavaScript', 'proficiency': 75, 'skill_type': 'technical', 'icon': 'fab fa-js-square'},
    {'name': 'HTML5', 'proficiency': 90, 'skill_type': 'technical', 'icon': 'fab fa-html5'},
    {'name': 'CSS3', 'proficiency': 85, 'skill_type': 'technical', 'icon': 'fab fa-css3-alt'},
    {'name': 'Git', 'proficiency': 80, 'skill_type': 'tools', 'icon': 'fab fa-git-alt'},
]

for skill_data in skills_data:
    skill, created = Skill.objects.get_or_create(
        name=skill_data['name'],
        defaults=skill_data
    )
    if created:
        print(f"✓ Skill '{skill.name}' created!")

# Create education records
education_data = [
    {
        'degree': 'Bachelor of Technology (B.Tech)',
        'institution': 'Your College Name',
        'location': 'Your City',
        'start_date': '2023-07-01',
        'end_date': None,
        'grade': '9.0 CGPA',
        'description': 'Currently pursuing Bachelor of Technology in Computer Science.',
        'is_current': True
    },
    {
        'degree': 'Higher Secondary (12th)',
        'institution': 'Your School Name',
        'location': 'Your City',
        'start_date': '2021-04-01',
        'end_date': '2023-03-31',
        'grade': '78%',
        'description': 'Completed Higher Secondary education with Science stream.',
        'is_current': False
    },
    {
        'degree': 'Secondary School (10th)',
        'institution': 'Your School Name',
        'location': 'Your City',
        'start_date': '2019-04-01',
        'end_date': '2021-03-31',
        'grade': '88%',
        'description': 'Completed Secondary education with excellent performance.',
        'is_current': False
    }
]

for edu_data in education_data:
    start_date = datetime.strptime(edu_data['start_date'], '%Y-%m-%d').date()
    end_date = None
    if edu_data['end_date']:
        end_date = datetime.strptime(edu_data['end_date'], '%Y-%m-%d').date()
    
    education, created = Education.objects.get_or_create(
        degree=edu_data['degree'],
        institution=edu_data['institution'],
        defaults={
            'location': edu_data['location'],
            'start_date': start_date,
            'end_date': end_date,
            'grade': edu_data['grade'],
            'description': edu_data['description'],
            'is_current': edu_data['is_current']
        }
    )
    if created:
        print(f"✓ Education '{education.degree}' created!")

# Create projects
projects_data = [
    {
        'title': 'Weather Forecasting App',
        'description': 'A sleek and functional interface for real-time weather updates and forecasts.',
        'technologies': 'Django, Python, JavaScript, REST API',
        'github_url': 'https://github.com/amit/weather-app',
        'live_url': 'https://weather-app-demo.com',
        'start_date': '2024-01-01',
        'is_featured': True
    },
    {
        'title': 'ChronoView App',
        'description': 'A time-based data visualization or scheduling tool—clean, modern, and intuitive.',
        'technologies': 'Django, JavaScript, HTML5, CSS3',
        'github_url': 'https://github.com/amit/chronoview-app',
        'live_url': 'https://chronoview-app-demo.com',
        'start_date': '2024-02-01',
        'is_featured': True
    },
    {
        'title': 'Portfolio Website',
        'description': 'A personal showcase of skills and projects, designed with style and clarity.',
        'technologies': 'Django, Bootstrap, JavaScript, CSS3',
        'github_url': 'https://github.com/amit/portfolio',
        'live_url': 'https://amit-portfolio.com',
        'start_date': '2024-03-01',
        'is_featured': True
    },
    {
        'title': 'JDBC CRUD Operations',
        'description': 'A backend-focused application demonstrating Create, Read, Update, and Delete operations.',
        'technologies': 'Java, JDBC, SQL',
        'github_url': 'https://github.com/amit/jdbc-crud',
        'live_url': None,
        'start_date': '2023-12-01',
        'is_featured': True
    }
]

for project_data in projects_data:
    start_date = datetime.strptime(project_data['start_date'], '%Y-%m-%d').date()
    
    project, created = Project.objects.get_or_create(
        title=project_data['title'],
        defaults={
            'description': project_data['description'],
            'technologies': project_data['technologies'],
            'github_url': project_data['github_url'],
            'live_url': project_data['live_url'],
            'start_date': start_date,
            'is_featured': project_data['is_featured']
        }
    )
    if created:
        print(f"✓ Project '{project.title}' created!")

print("\n" + "="*50)
print("✓ Setup completed successfully!")
print("="*50)
print("\nNext steps:")
print("1. Create a superuser: python manage.py createsuperuser")
print("2. Upload CV and profile image in Django admin")
print("3. Access admin at: http://127.0.0.1:8000/admin/")
print("4. Update the profile with your own details")