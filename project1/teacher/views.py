from django.shortcuts import render,redirect

# Create your views here.
def batchome(request):
    username = request.session.get('username')
    user_type = request.session.get('type')

    if username and user_type == 'batch':
        return render(request,'batchome.html') 
    
    return redirect('batch')