
from vagabundo import StandarHomeless, Left_Homeless
from field import Field
from coordinate import Coordinate

from bokeh.plotting import figure, output_file, show

def know_type_homeless(type_homeless):
    if type_homeless.__name__ == StandarHomeless:
        return "Vagabundo Estandar"
    elif type_homeless.__name__ == Moderate_Homeless:
        return "Vagabundo Moderado"
    else:
        return "Vagabundo Izquierdista"

def walking(field, homeless, steps):
    begin = field.get_coordinate(homeless)
    
    for _ in range(steps):
        field.move_homeless(homeless)
        
    return begin.distance(field.get_coordinate(homeless))

def simulate_walk(steps, number_of_attemps, type_homeless):
    homeless = type_homeless(name='Ivan')
    begin = Coordinate(0, 0)
    distance = []
    
    for _ in range(number_of_attemps):
        field = Field()
        field.add_homless(homeless, begin)
        simulation_walk = walking(field, homeless, steps)
        distance.append(round(simulation_walk, 1))
        
    return distance

def graph(x,y):
    paint = figure(title="Random Road", x_axis_label="Steps", y_axis_label="Distance")
    paint.line(x, y, legend_label = "Distance")
    show(paint)
    
def main(walk_distance, number_of_attemps, type_homeless):
    average_walking_distance = []
    
    for steps in walk_distance:
        distance = simulate_walk(steps, number_of_attemps, type_homeless)
        distance_average = round(sum(distance)/len(distance),3)
        distance_max = max(distance)
        distance_min = min(distance)
        average_walking_distance.append(distance_average)
        print(f"{type_homeless.__name__}Random Road of{steps}")
        print(f"Media = {distance_average}")
        print(f"Max = {distance_max}")
        print(f"Min = {distance_min}")
        
        graph(walk_distance, average_walking_distance)
        
if __name__ == "__main__":
    walk_distance = [10, 100, 1000, 10000]
    number_of_attemps = 100
    
    main(walk_distance, number_of_attemps, StandarHomeless)