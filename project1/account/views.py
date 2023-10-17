from django.shortcuts import render,redirect
from .models import user_accounts,admin_accounts
from .models import Student,Batch,Teacher


# Create your views here.
def index(request):
    return render(request,'index.html')

def log_in(request):
    if request.POST:
        stid = request.POST['studentid']
        dob = request.POST['dob']
        try:
            user = Student.objects.get(studentid=stid, st_dob=dob)
            request.session['username'] = stid
            request.session['std'] = 'std'
            return redirect('student')
        except:
            error_message = 'Incorrect username or password'
            return render(request,'login.html', {'error_message': error_message})
    
    username = request.session.get('username')
    user_type = request.session.get('std')

    if username and user_type == 'std':
        return redirect('student')
    return render(request,'login.html')

def sign_up(request):
    if request.POST:
        stid = request.POST['studentid']
        name = request.POST['name']
        dob = request.POST['dob']
        batch = Batch.objects.get(batch_no=request.POST['batch'])
        mail = request.POST['mail']
        phone = request.POST['phone']
        data = Student(studentid=stid, st_name=name, st_dob=dob, st_batch=batch, st_mail=mail, st_phone=phone)
        
        try:
            data.save()
        except:
            error_message='Student id or mail alrady existed'
            return render(request,'signup.html',{"error_message":error_message})
        return redirect(log_in)
    
    username = request.session.get('username')
    user_type = request.session.get('std')

    if username and user_type == 'std':
        return redirect('student')
    
    return render(request,'signup.html')

def batch(request):
    if request.POST:
        uname = request.POST['teacherid']
        dob = request.POST['dob']
        try:
            user = Teacher.objects.get(teacherid=uname, t_dob=dob)
            request.session['admin'] = uname
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