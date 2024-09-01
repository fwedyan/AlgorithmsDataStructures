# Sum of values in a list

def main():
    # Variables
    total = 0.0

    # Initialize lists
    numbers = [0.5, 0.2, 0.3, 1.4, 5, 10, 20]
    
    for number in numbers:
        total += number
    
    # Display total sales
    print ('Total :', \
           format(total, ',.2f'), sep='')

    # Calculate the average.
    average = total / len(numbers)
    
    # Calculate the maximum.
    highest = max(numbers)
    print(highest)
    print(numbers)
# Call the main function.
main()

