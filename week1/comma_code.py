def comma_code(items):
    if len(items) == 0:
        return ''
    elif len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return f"{items[0]} and {items[1]}"
    else:
        return ', '.join(items[:-1]) + f", and {items[-1]}"


balls = ['red', 'blue', 'green', 'yellow']
print(comma_code(balls))  # Output: red, blue, green, and yellow

utensils = ['fork', 'knife', 'spoon']
print(comma_code(utensils))  # Output: fork, knife, and spoon

anime = ['Naruto', 'One Piece', 'Attack on Titan', 'My Hero Academia']
print(comma_code(anime))  # Output: Naruto, One Piece, Attack on Titan

