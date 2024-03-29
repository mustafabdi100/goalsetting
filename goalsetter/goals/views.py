from django.shortcuts import render, redirect, get_object_or_404
from .models import Goal, Consequence, Progress
from django.http import JsonResponse

def home(request):
    return render(request, 'home.html')

def goal_list(request):
    goals = Goal.objects.all()
    return render(request, 'goal_list.html', {'goals': goals})

def goal_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        deadline = request.POST['deadline']
        consequence = request.POST['consequence']
        goal = Goal.objects.create(title=title, description=description, deadline=deadline)
        Consequence.objects.create(goal=goal, description=consequence)
        return redirect('goal_list')
    return render(request, 'goal_create.html')

def goal_detail(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id)
    consequences = Consequence.objects.filter(goal=goal)
    progress = Progress.objects.filter(goal=goal).order_by('-updated_at').first()
    return render(request, 'goal_detail.html', {'goal': goal, 'consequences': consequences, 'progress': progress})

def goal_detail_json(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id)
    consequences = Consequence.objects.filter(goal=goal)
    progress = Progress.objects.filter(goal=goal).order_by('-updated_at').first()

    data = {
        'title': goal.title,
        'description': goal.description,
        'deadline': goal.deadline.strftime('%Y-%m-%d'),
        'consequence': consequences.first().description if consequences.exists() else '',
        'progress': progress.progress if progress else 0
    }

    return JsonResponse(data)

def goal_update(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id)
    if request.method == 'POST':
        goal.title = request.POST['title']
        goal.description = request.POST['description']
        goal.deadline = request.POST['deadline']
        goal.save()
        consequence = Consequence.objects.filter(goal=goal).first()
        consequence.description = request.POST['consequence']
        consequence.save()
        return redirect('goal_detail', goal_id=goal.id)
    return render(request, 'goal_update.html', {'goal': goal})

def goal_delete(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id)
    if request.method == 'POST':
        goal.delete()
        return redirect('goal_list')
    return render(request, 'goal_delete.html', {'goal': goal})