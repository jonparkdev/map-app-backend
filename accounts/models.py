from django.db import models
from django.contrib.auth.models import User

class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, related_name="from_user", on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name="to_user",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['from_user', 'to_user'], name="request-constraint")
        ]

    def __str__(self):
        return f'From {self.from_user.first_name} to {self.to_user.first_name}'


class Friends(models.Model):
    users = models.ManyToManyField(User, related_name='friends_set')
