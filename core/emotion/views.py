from django.shortcuts import render, redirect
from .models import DailyEntry
from collections import Counter, defaultdict

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
            return redirect('/')

    # Últimos registros
    entries = DailyEntry.objects.all().order_by('-created_at', '-id')[:12]

    # Histórico diário por emoção dominante
    daily_summary_grouped = defaultdict(list)
    for entry in DailyEntry.objects.all():
        day = entry.created_at.date()
        daily_summary_grouped[day].append(entry.mood)

    daily_mood_summary = {}
    for date, moods in daily_summary_grouped.items():
        counter = Counter(moods)
        dominant = counter.most_common(1)[0][0]
        daily_mood_summary[date] = dominant

    return render(request, 'emotion/emotion.html', {
        'entries': entries,
        'moods': mood_styles,
        'daily_summary': daily_mood_summary
    })
