from django.db import models

class Todo(models.Model):
    title       = models.CharField(max_length=255, unique=True)
    due_date    = models.DateField()
    completed   = models.BooleanField()
    favorite    = models.BooleanField()
    liste       = models.ForeignKey('TodoList', null=False, related_name='liste', on_delete=models.CASCADE)

    def __str__(self):
        return f'Titre : {self.title}'
    
    class Meta:
        db_table = 'todo'
        verbose_name = 'Todo'
        verbose_name_plural = 'Todo'

class TodoList(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'Nom : {self.name}'
    
    class Meta:
        db_table = 'todo_list'
        verbose_name = 'Todo Liste'
        verbose_name_plural = 'Todo Listes'
