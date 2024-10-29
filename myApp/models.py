from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    done = models.BooleanField(default=False)
    #cuando se elimina un dato de la tabla padre, se eliminan los datos de la tabla hija
    project = models.ForeignKey(Project, on_delete = models.CASCADE)

    def __str__(self):
        return self.title + '-' + self.project.name

