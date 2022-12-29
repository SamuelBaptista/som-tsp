import numpy as np
import time

from sklearn.preprocessing import MinMaxScaler
from src.neuron import generate_network, get_neighborhood
from src.distance import select_closest, get_route
from src.plot import plot_network, plot_route, plot_candidates

def som(problem, iterations, filename, learning_rate=0.5):
    """Solve the TSP using a Self-Organizing Map."""
    
    # Obtain the normalized set of cities (w/ coord in [0,1])
    cities = problem.copy()

    scaler = MinMaxScaler()
    cities[['x', 'y']] = scaler.fit_transform(cities[['x', 'y']])

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
        if not i % 250:
            plot_network(cities, network, name='imgs/{:05d}.jpg'.format(i))

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

    route = get_route(cities, network)
    plot_route(cities, route, f'imgs/route_{filename}.jpg')
    
    return route