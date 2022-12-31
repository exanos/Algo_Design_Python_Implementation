def check_consistency(m, judgments):
    # Initialize the labels dictionary
    labels = {}

    # Iterate through the judgments
    for judgment in judgments:
        i, j = judgment[0], judgment[1]
        # If both i and j are not in the labels dictionary
        if i not in labels and j not in labels:
            # Add them to the labels dictionary with opposite labels
            labels[i] = "A"
            labels[j] = "B"
        # If either i or j is in the labels dictionary and the other is not
        elif i in labels and j not in labels or i not in labels and j in labels:
            # Return "inconsistent"
            return "inconsistent"
        # If both i and j are in the labels dictionary and their labels are the same
        elif labels[i] == labels[j]:
            # If the judgment is "different", return "inconsistent"
            if judgment[2] == "different":
                return "inconsistent"
        # If both i and j are in the labels dictionary and their labels are different
        elif labels[i] != labels[j]:
            # If the judgment is "same", return "inconsistent"
            if judgment[2] == "same":
                return "inconsistent"
    # Return "consistent"
    return "consistent"

# Test the check_consistency function
n = 4
judgments = [(1, 2, "same"), (2, 3, "different"), (3, 4, "same"), (1, 4, "different")]
result = check_consistency(n, judgments)
print(result)  # should print "consistent"
