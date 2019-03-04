from django.db import models

# The built-in User model already has secure handling for things like
# username, password, email address, and so on.
from django.contrib.auth.models import User


class Categories(models.Model):
    title = models.CharField("Category Title", max_length=50)
    parent_category = models.ForeignKey(
        "Categories", blank=True, null=True, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


class Contributors(models.Model):
    name = models.CharField("Contributor name", max_length=50)
    role = models.ForeignKey("Roles", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Pages(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    contributor = models.ForeignKey("Contributors", on_delete=models.CASCADE)
    tags = models.ManyToManyField("Tags", blank=True)
    category = models.ForeignKey("Categories", on_delete=models.CASCADE)
    title = models.CharField("Title of Page", max_length=50)
    body = models.TextField("Body of the Page", max_length=50)
    is_published = models.BooleanField("Published Online")
    is_flagged = models.BooleanField("Flagged for Review")

    def __str__(self):
        return self.title


class Permissions(models.Model):
    name = models.CharField("Name of Permission", max_length=50)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    body = models.TextField("Body of user profile", max_length=500)
    avatar = models.CharField("Avatar Image URL of user", max_length=500)

    def __str__(self):
        return f"{self.user.username}'s profile"


class Roles(models.Model):
    title = models.CharField("Role Title", max_length=50)
    permissions = models.ManyToManyField("Permissions")

    def __str__(self):
        return self.title


class Tags(models.Model):
    body = models.CharField("The body of the Tag", max_length=500)

    def __str__(self):
        return self.body


# class User(User):
#     name = models.CharField("Username", max_length=50)
#     role = models.ForeignKey(
#         "Roles", related_name="+", on_delete=models.CASCADE
#     )
#     profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
#     pages = models.ManyToManyField("Pages")

#     def __str__(self):
#         return self.name
