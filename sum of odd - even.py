def sum_even_odd(numbers):
    even_sum = 0
    odd_sum = 0

    for number in numbers:
        if number % 2 == 0:
            even_sum += number
        else:
            odd_sum += number  # Handle odd numbers here

    return (even_sum, odd_sum)

numbers = [1, 2, 3, 4, 5, 6]
print(sum_even_odd(numbers))

