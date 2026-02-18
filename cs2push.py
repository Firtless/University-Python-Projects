import random


Dust2 = ["Mid", "A-site", "B-site", "Short", "Long", "Lower"]

Nuke = ["Ramp", "A-site", "B-ste", "Door", "Outside", "Vent", "Secret", "Roof"]

Inferno = ["Mid", "A-site", "B-ste", "Bannana", "Apps", "Arch"]

Mirrage = ["Mid", "A-site", "B-ste", "Jungle", "Apps", "Lower", "Short"]

cs_maps = [Dust2, Nuke, Inferno, Mirrage]

# map = input("Enter your map: ")


def map_random(cs_maps):
    random_sublist = random.choice(cs_maps)
    random_item = random.choice(random_sublist)

    print(f"random chose: {random_item}")


# def cs_pick(cs_maps):
#     if map == cs_maps:
#         try:
#             current_map = map_random
#         except:

if __name__ == "__main__":
    map_random(cs_maps)
