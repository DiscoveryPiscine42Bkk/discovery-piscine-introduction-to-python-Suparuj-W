def array_of_names(name_dict):

    full_names = []
    for first, last in name_dict.items():
        full_name = f"{first.capitalize()} {last.capitalize()}"
        full_names.append(full_name)
    return full_names

if __name__== "__main__":
    name_dict = {}

    while True:
        first = input("Enter first name (or leave empty to finish): ")
        if first.strip() == "":
            break
        last = input("Enter last name: ")
        name_dict[first] = last

    if name_dict:
        print("Full names list:")
        print(array_of_names(name_dict))
    else:
        print("No names were entered.")