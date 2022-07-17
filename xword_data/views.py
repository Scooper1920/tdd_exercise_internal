from django.shortcuts import render

# Create your views here.
def home_view(request):
    
    return render(request, "xword/home_view.html")