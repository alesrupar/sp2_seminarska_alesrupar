from django.db import models

# Create your models here.
class Events(models.Model):
    reported_by = models.CharField(max_length=255)
    issue_time = models.DateTimeField(auto_now_add=True)
    issue = models.TextField()
    importance = models.CharField(max_length=255)
    status = models.BooleanField(null=True)

    class Meta:
        ordering = ['issue_time']

        def __unicode__(self):
            return self.title

