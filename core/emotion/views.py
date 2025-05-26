# emotion/views.py
from django.shortcuts import render, redirect
from .models import DailyEntry

def emotion_home(request):
    if request.method == 'POST':
        mood = request.POST.get('mood')
        if mood:
            DailyEntry.objects.create(mood=mood)
            return redirect('/')

    entries = DailyEntry.objects.all().order_by('-created_at')
    return render(request, 'emotion/emotion.html', {
        'entries': entries,
        'moods': ['feliz', 'triste', 'ansioso', 'calmo', 'irritado', 'grato']
    })
