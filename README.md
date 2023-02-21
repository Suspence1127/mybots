# Spencer Rothfleisch
# Assignment 7

In this assignment, I expanded the design space of my random creature generator from Assignment 6 to allow the chain to branch in 3D. This randomized robot has a random number of randomly shaped links with random sensor placement, and the links with and without sensors are colored as green and blue, respectively. The orientation of these links are determined by finding faces on each link that do not have a joint and checking to make sure if a link is placed in that location that it does not self-intersect with other links.

Each time "button.py" is ran, a randomized 3D robot is created and simulated. This specific program finds a random number between 3 and 15 to determine the number of links (configurable in constants.py). The orientation of the links and joints are then determined at random before actually creating the joints and links through the use of joint and link structs being placed in a dictionary, and then all joints and links are created for the simulation once the full robot has been essentially mapped out.

The morphospace is as follows:<br />
-Any body shape is possible that can be created from up the randomized number of links that range from 0.5 to 2 units in size in the x, y, and z direction<br />
-Joint orientation is determined depending on the placement of the link relative to the previous link to prevent self-intersection, which limits some movement capabilities but generally allows for movement in any direction as well as jumping<br />
-For the brain, every joint has a motor neuron, each link has a 50% of having a sensor neuron, and the neural network connects every sensor neuron to every motor neuron

Diagram:
![alt text](https://github.com/Suspence1127/mybots/blob/assignment7/diagram.jpg?raw=true)

Credits: This assignment was built with assistance from the [r/ludobots](https://www.reddit.com/r/ludobots/) reddit course and the [pyrosim](https://ccappelle.github.io/pyrosim/) python package.