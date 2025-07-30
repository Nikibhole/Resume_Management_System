from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('technical', 'Technical Skill'),
        ('soft', 'Soft Skill'),
        ('language', 'Language'),
        ('other', 'Other'),
    ]
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Job(models.Model):
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = HTMLField()
    technology = models.CharField(max_length=100, default="python")
    skills = models.ManyToManyField('Skill')
    location = models.CharField(max_length=100)
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Application(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    applied_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return self.name if self.name else "No Name"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job_type = models.CharField(max_length=100, blank=True)
    availability = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    education = models.TextField(blank=True)
    summary = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    languages = models.TextField(blank=True)
    internships = models.TextField(blank=True)
    accomplishments = models.TextField(blank=True)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    image = models.ImageField(upload_to='profile_pics/', default='default.jpg')

    def __str__(self):
        return self.user.username


class CareerTip(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    icon = models.CharField(max_length=50, blank=True)  # FontAwesome icon class
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class AptitudePaper(models.Model):
    title = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='aptitude_papers/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class MockTestSchedule(models.Model):
    topic = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    duration = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.topic} on {self.date}"


class HRQuestion(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question
