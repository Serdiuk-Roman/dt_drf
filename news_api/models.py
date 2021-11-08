from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=128, unique=True, blank=False)
    link = models.URLField(max_length=128, unique=True, blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    amount_of_upvotes = models.PositiveSmallIntegerField(default=0)
    author_name = models.CharField(max_length=64, blank=False)

    class Meta:
        ordering = ["amount_of_upvotes", "creation_date"]

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    author_name = models.CharField(max_length=64, blank=False)
    content = models.TextField(blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", related_name="comments", on_delete=models.CASCADE)

    class Meta:
        ordering = ["creation_date"]
