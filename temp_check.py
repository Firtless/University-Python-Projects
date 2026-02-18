def temp_check(temp):

    if len(temp) <= 2:
        return "Not enough data"

    is_up = True
    is_down = True

    for i in range(len(temp) - 1):
        if temp[i] > temp[i + 1]:
            is_up = False
        elif temp[i] < temp[i + 1]:
            is_down = False

    if is_up and is_down:
        return "Temp is stable"
    elif is_up:
        return "Temp going up"
    elif is_down:
        return "Temp is going down"
    else:
        return "Temp Undstable"


if __name__ == '__main__':

    user_input = input("Enter temps(20 22 21): ")

    try:
        temp_data = [float(x) for x in user_input.split()]
        result = temp_check(temp_data)
        print(f"Analysis result: {result}")

    except ValueError:
        print("Error: No SPACE!!!")
