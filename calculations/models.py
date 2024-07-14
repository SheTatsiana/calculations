from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=100)
    length = models.FloatField()
    width = models.FloatField()

    def area(self):
        return self.length * self.width

    def __str__(self):
        return self.name

class Building(models.Model):
    name = models.CharField(max_length=100)
    rooms = models.ManyToManyField(Room)

    def total_area(self):
        return sum(room.area() for room in self.rooms.all())

    def __str__(self):
        return self.name
