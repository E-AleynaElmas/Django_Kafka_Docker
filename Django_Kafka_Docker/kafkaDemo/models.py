from django.db import models

# Create your models here.

#Şarkı ismi, izlenme sayısı ve beğeni sayısı olan basit bir model
class KafkaDemo(models.Model):

    id =models.IntegerField(primary_key=True)
    artist=models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    views = models.IntegerField()
    likes = models.IntegerField()

    class Meta:
        verbose_name_plural = "events"
    
    def __str__(self):
        return self.artist