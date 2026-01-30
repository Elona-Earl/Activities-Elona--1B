word = input("Enter a word: ")

word_length = len(word)

numbers = []

for i in range(word_length):
    num = int(input(f"Number {i + 1}: "))
    numbers.append(num)

def compute_average(num_list):
    return sum(num_list) / len(num_list)

def compare_average_and_length(avg, length):
    if length > avg:
        return "The word length is greater than the average."
    elif length < avg:
        return "The word length is less than the average."
    else:
        return "The word length is equal to the average."

average = compute_average(numbers)

comparison_result = compare_average_and_length(average, word_length)

print("\n------ RESULTS -------")
print("List of numbers entered:", numbers)
print("Length of the word:", word_length)
print("Average of the numbers:", average)
print(comparison_result)
