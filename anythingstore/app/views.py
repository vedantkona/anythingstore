from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.csrf import csrf_exempt
from .models import TextFile, AudioFile, VideoFile
from django.http import JsonResponse
import os


def home(request):
    logged_in = request.user.is_authenticated
    return render(request, "Home/home.html", {"logged_in":logged_in})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        user = authenticate(request, username = username, password = pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("username or password is incorrect")
        
    return render(request, "authentication/login.html")

def register(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pas1 = request.POST.get('password1') 
        pas2 = request.POST.get('password2')
        if pas1 != pas2 or User.objects.filter(username=uname).exists():
            return HttpResponse("Your password and conform password is not same please retry.")
        else:
            my_user = User.objects.create_user(uname,email,pas1)
            my_user.save()
            return redirect('login')
    return render(request, "authentication/register.html")

def user_logout(request):
    logout(request)
    return redirect('home')
    
@login_required(login_url='login')
@csrf_exempt
def textnote(request):
    if request.method == 'POST':
        file = request.FILES.get('text_file')
        if file:
            filename, file_extension = os.path.splitext(file.name)
            if file_extension.lower() not in ['.txt', '.pdf', '.doc','.docx']:
                return JsonResponse({'status': 'error', 'message': 'Invalid file format. Only txt, pdf, doc, docx files are allowed.'})
            text_file = TextFile(user=request.user, file=file)
            text_file.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'No file received'})
    logged_in = request.user.is_authenticated
    return render(request, "Home/textnote.html", {"logged_in":logged_in})

@login_required(login_url='login')
@csrf_exempt
def audionote(request):
    if request.method == 'POST':
        file = request.FILES.get('audio_file')
        if file:
            filename, file_extension = os.path.splitext(file.name)
            if file_extension.lower() not in ['.m4a', '.flac', '.mp3','.wav']:
                return JsonResponse({'status': 'error', 'message': 'Invalid file format. Only m4a, flac, mp3, wav files are allowed.'})
            audio_file = AudioFile(user=request.user, file=file)
            audio_file.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'No file received'})
    logged_in = request.user.is_authenticated
    return render(request, "Home/audionote.html", {"logged_in":logged_in})

@login_required(login_url='login')
@csrf_exempt
def videotnote(request):
    if request.method == 'POST':
        file = request.FILES.get('video_file')
        if file:
            filename, file_extension = os.path.splitext(file.name)
            if file_extension.lower() not in ['.mp4', '.mp3']:
                return JsonResponse({'status': 'error', 'message': 'Invalid file format. Only MP4 and MP3 files are allowed.'})
            video_file = VideoFile(user=request.user, file=file)
            video_file.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'No file received'})
    logged_in = request.user.is_authenticated
    return render(request, "Home/videonote.html", {"logged_in":logged_in})

@login_required(login_url='login')
def user_Profile(request):
    text_files = TextFile.objects.filter(user = request.user)
    video_files = VideoFile.objects.filter(user = request.user)
    audio_files = AudioFile.objects.filter(user = request.user)
    logged_in = request.user.is_authenticated
    return render(request, "Home/profile.html", {"text_files": text_files, "logged_in":logged_in, "video_files":video_files, "audio_files": audio_files})