import matplotlib.pyplot as plt

from rd_walk import RandomWalk
# this code plots all the points in the walk

# make a random walk
while True:
    rw = RandomWalk()
    rw.fill_walk()

    # plot points in the walk
    plt.style.use("classic")
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers,cmap=plt.cm.Blues,edgecolors="none", s=15)
    # emphasize the first and last points
    ax.scatter(0, 0, c="green", edgecolors="none", s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors="none", s=100)

    plt.show()

    keep_running = input("Make another walk? (y/n):")
    if keep_running == "n":
        break



