from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class Person(User):
#     # user=models.OneToOneField(User,on_delete=models.CASCADE)
#     usern=models.CharField(max_length=50, unique=True)
#     def __str__(self) -> str:
#         return self.username

class Question(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    content=models.TextField(default='question')
    def __str__(self):
        return 'question id ' + str(self.id) + ' Author:'+ str(self.author_id)

class Answer(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    content=models.TextField(default='question')
    def __str__(self):
        return 'answer id ' + str(self.id) + ' Author:'+ str(self.author_id)
