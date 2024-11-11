class Classroom:
    # Static list containing names of classrooms in the left wing
    classroom_list = ["A101", "A102", "A103", "B201", "B202", "C301"]

    @staticmethod
    def search_classroom(class_room):
        # Perform case-insensitive search
        if class_room.upper() in (room.upper() for room in Classroom.classroom_list):
            return "Found"
        else:
            return -1


# Test the method
class_room_to_search = input("Enter the name of the classroom to search: ")

# Call the static method and display the result
result = Classroom.search_classroom(class_room_to_search)
if result == "Found":
    print("Classroom {} is in the left wing.".format(class_room_to_search))
else:
    print("Classroom {} is not found in the left wing.".format(class_room_to_search))
