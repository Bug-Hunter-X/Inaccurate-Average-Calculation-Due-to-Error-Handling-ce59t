def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

# Example usage (corrected)
averages = []
for i in range(5):
    data = []
    try:
        data.append(float(input(f"Enter number {i+1}: ")))
        averages.append(calculate_average(data))
    except ValueError:
        print("Invalid input. Skipping.")
        # Corrected: Don't append anything if there's an error
        pass # Pass here to skip this iteration

print(f"Averages: {averages}")# The corrected code addresses the bug by removing the problematic line and using pass to skip the iteration in case of an error. This ensures only valid averages are included in the results.