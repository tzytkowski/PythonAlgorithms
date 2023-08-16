###############################################
#
# Test program for ThreeDimensionalShape
#
###############################################

import ThreeDimensionalShape

CUBE = 1
CYLINDER = 2
QUIT = 3

def main():

    selection =0

    while selection != QUIT:
        print ()
        displayMenu()
        print ()
        selection = int(input('Please enter your selection: '))

        if selection == 1:
            side = float(input('Please enter the lengh of a side: '))
            cube = ThreeDimensionalShape.Cube("Cube", side)
            print ('The volume of the cube is: ', str(cube.calculateVolume()))

        elif selection == 2:
            height = float(input('Please enter the height of the cylinder: '))
            radius = float(input('Please enter the radius of the cylinder: '))
            cylinder = ThreeDimensionalShape.Cylinder("Cylinder", height, radius)
            print ('The volume of the cylinder is: ', str(cylinder.calculateVolume()))

        elif selection == 3:
            print ('Thank you!')

def displayMenu():
    print ('Please select a 3D shape to calculate:')
    print ('1 - The volume of a Cube')
    print ('2 - The volume of a Cylinder')
    print ('3 - QUIT')

main()
