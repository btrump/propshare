from django.db import models

class Category(models.Model):
    """
    Categories for the site
    """
    SLUG_MAX_LENGTH = 100
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, editable=False, max_length=SLUG_MAX_LENGTH)
    description = models.TextField(blank=True, default='')
    image = models.ImageField(blank=True, null=True, upload_to='categories')
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __unicode__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        from django.template.defaultfilters import slugify

        # generate slug from title, and truncate it to max length
        self.slug = slugify(self.title)[:self.SLUG_MAX_LENGTH]
        super(Category, self).save(args, kwargs)
    
    def get_absolute_url(self):
        return '/categories/%s' % self.slug
