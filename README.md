# Spencer Rothfleisch
# Final Project
# The Engineer

In Assignment 8, I used the parallel hill climber to design morphology and behavior for locomotion for my robot from Assignment 7. This randomized robot has a random number of randomly shaped links with random sensor placement, and the links with and without sensors are colored as green and blue, respectively. The final project takes Assignment 8 and runs it for 10 parents x 500 generations x 10 seeds = 50,000 sims

The morphospace is as follows:<br />
&nbsp;&nbsp;&nbsp;&nbsp;-Any body shape is possible that can be created from random links sized 0.5 to 2 units in the x, y, and z direction<br />
&nbsp;&nbsp;&nbsp;&nbsp;-Joint rotation orientation is determined depending on the placement of the new link relative to the previous link to prevent self-intersection, which limits some movement capabilities but allows for movement in any direction as well as jumping<br />
&nbsp;&nbsp;&nbsp;&nbsp;-For the brain, every joint has a motor neuron, each link has a 50% chance of having a sensor neuron, and the neural network connects every sensor neuron to every motor neuron, meaning a sensor on one side of the body certainly affects a motor on the other side of the body<br />

The mutations are as follows:<br />
&nbsp;&nbsp;&nbsp;&nbsp;-There is a 33% chance of a mutation to a synapse weight, adding a link, or removing a link<br />
&nbsp;&nbsp;&nbsp;&nbsp;-To remove a link, an edge link (a link that is only connected to one joint) is removed, and no link is allowed to be placed in its spot in future generations. Links cannot be removed if there is only 3 links left.<br />
&nbsp;&nbsp;&nbsp;&nbsp;-To add a link, a random openn face is found on a random link. Then, a link without a sensor is generated and connected by joint to the open face, and this joint is given a motor and is connected by synapses to every sensor<br />
&nbsp;&nbsp;&nbsp;&nbsp;-When a synapse weight is mutated, a synapse is selected at random and then its weight is re-randomized between -1 and 1<br />
&nbsp;&nbsp;&nbsp;&nbsp;-Besides randomizing the weight of one synapse or adding a new joint, the rest of the brain and its weights will always remain the same<br />

The algorithm is as follows:<br />
&nbsp;&nbsp;&nbsp;&nbsp;1. Click "button.py" to start generation<br />
&nbsp;&nbsp;&nbsp;&nbsp;2. 5 random robots are created, each with a random number of links between 3 and 15 (configurable in constants.py)<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a. First link is created in an absolute position of [0, 0, 2] with a random size in the range desribed in the morphospace<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b. First joint and second link are added to a random face on first link<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c. An existing link is randomly selected<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;d. A face on the link is randomly selected<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e. Using absolute positions of all links, overlap of a new randomly sized link being placed against that face is tested<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;f. If there is overlap, steps c-e are repeated, if not, continue to step g<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;g. Link is placed at that position with a joint connecting the two links, and if the current number of links is less than the total number of links, go back to step c, but if total number of links is met continue to step 3<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(Just as a note, the link information is stored in array at this point in time and not actually created using pyrosim)<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3. Brain is created<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a. Each link is determined at random to be a sensor or not with a 50% chance<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b. Every joint is given a motor <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c. For the synapses, Every sensor is connected to every motor to be a complete neural network with random weights between -1 and 1<br />
&nbsp;&nbsp;&nbsp;&nbsp;4. Evolution commences<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a. body#.urdf and brain#.nndf are created for the 5 parents (number of parents configurable in constants.py)<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b. Fitness is recorded (distance travelled in negative x direction)<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c. Evolution occurs with a 33% chance of a mutation to a synapse weight, adding a link, or removing a link<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;d. body#.urdf and brain#.nndf are created for the 5 children and fitness is recorded<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e. If the fitness of the child is more favorable than the parent, it takes the parent's position<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;f. This continues for 20 generations (configurable in constants.py)<br />
&nbsp;&nbsp;&nbsp;&nbsp;5. Best evolution and its original parent are shown<br />
&nbsp;&nbsp;&nbsp;&nbsp;6. The fitness of the 5 robots are [plotted](https://github.com/Suspence1127/mybots/blob/assignment8/samplePlot.png) and shown (example shows 5 seeds for 20 generations)<br />

Diagram:
![alt text](https://github.com/Suspence1127/mybots/blob/assignment8/diagramNEW.jpg)

Credits: This assignment was built with assistance from the [r/ludobots](https://www.reddit.com/r/ludobots/) reddit course and the [pyrosim](https://ccappelle.github.io/pyrosim/) python package.