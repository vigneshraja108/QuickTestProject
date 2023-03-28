from django.db import models


# Create your models here.
class Building(models.Model):
    name = models.CharField(max_length=100)


class RoomType(models.Model):
    ROOM_TYPE = [
        ('Single', 'Single'),
        ('Double', 'Double')
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=ROOM_TYPE)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)


class Room(models.Model):
    number = models.PositiveSmallIntegerField()
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    price = models.FloatField()


class BlockedDay(models.Model):
    day = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
