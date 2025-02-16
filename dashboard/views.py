from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'dashboard/home.html')

@login_required
def accounts(request):
    if request.user.profile.department == 'Accounts' or request.user.is_superuser:
        return render(request, 'dashboard/accounts.html')
    return redirect('home')

@login_required
def hr(request):
    if request.user.profile.department == 'HR' or request.user.is_superuser:
        return render(request, 'dashboard/hr.html')
    return redirect('home')

@login_required
def it(request):
    if request.user.profile.department == 'IT' or request.user.is_superuser:
        return render(request, 'dashboard/it.html')
    return redirect('home')

@login_required
def marketing(request):
    if request.user.profile.department == 'Marketing' or request.user.is_superuser:
        return render(request, 'dashboard/marketing.html')
    return redirect('home')
