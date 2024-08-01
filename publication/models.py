from django.db import models
from author.models import Author

# Create your models here.
class Publication(models.Model):
    date_pub = models.DateTimeField(
        'publication date',
        auto_now_add=True
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE
    )
    pub_text = models.TextField(
        'publications',
        max_length=255
    )
    pub_title = models.CharField(
        'publication title',
        max_length=100
    )

    class Meta:
        db_table = 'publications'