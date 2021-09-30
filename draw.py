

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    user_input = ""
    while not user_input in ("pyramid","square","triangle","rhombus","diamond","inverted triangle"):   
          user_input =input("Shape?: ").lower()      
    return user_input
     
# TODO: Step 1 - get height (it must be int!)
def get_height():
    height_number = 81
    while not (0 < height_number < 81):
        height_number = input("Height?: ").strip()
        if height_number.isnumeric():
            height_number = int(height_number)
        else:
            height_number = 81
    return height_number

# TODO: Step 2
def draw_pyramid(height, outline):
    if outline == True:
        for tall in range(height):
            for bottom in range(height-tall-1):
                    print(" ", end="")
            for stars in range(2*tall+1):
                if stars == 0 or stars == 2*tall  or tall == height-1:
                    print("*", end="")
                else:
                    print(" ", end="")  
            print()
    else:
        for tall in range(height):
            for length in range(height-tall-1):
                print(" ", end="")
            for tall in range(2*tall + 1):
                print("*", end="")
            print()

# TODO: Step 3
def draw_square(height, outline):
    if outline == True:
        for side in range(height):
            for breath in range(height):
                if side == 0 or breath == 0 or side == (height-1) or breath == (height-1):
                    print("*", end="")
                else:
                    print(" ", end="")  
            print()
    else:
        for side in range(height):
            for breath in range(height):
                print("*", end="")
            print()

# TODO: Step 4
def draw_triangle(height, outline):
    if outline == True:
        for halved_side in range(height):
            for base in range(halved_side+1):
                if halved_side == 0 or base == 0 or halved_side == base or halved_side == (height-1):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    else:
        for halved_side in range(height):
            for base in range(halved_side+1):
                print("*", end="")  
            print()          

def draw_rhombus(height, outline):
    if outline == True:
        for slanted_side in range(height):
            for slanted_base in range(height-slanted_side-1):
                print(" ", end="")
            for star in range(height):
                if star == 0 or slanted_side == 0 or star == (height-1) or slanted_side == (height-1):
                    print("*", end="")
                else:
                    print(" ", end="")    
            print()
    else:
        for slanted_side in range(height):
            for slanted_base in range(height-slanted_side-1):
                print(" ", end="")
            for star in range(height):
                print("*", end="")
            print()    

def draw_diamond(height, outline):
    if outline == True:
        for top_side in range(height-1):
            for top_base in range(height-top_side-1):
                    print(" ", end="")
            for starz in range(2*top_side+1):
                if starz == 0 or starz == 2*top_side:
                    print("*", end="")
                else:
                    print(" ", end="")
            print() 
        for top_side in range(height):
            for top_base in range(top_side):
                print(" ", end="")
            for starz in range(2*(height-top_side)-1):
                if starz == 0 or starz == 2*(height-top_side-1):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()    
                
    else: 
        for top_side in range(height):
            for top_base in range(height-top_side-1):
                print(" ", end="")
            for starz in range(2*top_side+1):
                print("*", end="")
            print()  
        for top_side in range(height-1):
            for top_base in range(top_side+1):
                print(" ", end="")
            for starz in range(2*(height-top_side-1)-1):
                print("*", end="")
            print()

def draw_inverted_triangle(height, outline):
    if outline == True:
        for right_side in range(height):
            for right_base in range(height-right_side):
                if right_base == 0 or right_side == 0 or right_base == (height-right_side-1):
                    print("*", end="")
                else:
                    print(" ", end="")
            print() 
    else:
        for right_side in range (height):
            for right_base in range(right_side+1):
                print("*", end="")
            print()

# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == ("pyramid"):
        draw_pyramid(height, outline)
    if shape == ("square"):
        draw_square(height, outline)
    if shape == ("triangle"):
        draw_triangle(height, outline)    
    if shape == ("rhombus"):
        draw_rhombus(height, outline)
    if shape == ("diamond"):
        draw_diamond(height, outline)
    if shape == ("inverted triangle"):
        draw_inverted_triangle(height, outline)        

# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    outline_input = input("Outline? [y/n]").lower()
    if outline_input == "y":
        return True
    else:   
        return False


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

