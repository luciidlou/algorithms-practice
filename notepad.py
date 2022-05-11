def find_all_hobbyists(hobby, hobbies):
    """bleh"""
    hobbyists = []
    for name, hobby_list in hobbies.items():
        for h in hobby_list:
            if h == hobby:
                hobbyists.append(name)

    return hobbyists


if __name__ == "__main__":
    hobbies = {
        "Steve": ['Fashion', 'Piano', 'Reading'],
        "Patty": ['Drama', 'Magic', 'Pets'],
        "Chad": ['Puzzles', 'Pets', 'Yoga']
    }

    print(find_all_hobbyists('Yoga', hobbies))
