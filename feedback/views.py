# homeHub/feedback/views.py

from django.shortcuts import render, redirect
from .forms import FeedbackForm

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()  # Save feedback to the database
            return redirect('feedback_success')  # Redirect to a success page
    else:
        form = FeedbackForm()

    return render(request, 'feedback/feedback.html', {'form': form})

def feedback_success(request):
    return render(request, 'feedback/feedback_success.html')


