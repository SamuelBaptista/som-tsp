import matplotlib.pyplot as plt
import matplotlib as mpl


def plot_candidates(candidates, name):
    fig = plt.figure(figsize=(5, 5), frameon = False)
    axis = fig.add_axes([0,0,1,1])

    axis.set_aspect('equal', adjustable='datalim')
    plt.axis('off')

    plt.scatter(candidates[:,0], candidates[:,1], color='blue', s=4)
    plt.savefig(name, bbox_inches='tight', pad_inches=0, dpi=200)
    plt.close()

def plot_network(cities, neurons, name='diagram.png', ax = None, names = True):
    """Plot a graphical representation of the problem"""
    mpl.rcParams['agg.path.chunksize'] = 10000

    if not ax:
        fig = plt.figure(figsize=(5, 5), frameon = False)
        axis = fig.add_axes([0,0,1,1])

        axis.set_aspect('equal', adjustable='datalim')
        plt.axis('off')

        axis.scatter(cities['x'], cities['y'], color='red', s=4)
        axis.plot(neurons[:,0], neurons[:,1], 'b.', ls='-', markersize=2)

        if names:
            for i in range(len(cities)):
                plt.text(
                    x=cities.x[i],
                    y=cities.y[i],
                    s=cities.codigo[i],
                    fontdict=dict(color='black', size=10, alpha=0.3)
                )

        plt.savefig(name, bbox_inches='tight', pad_inches=0, dpi=200)
        plt.close()

    else:
        ax.scatter(cities['x'], cities['y'], color='red', s=4)
        ax.plot(neurons[:,0], neurons[:,1], 'b.', ls='-', markersize=2)
        return ax

def plot_route(cities, route, name='diagram.png', ax=None, names=True):
    """Plot a graphical representation of the route obtained"""
    mpl.rcParams['agg.path.chunksize'] = 10000

    if not ax:
        fig = plt.figure(figsize=(5, 5), frameon = False)
        axis = fig.add_axes([0,0,1,1])

        axis.set_aspect('equal', adjustable='datalim')
        plt.axis('off')

        if names:
            for i in range(len(cities)):
                plt.text(
                    x=cities.x[i],
                    y=cities.y[i],
                    s=cities.codigo[i],
                    fontdict=dict(color='black', size=10, alpha=0.3)
                )

        axis.scatter(cities['x'], cities['y'], color='blue', s=4)
        route = cities.reindex(route)
        route.loc[route.shape[0]] = route.iloc[0]
        axis.plot(route['x'], route['y'], color='purple', linewidth=1)

        plt.savefig(name, bbox_inches='tight', pad_inches=0, dpi=200)
        plt.close()

    else:
        ax.scatter(cities['x'], cities['y'], color='blue', s=4)
        route = cities.reindex(route)
        route.loc[route.shape[0]] = route.iloc[0]
        ax.plot(route['x'], route['y'], color='purple', linewidth=1)
        return ax
