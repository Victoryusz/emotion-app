# emotion/views.py
from django.shortcuts import render, redirect
from .models import DailyEntry

def emotion_home(request):
    mood_styles = {
        'feliz':     {'emoji': '😄', 'btn': 'success'},
        'triste':    {'emoji': '😢', 'btn': 'danger'},
        'ansioso':   {'emoji': '😰', 'btn': 'warning'},
        'calmo':     {'emoji': '😌', 'btn': 'info'},
        'irritado':  {'emoji': '😠', 'btn': 'secondary'},
        'grato':     {'emoji': '🙏', 'btn': 'primary'},
    }

    if request.method == 'POST':
        mood = request.POST.get('mood')
        if mood:
            DailyEntry.objects.create(mood=mood)
            return redirect('/')  # Isso força um reload com GET atualizado

    # 🔁 ESSENCIAL: traz os últimos 12 atualizados em ordem decrescente
    entries = DailyEntry.objects.all().order_by('-created_at', '-id')[:12]

    return render(request, 'emotion/emotion.html', {
        'entries': entries,
        'moods': mood_styles,
    })



