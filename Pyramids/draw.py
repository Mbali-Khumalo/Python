

def get_shape():
    while True:
        shapes = ['square', 'triangle', 'pyramid']
        shape = input('Shape?: ').lower()
        if shape in shapes:
            return shape



def get_height():
    while True:
        height = input('Height?: ')
        if height.isdigit():
            height = int(height)
            if (height) <=80:
                return int(height)
            


def draw_square(height, outline):
    if outline is False:
        for i in range(height):
            print("*"*height)
    if outline is True:
        for i in range(height):
            for j in range(height):
                if i == 0 or j == 0 or j == height-1 or i == height-1:
                    print("*",end="")
                else:
                    print(" ",end="")
            print()



def draw_triangle(height, outline):
    if outline== False:
        for i in range(height):
            print(""*(height-1)+"*"*(i + 1))
    else:
        for row in range(1,height + 1):
            if row==1 or row==2 or row==height:
                    print("*"*row)
            else:
                print("*" + ' ' * (row -2) + '*')


def draw_pyramid(height, outline):
    if outline == False:
        for num in range(height):
            print(" "*(height-num-1) + "*" * (2*num+1))
    else:
        for num in range(height):
            for a in range(height-num-1):
                print(" ",end="")
            for a in range(2*num+1):
                if a==0 or a==2*num or num==height-1:
                    print ("*", end="")
                else:
                    print(' ', end='')
            print()

def draw(shape, height, outline):
    if shape == 'square':
        draw_square(height, outline)
    if shape == 'triangle':
        draw_triangle(height, outline)
    if shape == 'pyramid':
        draw_pyramid(height, outline)


def get_outline():
    outline = input('Outline? (y/N): ').lower()
    if outline == 'y':
        return True
    elif outline == 'n' or outline== '':
        return False
    
if __name__ == "__main__":
    shape_gram = get_shape()
    height_gram = get_height()
    outline_gram = get_outline()
    draw(shape_gram, height_gram, outline_gram)
