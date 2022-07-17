from django.shortcuts import render
from .models import Puzzle, Entry, Clue
# from django.contrib.auth.decorators import  login_required

# Create your views here.

# @login_required - commented out due to redirect error after login "database not connected to utc"
#google advised likely due to psycopg-binary version
def drill_view(request):
    clue = Clue.objects.all()
    
    return render(request, "xword/drill_view.html")

# - **Drill view:** presents a random clue with information about the entry (length and puzzle
#   where it appeared) to the user, and includes an input field where the user can provide a guess
#   at the answer. Input of an incorrect guess should re-display the same clue with a note the answer
#   is not correct. Input of a correct answer should redirect to the answer view for that clue.
#   The drill view's rendered page should offer the user an "escape hatch" to see the answer even
#   if they cannot correctly guess it.


def answer_view(request):
    pass 

