from django.shortcuts import render, redirect
from .models import Job, Application, CareerTip, AptitudePaper, MockTestSchedule, HRQuestion
from .models import UserProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseNotFound
from django.core.mail import send_mail
from django.views.decorators.http import require_POST
from django.conf import settings



def home1(request):
    keyword = request.GET.get('keyword', '')
    category = request.GET.get('category', '')
    location = request.GET.get('location', '')

    jobs = Job.objects.all()

    if keyword:
        jobs = jobs.filter(title__icontains=keyword)
    if category:
        jobs = jobs.filter(technology__icontains=category)
    if location:
        jobs = jobs.filter(location__icontains=location)

    show_results = bool(request.GET)

    return render(request, 'jobportal/home.html', {
        'jobs': jobs,
        'show_results': show_results
    })





def register(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        username = email

        if User.objects.filter(username=username).exists():
            messages.warning(request, "User with this email already exists.")
            return redirect("register")

        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = fullname
        user.save()

        messages.success(request, "Registration successful! Please log in.")
        return redirect("login")

    return render(request, "jobportal/register.html")

def custom_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next') or 'jobs'
            return redirect(next_url)
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "jobportal/login.html")



def custom_logout(request):
    logout(request)
    return redirect('logout_success')

def logout_success(request):
    return render(request, 'jobportal/logout.html')



@login_required
def profilepage(request):
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == "POST":
        profile.job_type = request.POST.get("job_type", "")
        profile.availability = request.POST.get("availability", "")
        profile.location = request.POST.get("location", "")
        profile.education = request.POST.get("education", "")
        profile.summary = request.POST.get("summary", "")
        profile.skills = request.POST.get("skills", "")
        profile.languages = request.POST.get("languages", "")
        profile.internships = request.POST.get("internships", "")
        profile.accomplishments = request.POST.get("accomplishments", "")

        if 'resume' in request.FILES:
            profile.resume = request.FILES['resume']

        profile.save()
        messages.success(request, "Profile updated successfully!")
        return redirect("home")

    return render(request, "jobportal/profile.html", {"profile": profile})



@login_required(login_url='login')
def applyjob(request, id):
    try:
        job = Job.objects.get(id=id)
    except Job.DoesNotExist:
        messages.error(request, "Job not found.")
        return redirect("jobs")

    if Application.objects.filter(job=job, user=request.user).exists():
        messages.warning(request, "You have already applied for this job.")
        return redirect("jobs")

    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        resume = request.FILES.get("resume")

        if not resume:
            messages.error(request, "Please upload your resume.")
            return render(request, "jobportal/apply_form.html", {"job": job})

        if not resume.name.endswith(('.pdf', '.doc', '.docx')):
            messages.error(request, "Only PDF or DOC files are allowed.")
            return render(request, "jobportal/apply_form.html", {"job": job})

        Application.objects.create(
            user=request.user,
            job=job,
            name=full_name,
            email=email,
            resume=resume
        )
        messages.success(request, "Your application was submitted successfully!")
        return redirect("jobs")

    return render(request, "jobportal/apply_form.html", {"job": job})


def admindashboard(request):
    applications = Application.objects.all().order_by('applied_on')
    return render(request, "jobportal/admin_dashboard.html", {'applications': applications})


@staff_member_required
@require_POST
def update_status(request, app_id):
    from .models import Application

    try:
        application = Application.objects.get(id=app_id)
    except Application.DoesNotExist:
        return HttpResponseNotFound("Application not found.")

    action = request.POST.get('action')
    subject = "Application Update"
    message = ""

    if action == 'approve':
        application.status = 'Approved'
        message = f"Dear {application.user.first_name},\n\nCongratulations! Your job application for '{application.job.title}' has been shortlisted."

    elif action == 'reject':
        application.status = 'Rejected'
        message = f"Dear {application.user.first_name},\n\nWe regret to inform you that your application for '{application.job.title}' has not been shortlisted."

    elif action == 'reset':
        application.status = 'Pending'
        message = f"Dear {application.user.first_name},\n\nYour application for '{application.job.title}' has been reset to Pending for review."

    else:
        messages.error(request, "Invalid action.")
        return redirect('admin_dashboard')

    application.save()

    try:
        send_mail(
            subject,
            message,
            'kartikbhole791@gmail.com',
            [application.user.email],
            fail_silently=False,
        )
        print(f"✅ Email sent to: {application.user.email}")
    except Exception as e:
        print(f"❌ Email sending failed: {e}")

    return redirect('admin_dashboard')


@login_required
def my_applications(request):
    applications = request.user.application_set.all()
    return render(request, "jobportal/my_applications.html", {"applications": applications})


def privacy_policy(request):
    return render(request, 'jobportal/privacy_policy.html')

def faq(request):
    return render(request, 'jobportal/faq.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        subject = f"New Contact Message from {name}"
        full_message = f"Sender: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            messages.error(request, f"Error sending message: {e}")
        return redirect('contact')

    return render(request, 'jobportal/contact.html')

def about(request):
    return render(request, 'jobportal/about.html')

def home2(request):
    return render(request, "jobportal/home2.html")

def home3(request):
    return render(request, "jobportal/home3.html")

def landing(request):
    return render(request, 'jobportal/landing.html')


def jobs(request):
    all_jobs = Job.objects.all().order_by('-posted_on')
    return render(request, "jobportal/jobs.html", {"jobs": all_jobs})


def career_resources(request):
    tips = CareerTip.objects.all()
    papers = AptitudePaper.objects.all()
    tests = MockTestSchedule.objects.all()
    hr_questions = HRQuestion.objects.all()

    return render(request, 'jobportal/career_resources.html', {
        'tips': tips,
        'papers': papers,
        'tests': tests,
        'hr_questions': hr_questions
    })



