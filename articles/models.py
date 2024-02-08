from django.db import models
from django.contrib.auth.models import User

class Article:
    url = models.CharField(max_length = 8) # TODO: Not so sure about length 
    
    # IMPORTANT: 
    # URL encoding
    # 32 base number
    # hashlib.sha256("date + name + author_id".encode("utf-8"))
    
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    html = models.CharField()

    def __str__(self) -> str:
        return f"Author: {self.author.initials()}\nTitle: {self.title}\nURL: {self.url}\n"