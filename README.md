# Assignment 7
# Spencer Rothfleisch

In this assignment, I expanded the design space of my random creature generator from Assignment 6 to allow the chain to branch in 3D. This randomized robot has a random number of randomly shaped links with random sensor placement, and the links with and without sensors are colored as green and blue, respectively. The orientation of these links are determined by finding faces on each link that do not have a joint and checking to make sure if a link is placed in that location that it does not self-intersect with other links.

Each time "button.py" is ran, a randomized 3D robot is created and simulated. This specific program finds a random number between 3 and 15 to determine the number of links (configurable in constants.py), and then each link has a 50% chance of having a sensor. Each sensor is connected to every motor for a full neural network.

The morphospace is as follows:
-Any body shape is possible that can be created from links that range from 0.5 to 2 units in size in the x, y, and z direction
-Joint orientation changes depending on the

This assignment was built with assistance from [r/ludobots](https://www.reddit.com/r/ludobots/) reddit course and [pyrosim](https://ccappelle.github.io/pyrosim/).