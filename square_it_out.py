def square_it_out(start, end):
    """
    Accepts the beginning and end range of numbers, finds the square values,
    filters the odd and even square values, and prints them.
    """
    # Generate list of squares from start to end inclusive
    squares = [i**2 for i in range(start, end + 1)]
    
    # Filter odd and even squares
    odd_squares = [sq for sq in squares if sq % 2 != 0]
    even_squares = [sq for sq in squares if sq % 2 == 0]
    
    # Print the results
    print("Odd squares:", odd_squares)
    print("Even squares:", even_squares)

# Example usage
if __name__ == "__main__":
    square_it_out(1, 10)
