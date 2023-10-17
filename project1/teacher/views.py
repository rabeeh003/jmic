from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from account.models import Student,Teacher,Batch,Sem,Mark
from .form import addmark_form
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
        batch = Batch.objects.all()
        
        if request.POST:
            new_name = request.POST.get('name')
            new_dob = request.POST.get('dob')
            new_batch = request.POST.get('batch')
            new_mail = request.POST.get('email')
            new_phone = request.POST.get('phone')
            
            c = 0

            if new_name != us.st_name:
                us.st_name = new_name
                c += 1
            if new_mail != us.st_mail:
                us.st_mail = new_mail
                c += 1
            if new_dob != '':
                us.st_dob = new_dob
                c += 1
            if new_batch != us.st_batch:
                bat = Batch.objects.get(batch_no=new_batch)
                us.st_batch = bat
                c += 1
            if new_phone != us.st_phone:
                us.st_phone = new_phone
                c += 1

            if c != 0:
                us.save()
    
            return redirect(batchome)
        return render(request,'batcheditpage.html',{'us':us,'batch':batch}) 
    
    return redirect('batch')

def deleteobj(request, pk):
    us = get_object_or_404(Student, id=pk)
    if request.method == 'POST':
        us.delete()
        return redirect('batchome')
    return redirect('batchome')

def addstu(request):
    username = request.session.get('admin')
    user_type = request.session.get('batch')

    if username and user_type == 'batch':
        te = Teacher.objects.get(teacherid=username)
        batchn = Batch.objects.get(batch_teacher=te)
        if request.POST:
            stid = request.POST.get('studentid')
            name = request.POST.get('name')
            dob = request.POST.get('dob')
            mail = request.POST.get('email')
            phone = request.POST.get('phone')
            data = Student(studentid=stid, st_name=name, st_dob=dob, st_batch=batchn, st_mail=mail, st_phone=phone)
            try:
                data.save()
                messages.success(request, 'Your success message goes here.')
            except:
                error_message='Username or mail alrady existed'
                return render(request,'addstudent.html',{"error_message":error_message})
            return render(request,'addstudent.html')
        return render(request,'addstudent.html',{"batch":batchn})    
    return redirect("batch")

def marck(request):
    username = request.session.get('admin')
    user_type = request.session.get('batch')

    if username and user_type == 'batch':
        te = Teacher.objects.get(teacherid=username)
        batchn = Batch.objects.get(batch_teacher=te)
        sem = Sem.objects.all()
        ma = Mark.objects.all()
        # subj = [semester.sub1,semester.sub2,semester.sub3,semester.sub4, semester.sub5, semester.sub6, semester.sub7]
        subj = {
            'sem1':[],
            'sem2':[],
            'sem3':[],
            'sem4':[],
        }
        mar = {
            'sem1':[],
            'sem2':[],
            'sem2':[],
            'sem2':[],
        }
        data = []
        for sem_name, subjects in subj.items():
            sem_data = {
                "sem_name": sem_name,
                "subjects": subjects,
                "marks": mar.get(sem_name, []),
            }
            data.append(sem_data)
        
        for i, s in enumerate(sem):
            for n in range(s.count_of_sub):
                field_name = f'sub{n + 1}'  # Construct the field name as a string
                subject_name = getattr(s, field_name)  # Use getattr to access the field by name
                
                subj[f'sem{s.sem}'].append(subject_name)
        for i, s in enumerate(ma):
            for n in range(s.count_subject):
                field_name = f's{n + 1}'  # Construct the field name as a string
                mrcck = getattr(s, field_name)  # Use getattr to access the field by name
                mar[f'sem{s.sem_no}'].append(mrcck)

        return render(request,'marck.html',{"batch":batchn,'sem':sem,'subj':subj,'mar':mar,'data': data})    
    return redirect("batch")

def addmarck(request):
    username = request.session.get('admin')
    user_type = request.session.get('batch')

    if username and user_type == 'batch':
        te = Teacher.objects.get(teacherid=username)
        batchn = Batch.objects.get(batch_teacher=te)
        stud = Student.objects.filter(st_batch=batchn)
        sem = Sem.objects.all()
        form = addmark_form()        
        return render(request,'marckadd.html',{'std':stud, 'sem':sem, 'form':form})
    return redirect("batch")

