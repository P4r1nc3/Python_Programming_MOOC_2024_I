# Write your solution here
def read_input(message, low, high):
    while True:
        try:
            num = int(input(message))
            if num >= low and num <= high:
                return num
        except ValueError:
            pass

        print(f'You must type in an integer between {low} and {high}')
