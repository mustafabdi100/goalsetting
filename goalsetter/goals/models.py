from django.db import models

class Goal(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Consequence(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"Consequence for {self.goal.title}"

class Progress(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    progress = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Progress for {self.goal.title}"