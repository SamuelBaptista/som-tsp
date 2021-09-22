import os
import numpy as np
import time

from io_helper import read_tsp, normalize, generate_tsp_from_excel
from neuron import generate_network, get_neighborhood, get_route
from distance import select_closest, route_distance
from plot import plot_network, plot_route
from gif import get_frames, create_gif, remove_images

def main():
    start = time.time()

    files = os.listdir('inputs')

    for file in files:
        print(file)

        filename = file.split('/')[-1].split('.')[0]
        generate_tsp_from_excel('inputs/'+file, filename) 

        problem = read_tsp('assets/'+ filename +'.tsp')

        route = som(problem, 100000, filename)

        problem = problem.reindex(route)
        problem.to_excel(f'outputs/output_from_{filename}.xlsx', index=False)

        distance = route_distance(problem)
        print('Route found of length {}'.format(distance))

        frames = get_frames()
        create_gif(frames, filename)
        remove_images(filename)

    end = time.time()

    print(f'Execution time: {(end-start):0.2f} seconds ')


def som(problem, iterations, filename, learning_rate=0.8):
    """Solve the TSP using a Self-Organizing Map."""
    
    # Obtain the normalized set of cities (w/ coord in [0,1])
    cities = problem.copy()

    cities[['x', 'y']] = normalize(cities[['x', 'y']])

    # The population size is 8 times the number of cities
    n = cities.shape[0] * 8

    # Generate an adequate network of neurons:
    network = generate_network(n)
    print('Network of {} neurons created. Starting the iterations:'.format(n))

    for i in range(iterations):
        if not i % 100:
            print('\t> Iteration {}/{}'.format(i, iterations), end="\r")
        # Choose a random city
        city = cities.sample(1)[['x', 'y']].values
        winner_idx = select_closest(network, city)
        # Generate a filter that applies changes to the winner's gaussian
        gaussian = get_neighborhood(winner_idx, n//10, network.shape[0])
        # Update the network's weights (closer to the city)
        network += gaussian[:,np.newaxis] * learning_rate * (city - network)
        # Decay the variables
        learning_rate = learning_rate * 0.99997
        n = n * 0.9997

        # Check for plotting interval
        if not i % 1000:
            plot_network(cities, network, name='diagrams/{:05d}.png'.format(i))

        # Check if any parameter has completely decayed.
        if n < 1:
            print('Radius has completely decayed, finishing execution',
            'at {} iterations'.format(i))
            break
        if learning_rate < 0.001:
            print('Learning rate has completely decayed, finishing execution',
            'at {} iterations'.format(i))
            break
    else:
        print('Completed {} iterations.'.format(iterations))

    plot_network(cities, network, name='diagrams/final.png')

    route = get_route(cities, network)
    plot_route(cities, route, f'diagrams/route_{filename}.png')
    
    return route

if __name__ == '__main__':
    main()
