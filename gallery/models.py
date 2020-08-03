from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def update_category(self, update):
        self.name = update
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod 
    def get_category_id(cls, id):
        category = Category.objects.get(pk = id)
        return category

class Image(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to = 'uploads/')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image_location = models.ForeignKey('Location', on_delete=models.CASCADE)

    def save_image(self):
        self.save()

    @classmethod
    def update_image(self):
        self.update()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls, id, title, description, image_location, category):
        update = cls.objects.filter(id = id).update(title = title, description = description, image_location = location, category = category)

    @classmethod
    def search_by_category(cls,category):
        images = Image.objects.filter(category__name__icontains=category)
        return images

    @classmethod
    def filter_by_location(cls, image_location):
        images_location = cls.objects.filter(image_location_id=image_location)
        return images_location

    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images


class Location(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def update_location(self, update):
        self.name = update
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def get_location_id(cls, id):
        locate = Location.objects.get(pk = id)
        return locate
