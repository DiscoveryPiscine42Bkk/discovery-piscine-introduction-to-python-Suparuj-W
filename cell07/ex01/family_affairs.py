def find_the_redheads(family):

    redheads = filter(lambda name: family[name].lower() == "red", family)
    return list(redheads)


if __name__== "__main__":
    family = {}

    while True:
        name = input("Enter family member's first name (or leave empty to finish): ")
        if name.strip() == "":
            break
        hair_color = input(f"Enter {name}'s hair color: ")
        family[name] = hair_color

    redheads = find_the_redheads(family)

    if redheads:
        print("Red-haired family members:")
        print(redheads)
    else:
        print("No red-haired family members found.")