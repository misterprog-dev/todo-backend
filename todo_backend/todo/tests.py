from django.test import TestCase
from datetime import datetime
from .models import Todo, TodoList


class TodoTestCase(TestCase):
    def setUp(self):
        self.todo_list = TodoList()
        self.todo_list.name = 'Job'
        self.todo_list.save()

        # On crée notre todo
        self.todo = Todo()
        self.todo.title = 'Nouveau'
        self.todo.due_date = datetime.now()
        self.todo.completed = True
        self.todo.favorite = True
        self.todo.liste = self.todo_list

        self.todo.save()

    def test_create_todo(self):
        # GIVEN
        nbre_of_todo_before_add = Todo.objects.count()

        # WHEN
        Todo.objects.create(title='Titre 1', due_date=datetime.now(
        ), completed=True, favorite=True, liste=self.todo_list)
        Todo.objects.create(title='Titre 2', due_date=datetime.now(
        ), completed=True, favorite=True, liste=self.todo_list)

        # THEN
        nbre_of_todo_after_add = Todo.objects.count()
        self.assertEqual(nbre_of_todo_before_add + 2, nbre_of_todo_after_add)

    def test_update_todo(self):
        # WHEN
        self.todo.title = 'Changed'
        self.todo.save()

        # THEN
        self.assertEqual(self.todo.title, 'Changed')


    def test_delete_todo(self):
        # GIVEN
        nbre_todo_before_deleted = Todo.objects.count()

        # WHEN
        self.todo.delete()

        # THEN
        nbre_todo_after_deleted = Todo.objects.count()
        self.assertTrue(nbre_todo_before_deleted - 1 == nbre_todo_after_deleted)
