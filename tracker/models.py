from django.db import models
from django.utils import timezone
from django.urls import reverse

class TimestampedBaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(TimestampedBaseModel, self).save(*args, **kwargs)

    def __str__(self):
        str_data = []
        if self.id:
            str_data.append(str(self.id))
        if hasattr(self, "uuid"):
            str_data.append(str(self.uuid))
        if hasattr(self, "name"):
            str_data.append(self.name)
        return " / ".join(str_data)

class Student(TimestampedBaseModel):
    active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return f" {self.first_name} {self.last_name}"

    
    def get_absolute_url(self):
        return reverse('student-detail', kwargs={'pk': self.pk})
 

class Standard(TimestampedBaseModel):
    active = models.BooleanField(default=True)
    statement_name = models.CharField(max_length=100, null=False, blank=False)

    def get_absolute_url(self):
        return reverse('standard-detail', kwargs={'pk': self.pk})
    
    def __str__(self):
        return f" {self.statement_name}"

class Assessment(TimestampedBaseModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
    score = models.IntegerField(null = False)

    def save(self, *args, **kwargs):
        if self.score < 1 or self.score > 4:
            raise ValueError("score must between 1 and 4 inclusive")
        return super(Assessment, self).save(*args, **kwargs)
    

    def get_absolute_url(self):
        return reverse('assessment-detail', kwargs={'pk': self.pk})

