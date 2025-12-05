'''Write a list comprehension to generate a list of squares for all even numbers from 1 to 20.'''
even_num_squares = [x**2 for x in range(1,21) if x%2==0]
print("Squares for all even numbers from 1 to 20 :-",even_num_squares)