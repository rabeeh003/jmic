from django.shortcuts import render,redirect
from .models import user_accounts,admin_accounts
# Create your views here.

def index(request):
    return render(request,'index.html')

def log_in(request):
    if request.POST:
        uname = request.POST['username']
        upass = request.POST['password']
        try:
            user = user_accounts.objects.get(user_name=uname, user_pass=upass)
            request.session['username'] = uname
            request.session['std'] = 'std'
            return redirect('student')
        except user_accounts.DoesNotExist:
            error_message = 'Incorrect username or password'
            return render(request,'login.html', {'error_message': error_message})
    
    username = request.session.get('username')
    user_type = request.session.get('std')

    if username and user_type == 'std':
        return redirect('student')
    
    
    return render(request,'login.html')

def sign_up(request):
    if request.POST:
        uname = request.POST['username']
        umail = request.POST['mail']
        upass = request.POST['password']
        data = user_accounts(user_name=uname,user_mail=umail, user_pass=upass)

        try:
            data.save()
        except:
            error_message='Username or mail alrady existed'
            return render(request,'signup.html',{"error_message":error_message})
        return redirect(log_in)
    
    username = request.session.get('username')
    user_type = request.session.get('std')

    if username and user_type == 'std':
        return redirect('student')
    
    return render(request,'signup.html')

def batch(request):
    if request.POST:
        uname = request.POST['username']
        upass = request.POST['password']
        try:
            user = admin_accounts.objects.get(admin_name=uname, admin_pass=upass)
            request.session['admin'] = 'admin'
            request.session['batch'] = 'batch'
            return redirect("batchome")
        except:
            error_message = 'Incorrect username or password'
            return render(request,'batch.html', {'error_message': error_message})
        
    username = request.session.get('admin')
    user_type = request.session.get('batch')

    if username and user_type == 'batch':
        return redirect("batchome") 
    
    return render(request,'batch.html')


def log_out(request):
    if 'username' or 'admin' in request.session:
        request.session.flush()
    return redirect(index)