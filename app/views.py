from django.http import JsonResponse
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
def quiz1(request):
    if request.method == 'POST':
        submitted_code = request.POST.get('code')
        if submitted_code == '2504':
            if hasattr(request.user, 'team'):  # Check if the user has an associated team
                team = request.user.team
                if team.quiz_1_status == False:
                    team.score += 100 
                team.quiz_1_status = True
                team.save() 

    return render(request, 'quiz1.html')



def quiz2(request):
    if request.user.is_authenticated and request.user.team.quiz_1_status == True:
        if request.method == 'POST':
            submitted_code = request.POST.get('geneL')
            if submitted_code == '12q23.2':
                if hasattr(request.user, 'team'):
                    team = request.user.team
                    if team.quiz_2_status == False:
                        team.score += 100 
                    team.quiz_2_status = True
                    team.save() 

        return render(request, 'quiz2.html')
  
    return redirect(quiz1)



@login_required
def quiz3(request):
    if request.user.is_authenticated and request.user.team.quiz_2_status == True:
        if request.method == 'POST':
            submitted_code = request.POST.get('UnlockKey')
            if submitted_code == '439':
                if hasattr(request.user, 'team'):
                    team = request.user.team
                    if team.quiz_3_status == False:
                        team.score += 100
                    team.quiz_3_status = True
                    team.save()

        return render(request, 'quiz3.html')
    
    return redirect(quiz2)

@login_required
def quiz4(request):
    if request.method == 'POST':
        submitted_code = request.POST.get('UnlockKey')
        if submitted_code == '6666':
            if hasattr(request.user, 'team'):
                team = request.user.team
                if team.quiz_4_status == False:
                    team.score += 100
                team.quiz_4_status = True
                team.save()
                return redirect(index)
    team = request.user.team
    team.score -= 1
    team.save()
    return render(request, 'quiz4.html')

@login_required
def quiz5(request):
    if request.method == 'POST':
        submitted_code = request.POST.get('UnlockKey').lower()
        if submitted_code == 'crispr':
            if hasattr(request.user, 'team'):
                team = request.user.team
                if team.quiz_5_status == False:
                    team.score += 100
                team.quiz_5_status = True
                team.save()
                return redirect(index)
    return render(request, 'quiz5.html')


def update_score(request):
    team = request.user.team
    team.score -= 10
    team.save()
    # Your logic to update the user's score goes here
    # For example, you can access the user's score from request.user.team.score
    
    # Return a JSON response indicating success or failure
    return JsonResponse({'status': 'success'})









def custom_404_page(request, exception):
    return render(request, '404.html', status=404)


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'signin.html', {'error_message': 'Invalid username or password!'})

    return render(request, 'signin.html')

def signout(request):
    logout(request)
    return redirect('index')