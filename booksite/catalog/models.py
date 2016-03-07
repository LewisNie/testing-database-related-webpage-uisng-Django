from django.db import models

class Publisher(models.Model):
    pub_id=models.IntegerField(primary_key=True,unique=True)
    pub_name = models.CharField(max_length=50,unique=True)
    city = models.CharField(max_length=50)
    def __unicode__(self):
	return u'%s' %(self.pub_name)

class Title(models.Model):
    title_id=models.CharField(primary_key=True,max_length=20)
    title = models.CharField(max_length=100)
    category=models.CharField(max_length=20)
    price = models.FloatField(null=True, blank=True)
    pub_id=models.ForeignKey("Publisher")
    def __unicode__(self):
	return u'%s' %(self.title)
#from catalog.models import Publisher,Title

