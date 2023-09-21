# Read User Input
jury = input()

# Logic

while jury != "Finish":
    current_presentation = input()
    current_presentation_score = float(input())
    average_presentation = 0

    for presentation in range(int(jury)):

        average_presentation += current_presentation_score
        current_presentation_score = float(input())


# Print Output
