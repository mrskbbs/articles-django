import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    url = models.CharField(max_length = 8) # TODO: Not so sure about length 
    
    # IMPORTANT: 
    # URL encoding
    # 32 base number
    # hashlib.sha256("date + name + author_id".encode("utf-8"))
    
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    html = models.CharField(max_length = 5000)
    published = models.DateField(auto_now = False, auto_now_add = True)

    def __str__(self) -> str:
        return f"Author: {self.author.get_full_name()}\nTitle: {self.title}\nURL: {self.url}\n"

    def authorName(self) -> str:
        return self.author.get_full_name()
    
    def authorUsername(self) -> str:
        return self.author.username