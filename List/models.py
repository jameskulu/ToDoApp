from django.db import models

class Task(models.Model):
  title = models.CharField(max_length=200)
  completed = models.BooleanField(default=False)
  date_created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title

  class Meta:
    ordering = ('-date_created', )