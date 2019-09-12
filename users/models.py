from django.db import models

class User(models.Model):
	name = models.CharField(max_length=100, unique=True, null=False)
	username = models.CharField(max_length=100, null=False)

	def follows(self):
		follows = Follows.objects.filter(owner=self.id)
		return follows

	def followers(self):
		followers = Follows.objects.filter(following=self.id)
		return followers

	def __str__(self):
		return "{} - {}".format(self.name, self.username)
		
class Follows(models.Model):
	owner = models.ForeignKey(User, related_name="owner", on_delete = models.CASCADE, null=True)
	following = models.ForeignKey(User, related_name="following", on_delete = models.CASCADE, null=True)

	@classmethod
	def follow(cls, owner, following):
		follows, created = cls.objects.get_or_create(owner = owner, following = following)
		return created

	@classmethod
	def unfollow(cls, owner, following):
		follows = cls.objects.filter(owner = owner, following = following).first()
		return follows != None and follows.delete()[0] > 0

	def __str__(self):
		return "{} -> {}".format(self.owner.name, self.following.name)