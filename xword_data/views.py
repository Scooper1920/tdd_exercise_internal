from django.shortcuts import render
# from django.contrib.auth.decorators import  login_required

# Create your views here.

# @login_required - commented out due to redirect error after login "database not connected to utc"
#google advised likely due to psycopg-binary version
def drill_view(request):
    
    return render(request, "xword/drill_view.html")