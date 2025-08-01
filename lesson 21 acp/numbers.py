def filter_square_values(start, end):
    squares = [i**2 for i in range(start, end + 1)]
    
    even_squares = [sq for sq in squares if sq % 2 == 0]
    odd_squares = [sq for sq in squares if sq % 2 != 0]

    print(f"Square values from {start} to {end}: {squares}")
    print(f"Even square values: {even_squares}")
    print(f"Odd square values: {odd_squares}")
filter_square_values(1, 10)