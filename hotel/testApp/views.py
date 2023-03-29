from django.http import HttpResponse, JsonResponse
from .models import Building, RoomType, Room, BlockedDay


# Create your views here.

def available(request):
    check_in = request.GET['check_in']
    check_out = request.GET['check_out']
    building = request.GET['building']
    filter_days = BlockedDay.objects.filter(day__lte=check_out, day__gte=check_in).values("room_id")
    h=[]
    if not filter_days:
        building_names = Building.objects.filter(name=building).values()
        for build in building_names:
            room_types = RoomType.objects.filter(building=build.get('id')).values("id", "name", "type")
            if room_types:
                for room in room_types:
                    room_type_data = helper(room)
                    h.append(room_type_data)

        return JsonResponse(h, safe=False)
    else:
        return HttpResponse("These days are blocked")


def helper(room_type):
    rooms = Room.objects.filter(room_type=room_type.get('id')).values().order_by("price")
    room_date = []
    for room in rooms:
        room.pop("room_type_id")
        room.pop("id")
        room.update(room_type)
        room_date.append(room)
    return room_date

