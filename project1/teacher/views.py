from django.shortcuts import render,redirect
# from django.views.generic import TemplateView, ListView, DeleteView
from account.models import user_accounts

# Create your views here.
def batchome(request):
    username = request.session.get('admin')
    user_type = request.session.get('batch')

    if username and user_type == 'batch':
        us = user_accounts.objects.all() 
        return render(request,'batchome.html',{'us':us}) 
    
    return redirect('batch')

# def search(request):
#     if request.method == 'POST':
#         search_term = request.POST.get('search')
#         if search_term:
#             # Use Q objects for complex queries
#             results = user_accounts.objects.filter(
#                 Q(user_name__icontains=search_term)
#             )
#             return render(request, 'batchome.html', {'us': results})
#     return redirect(batchome)

# class std(TemplateView):
#     context_object_name = 'stdetail'
#     template_name = "batchedit.html"
#     model = user_accounts
    
    
