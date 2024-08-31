# needed data:
sorted_names = [
    "Aaron", "Abel", "Abigail", "Addison", "Adrian", "Aiden", "Aaliyah", "Ali", "Allison",
    "Amaya", "Amelia", "Andre", "Annie", "Anthony", "Ariana", "Ari", "Ashley", "Ashton",
    "Aurora", "Austin", "Bella", "Benjamin", "Blake", "Brady", "Brian", "Bryce", "Brooklyn",
    "Bailey", "Cameron", "Camila", "Carl", "Caroline", "Carter", "Cassandra", "Cedric",
    "Chad", "Charles", "Charlotte", "Chloe", "Christian", "Christopher", "Clara", "Collin",
    "Connor", "Cooper", "Dakota", "Daniel", "David", "Diana", "Derek", "Diego", "Dominic",
    "Dylan", "Dora", "Edgar", "Eleanor", "Elena", "Elijah", "Ella", "Ellie", "Eliza",
    "Elizabeth", "Eli", "Elias", "Emma", "Ethan", "Eva", "Evelyn", "Ezra", "Felix", "Fiona",
    "Freddie", "Gabriel", "Gabriella", "Gage", "Giana", "Gianna", "Giselle", "Gordon",
    "Grace", "Gracie", "Hailey", "Hannah", "Harper", "Hazel", "Henry", "Hudson", "Hunter",
    "Ian", "Isaac", "Isabella", "Isaiah", "Jack", "Jackie", "Jacob", "James", "Jasper",
    "Jayden", "Jeremy", "Joan", "Jocelyn", "John", "Joshua", "Josiah", "Julia", "Juno",
    "Kaitlyn", "Karen", "Kasey", "Kayla", "Keira", "Kennedy", "Kendall", "Kieran", "Kylie",
    "Landon", "Laura", "Leah", "Leo", "Levi", "Lila", "Lily", "Lincoln", "Lola", "Logan",
    "Luca", "Lucas", "Lucy", "Luna", "Maddox", "Madeline", "Madison", "Margarita",
    "Mariana", "Martha", "Mason", "Matthew", "Max", "Melanie", "Michael", "Mia", "Micah",
    "Mila", "Molly", "Monica", "Nash", "Natalie", "Nathan", "Nathaniel", "Nina", "Nolan",
    "Nora", "Oliver", "Olivia", "Ophelia", "Oscar", "Paige", "Parker", "Patrick", "Penelope",
    "Peyton", "Quinn", "Riley", "River", "Roman", "Rory", "Rosa", "Ruby", "Sadie", "Samantha",
    "Samuel", "Sarah", "Santiago", "Savannah", "Scarlett", "Sebastian", "Selena", "Serena",
    "Shane", "Sierra", "Skyler", "Sophia", "Sophie", "Stella", "Talia", "Tanner", "Theo",
    "Thomas", "Tristan", "Tyler", "Vera", "Victoria", "Violet", "William", "Willow", "Wyatt",
    "Xander", "Yara", "Zachary", "Zara", "Zane", "Zoe", "Zoey", "Zion"
]

# searching items via binary search
def binary_search_max_steps(names, name):
    low = 0
    high = len(names) - 1
    steps = 0;

    while low <= high:
        mid = (low + high) // 2
        guess = names[mid]
        steps += 1

        if guess == name:
                return steps
        elif guess < name:
            low = mid + 1
        else:
            high = mid - 1

    return steps

print(binary_search_max_steps(sorted_names, "Adrian")) # => 8
print(binary_search_max_steps(sorted_names, "Lily")) # => 8

#	•	Maximum Steps Calculation:
#	•	For a list of size 128, the maximum number of steps is log_2(128) = 7 .
#	•	For a list of size 256, the maximum number of steps is log_2(256) = 8 .