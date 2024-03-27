from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth import authenticate, login, logout
from .models import Team

def index(request):
    if request.user.is_authenticated:
        teams = Team.objects.all()
        return render(request, 'index.html', {'teams': teams})
    else:
        return redirect('signin')



@login_required
def quiz2(request):
    if request.user.team.quiz_1_status == True:
        return render(request, 'quiz2.html')
    else:
        return redirect(quiz1)

def custom_404_page(request, exception):
    return render(request, '404.html', status=404)

@login_required
def quiz1(request):
    if request.method == 'POST':
        # Retrieve the submitted code from the form
        submitted_code = request.POST.get('code')

        # Check if the submitted code matches the specified value (2504)
        if submitted_code == '2504':
            # Update the quiz_1_status to True
            if hasattr(request.user, 'team'):  # Check if the user has an associated team
                team = request.user.team  # Access the associated team
                if team.quiz_1_status == False:
                    team.score += 100 
                team.quiz_1_status = True
                team.save() 
                return redirect('quiz2')

    # Render the quiz1 page if no POST request or incorrect code submitted
    return render(request, 'quiz1.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('signin')
    return render(request, 'signin.html')

def signout(request):
    logout(request)
    return redirect('index')