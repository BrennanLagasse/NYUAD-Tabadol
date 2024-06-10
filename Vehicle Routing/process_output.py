import random

def parse_string(input_string):
    return list(map(int, input_string.split('_')))

def get_routes_from_sample(sample, num_vehicles, num_steps):
    """Builds a set of routes from the sample returned."""

    routes =  [[-1]*num_steps for _ in range(num_vehicles)]

    # Go through all entries
    for key, val in sample.items():
        vehicle, vertex, step = parse_string(key)
        if val == 1.0:
            routes[vehicle][step] = vertex

    # Clean up trailing and leading values (not optimized)
    for route in routes:
        for i in range(len(route)):
            if route[i] == 5:
                route.pop(0)

    for route in routes:
        for i in range(len(route)-1, 0, -1):
            if route[i] == 5:
                route.pop(i) 

    return routes

def get_cost_routes(paths, distances):
    cost = 0

    num_vertices = len(distances)

    for path in paths:
        if len(path) > 0:

            # Cost in middle of path
            for i in range(len(path) - 1):
                cost += distances[path[i]][path[i+1]]

            # Cost of first choice
            cost += distances[num_vertices - 1][path[0]]

            # Cost of last choice
            cost += distances[path[len(path) - 1]][num_vertices - 1]

    return cost

def report_output(routes, distances):
    print(f'Best routes (depot omitted at start and end):')
    for num, route in enumerate(routes):
        print(f'\tVehicle {num}: {route}')

    print(f'Best cost: {get_cost_routes(routes, distances)}')


def sanity_check(distances, num_vehicles):
    """Test a number of random routes to determine if the outputted score is reasonably good. Quick and lazy indicator of quality"""

    r = []
    for i in range(num_vehicles):
        r.append(i)

    min = 300
    best_route = r
    # Randomly sample a lot of options
    for i in range(10000):
        random.shuffle(r)

        routes = []

        average_visits_per_vehicle = len(distances) // num_vehicles

        for i in range(num_vehicles - 1):
            routes.append(r[i*average_visits_per_vehicle : (i+1)*average_visits_per_vehicle])

        r.append(r[(num_vehicles-1)*average_visits_per_vehicle:])

        cost = get_cost_routes(routes, distances)
        if cost < min:
            min = cost
            best_routes = routes
    print(min)
    print(best_routes)