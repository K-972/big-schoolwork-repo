#Write an algorithm that will calculate the amount of paint required to paint a room. The user will enter the dimensions of the room, the total dimensions of the unpaintable areas (such as windows, doors or brickwork) and the number of coats of paint required.Assume that 1 litre of paint covers 11 sq m. 

height = int(input("enter height of walls: "))
length = int(input("enter length of walls: "))

area_of_wall = height * length

area_of_4_walls = area_of_wall * 4

how_many_coats = int(input("how manycoats: "))

cant_paint = int(input("area you cant paint in m2: "))


#print(area_of_4_walls)

area_of_four_walls_minus_cant_paint = area_of_4_walls - cant_paint

one_litre_paint = 11

litres_needed = area_of_four_walls_minus_cant_paint // one_litre_paint

litres_needed = (litres_needed * how_many_coats)

print(f"you need {litres_needed} litres to paint the walls with {how_many_coats} coats")
