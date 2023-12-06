import math

# Define the constants
k_1 = 545140134
k_2 = 13591409
k_3 = 640320
k_4 = 100100025
k_5 = 327843840
k_6 = 53360


# Function to calculate the series sum
def calculate_pi_approximation(n):
    total_sum = 0
    for i in range(n + 1):
        numerator = (-1) ** i * math.factorial(6 * i) * (k_2 + i * k_1)
        denominator = math.factorial(i) ** 3 * math.factorial(3 * i) * (8 * k_4 * k_5) ** i
        total_sum += numerator / denominator
    return total_sum

# Calculate the value of pi using the formula
S = calculate_pi_approximation(1000)  # You can change the number of terms in the series
pi_approximation = k_6 * math.sqrt(k_3) / S

print("Approximation of pi:", pi_approximation)
