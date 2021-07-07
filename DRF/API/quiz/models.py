from django.db import models

# Create your models here.
class Question(models.Model) :
    ques = models.CharField(max_length=100)
    option1 = models.CharField(max_length=20)
    option2 = models.CharField(max_length=20)
    option3 = models.CharField(max_length=20)
    option4 = models.CharField(max_length=20)
    cans = models.CharField(
        max_length=20,
        # choices=[('option1','Choice 1'),('option2','Choice 2'),('option3','Choice 3'),('option4','Choice 4')],
    )

    def str(self) -> str:
        return self.ques