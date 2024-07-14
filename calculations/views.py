from django.shortcuts import render, get_object_or_404, redirect
from .models import Room, Building
from .forms import RoomForm, BuildingForm

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'calculations/room_list.html', {'rooms': rooms})

def room_detail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    return render(request, 'calculations/room_detail.html', {'room': room})

def room_new(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save()
            return redirect('room_detail', pk=room.pk)
    else:
        form = RoomForm()
    return render(request, 'calculations/room_edit.html', {'form': form})

def building_list(request):
    buildings = Building.objects.all()
    return render(request, 'calculations/building_list.html', {'buildings': buildings})

def building_detail(request, pk):
    building = get_object_or_404(Building, pk=pk)
    return render(request, 'calculations/building_detail.html', {'building': building})

def building_new(request):
    if request.method == "POST":
        form = BuildingForm(request.POST)
        if form.is_valid():
            building = form.save()
            return redirect('building_detail', pk=building.pk)
    else:
        form = BuildingForm()
    return render(request, 'calculations/building_edit.html', {'form': form})
