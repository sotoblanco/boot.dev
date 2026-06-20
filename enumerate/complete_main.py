def track_goblin_rooms(hallway):
    goblin_rooms = []
    for index, room in enumerate(hallway):
        if room == "goblin":
            goblin_rooms.append(index)
    return goblin_rooms
