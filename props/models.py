from django.db import models
from django.contrib.auth.models import User
from categories.models import Category
from datetime import datetime
import pytz

class ActivePropsManager(models.Manager):
    def get_query_set(self):
        return super(ActivePropsManager, self).get_query_set() # .filter(STATUS_PENDING)

class Prop(models.Model):
    # Prop - name, category, description, photo gallery, foreign key to owner, status, suggested donation
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, editable=False)
    owner = models.ForeignKey(User)
    categories = models.ManyToManyField(Category, null=False)
    description = models.TextField()
    image = models.ImageField(null=True, upload_to='props/%Y/%m/%d')
    date_created = models.DateTimeField(editable=False, default=datetime.now(pytz.utc))
    date_modified = models.DateTimeField(editable=False, default=datetime.now(pytz.utc))
    STATUS_PENDING = 0;
    STATUS_AVAILABLE = 1;
    STATUS_IN_USE = 2;
    STATUS_DISABLED = 3;
    STATUS_DELETED = 4;
    STATUS_CODES = (
                    (STATUS_PENDING, 'Pending'),
                    (STATUS_AVAILABLE, 'Available'),
                    (STATUS_IN_USE, 'In Use'),
                    (STATUS_DISABLED, 'Disabled'),
                    (STATUS_DELETED, 'Deleted')
                    )
    status = models.IntegerField(choices=STATUS_CODES, default=STATUS_PENDING)

    objects = models.Manager()
    active = ActivePropsManager()
    
    def get_absolute_url(self):
      from django.core.urlresolvers import reverse
      return reverse('prop_detail', kwargs={'owner':self.owner,'slug': self.slug})
    
    def __unicode__(self):
      return self.name
    
    def save(self, *args, **kwargs):
      from django.template.defaultfilters import slugify
      
      self.date_modified = datetime.now(pytz.utc)
      self.slug = slugify(self.name)
      super(Prop, self).save(args, kwargs)