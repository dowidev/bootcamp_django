from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category

    def __repr__(self):
        return self.category


class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    summary = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to="blogs/featured_images")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title
