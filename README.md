# Spencer Rothfleisch
# Assignment 8

In this assignment, I used the parallel hill climber to design morphology and behavior for locomotion for my robot in Assignment 7. This randomized robot has a random number of randomly shaped links with random sensor placement, and the links with and without sensors are colored as green and blue, respectively. 

Each time "button.py" is ran, 5 randomized 3D robots are created and evolved for 20 generations (configurable in constants.py). It finds a random number between 3 and 15 to determine the number of links (configurable in constants.py). The orientation of the links and joints are then determined at random before actually creating the joints and links by placing joint and link structs (as defined in joint.py and link.py) in a dictionary, and then all joints and links are created for the simulation once the full robot has been essentially mapped out. The orientation of these links are determined by finding faces on each link that do not have a joint and checking to make sure if a link is placed in that location that it does not self-intersect with other links.

The morphospace is as follows:<br />
-Any body shape is possible that can be created from up the randomized number of links that range from 0.5 to 2 units in size in the x, y, and z direction<br />
-Joint orientation is determined depending on the placement of the link relative to the previous link to prevent self-intersection, which limits some movement capabilities but generally allows for movement in any direction as well as jumping<br />
-For the brain, every joint has a motor neuron, each link has a 50% of having a sensor neuron, and the neural network connects every sensor neuron to every motor neuron, meaning a sensor on one side of the body certainly affects a motor on the other side of the body<br />
For mutations:<br />
-there is a 33% chance of a mutation to a synapse weight, adding a link, or removing a link<br />
-To remove a link, an edge link (a link that is only connected by one joint) is removed, and no link is allowed to be placed in its spot in future generations<br />
-To add a link, open faces are found and then a link without a sensor is added to an open face (as long as that face was not already connected to a link), and the new joint is created with a motor and is connected by synapses to every sensor<br />
-When a synapse weight is mutated, a synapse is selected at random and then its weight is randomized again<br />
-Besides randomizing the weight of one synapse or adding a new joint, the rest of the brain and its weights will remain the same<br />

Diagram:
![alt text](https://github.com/Suspence1127/mybots/blob/assignment7/diagram.jpg?raw=true)

Credits: This assignment was built with assistance from the [r/ludobots](https://www.reddit.com/r/ludobots/) reddit course and the [pyrosim](https://ccappelle.github.io/pyrosim/) python package.