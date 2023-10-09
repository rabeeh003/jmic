from django.shortcuts import render,redirect

# Create your views here.
def batchome(request):
    username = request.session.get('admin')
    user_type = request.session.get('batch')

    if username and user_type == 'batch':
        return render(request,'batchome.html') 
    
    return redirect('batch')