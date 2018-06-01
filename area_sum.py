import math
import ballinbox as bb
import validate as val

def area_sum(circles):
    area = 0.0
    for circle in circles:
        area += circle[2]**2 * math.pi

    return area

__name__ = '__main__'
if __name__ == '__main__':
    num_of_circle = 5
    blockers = [(0.5, 0.5),(0.5, -0.3)]
    circles = bb.ball_in_box(num_of_circle,blockers)
    t = 0
    while t<100000:
        circles1 = bb.ball_in_box(num_of_circle, blockers)
        if area_sum(circles)<area_sum(circles1):
            circles = circles1
        t += 1
    
    if num_of_circle == len(circles) and val.validate(circles, blockers):
        area = area_sum(circles)
        print "The case: num_of_circle = 5   blockers (0.5,0.5)  (0.5,-0.3)"
        print("Total area: {}".format(area))
        for circle in circles:
            print "(", circle[0], circle[1], circle[2], ")"
    else:
        print("Error: no good circles.")


