from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from account.models import user_accounts,Student,Teacher,Batch

# Create your views here.
def batchome(request):
    username = request.session.get('admin')
    user_type = request.session.get('batch')

    if username and user_type == 'batch':
        try:
            cl = Teacher.objects.get(teacherid=username)
            bt = Batch.objects.get(batch_teacher=cl.id)
            us = Student.objects.filter(st_batch=bt)
            return render(request,'batchome.html',{'us':us})
        except:
            return render(request,'batchome.html')

    
    return redirect('batch')

def batchedit(request, pk):
    username = request.session.get('admin')
    user_type = request.session.get('batch')

    if username and user_type == 'batch':
        us = get_object_or_404(Student, id=pk)
        if request.POST:
            new_name = request.POST.get('name')
            new_email = request.POST.get('email')
            new_password = request.POST.get('password')
            
            c = 0

            if new_name != us.user_name:
                us.user_name = new_name
                c += 1
            if new_email != us.user_mail:
                us.user_mail = new_email
                c += 1
            if new_password != us.user_pass:
                us.user_pass = new_password
                c += 1
            
            if c != 0:
                us.save()
            
            # return redirect(batchome)
        return render(request,'batcheditpage.html',{'us':us}) 
    
    return redirect('batch')

def deleteobj(request, pk):
    us = get_object_or_404(Student, id=pk)
    if request.method == 'POST':
        us.delete()
        return redirect('batchome')
    return redirect('batchome')

def addstu(request):
    if request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        data = user_accounts(user_name=name,user_mail=email, user_pass=password)
        try:
            data.save()
            messages.success(request, 'Your success message goes here.')
        except:
            error_message='Username or mail alrady existed'
            return render(request,'addstudent.html',{"error_message":error_message})
        return render(request,'addstudent.html')
        
    return render(request,'addstudent.html')

    
    
