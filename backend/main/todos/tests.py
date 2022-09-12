from turtle import title
from django.test import TestCase
from .models import Todo
# Create your tests here.


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        Todo.objects.create(
            title='first todo', body='first body')

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        ttl = f'{todo.title}'
        self.assertEqual(ttl, 'first todo')
    
    
    def test_body_content(self):
        todo = Todo.objects.get(id=1)
        bdy = f'{todo.body}'
        self.assertEqual(bdy, 'first body')