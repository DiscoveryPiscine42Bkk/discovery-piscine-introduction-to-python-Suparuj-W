def average(scores):

    total = sum(scores)
    count = len(scores)
    avg = total / count
    print(f"\nAverage score: {avg:.2f}")


if __name__== "__main__":
    scores = []

    print("Enter students' scores one by one.")
    print("Type 'done' when you are finished.\n")

    while True:
        score_input = input("Enter score (or 'done' to finish): ")

        if score_input.lower() == "done":
            break


        try:
            score = float(score_input)
            scores.append(score)
        except ValueError:
            print("Please enter a valid number.\n")
            continue

    if scores:
        average(scores)
    else:
        print("No scores entered.")