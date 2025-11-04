def famous_births(people_dict):

    sorted_people = sorted(
        people_dict.values(),
        key=lambda x: x[":date_of_birth"]
    )


    for person in sorted_people:
        print(f"{person[':name']} was born on {person[':date_of_birth']}")


if __name__== "__main__":
    people = {}

    print("Enter people's information. Leave name empty to finish.\n")

    while True:
        key = input("Enter a unique key for this person (or leave empty to finish): ")
        if key.strip() == "":
            break

        name = input("Enter full name: ")
        dob = input("Enter date of birth (YYYY-MM-DD): ")

        people[key] = {":name": name, ":date_of_birth": dob}

    if people:
        print("\nPeople sorted by date of birth:")
        famous_births(people)
    else:
        print("No people entered.")