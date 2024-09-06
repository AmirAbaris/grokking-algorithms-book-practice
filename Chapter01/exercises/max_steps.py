# needed data:
sorted_names = [
    "Aaron", "Abigail", "Addison", "Adrian", "Aiden", "Alice", "Alyssa", "Amelia", "Andrew", 
    "Anna", "Anthony", "Aria", "Ariana", "Aurora", "Ava", "Bella", "Benjamin", "Brayden", 
    "Brooklyn", "Caleb", "Cameron", "Caroline", "Carter", "Charles", "Charlotte", 
    "Chloe", "Christian", "Christopher", "Clara", "Connor", "Cooper", "Daniel", 
    "David", "Dylan", "Elena", "Elijah", "Ella", "Ellie", "Eliza", "Elizabeth", 
    "Eli", "Elias", "Emma", "Ethan", "Eva", "Evelyn", "Ezra", "Gabriel", "Gavin", 
    "Grace", "Hannah", "Harper", "Hazel", "Henry", "Hudson", "Hunter", "Isaac", 
    "Isabella", "Isaiah", "Jack", "Jacob", "James", "Jaxon", "Jeremiah", "John", 
    "Joseph", "Josephine", "Joshua", "Josiah", "Julia", "Kennedy", "Landon", 
    "Layla", "Leah", "Leo", "Levi", "Liam", "Lillian", "Lincoln", "Lola", "Logan", 
    "Luca", "Lucas", "Lucy", "Luna", "Madeline", "Madison", "Mason", "Matthew", 
    "Mia", "Michael", "Mila", "Nash", "Natalie", "Nathan", "Nathaniel", "Nora", 
    "Oliver", "Olivia", "Owen", "Paisley", "Parker", "Penelope", "Peyton", 
    "Riley", "Robert", "Ryan", "Sadie", "Samantha", "Samuel", "Sarah", "Savannah", 
    "Scarlett", "Sebastian", "Sofia", "Sophia", "Sophie", "Stella", "Thomas", 
    "Tyler", "Victoria", "Violet", "William", "Willow", "Wyatt", "Zane", "Zoe", "Zoey"
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

print(binary_search_max_steps(sorted_names, "Nora")) # => 7
print(binary_search_max_steps(sorted_names, "Layla")) # => 7
