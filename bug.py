def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

# Example usage (potential error)
averages = []
for i in range(5):
    data = []
    # Simulate some data acquisition (potentially with errors)
    try:
        data.append(float(input(f"Enter number {i+1}: ")))
    except ValueError:
        print("Invalid input. Skipping.")
        # Here's the bug: we skip, but we still add to averages
        averages.append(0) # Appending 0 here is problematic
    else:
        averages.append(calculate_average(data))

print(f"Averages: {averages}")