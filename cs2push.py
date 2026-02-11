import random


Dust2 = ["Mid", "A-site", "B-site", "Short", "Long", "Lower"]

Nuke = ["Ramp", "A-site", "B-ste", "Door", "Outside", "Vent", "Secret", "Roof"]

Inferno = ["Mid", "A-site", "B-ste", "Bannana", "Apps", "Arch"]

Mirrage = ["Mid", "A-site", "B-ste", "Jungle", "Apps", "Lower", "Short"]

cs_maps = [Dust2, Nuke, Inferno, Mirrage]

map = input("Enter your map: ")

for i in cs_maps:
    if map == int(cs_maps[i]):
        j = random.randint(1, len(map))
    else:
        print("Enter correctly")
    i += 1

if __name__ == "__main__":
    print(map[j])
