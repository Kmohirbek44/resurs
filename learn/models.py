from django.db import models


class Subject(models.Model):
    name          = models.CharField(max_length = 20)

    def __str__(self):
        return self.name


class Exam(models.Model):
    name           = models.CharField(max_length=20)
    subject        = models.ForeignKey(Subject,on_delete=models.CASCADE)
    score          = models.IntegerField(default=0)
    
    class Meta:
        order_with_respect_to = 'name'

    def __str__(self):
        return self.name


class Question(models.Model):
    exam            = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question_text   = models.TextField(max_length = 255, null = False)

    class Meta:
        order_with_respect_to = 'exam'

    def __str__(self):
        return "%s" % (self.question_text)


class Choice(models.Model):
    question        = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text     = models.CharField(max_length = 255, null = False)
    is_correct      = models.BooleanField(blank=True)
    
    class Meta:
        order_with_respect_to = 'question'

    def __str__(self):
        return self.choice_text

