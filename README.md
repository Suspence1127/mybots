# Final Project - The Artist
Created By Spencer Rothfleisch

![FinalProjectGif](https://github.com/Suspence1127/mybots/blob/finalProject/FinalProjectGif.gif)

As seen in the teaser gif above, I used the parallel hill climber methodology to design and evolve morphology and behavior for randomly generated robots. This randomized robot has a random number of randomly shaped links with random sensor placement, and the links with and without sensors are colored as green and blue, respectively.

[YouTube Link](https://www.youtube.com/watch?v=lpZJTHlbugk) (explains the following and shows examples)

The morphospace:<br />

Any body shape is possible that can be created from random links sized 0.5 to 2 units in the x, y, and z direction. Bodies and joints are created as follows: (The numbers on the phenotype diagram represent one posibility of the order that the robot links were generated)<br/>
![BodyCreation](https://github.com/Suspence1127/mybots/blob/finalProject/bodyCreationDiagram.jpg)<br/>

The neural network of the brain sends synapses that connect every sensor neuron to every motor neuron:<br/>
![BrainCreation](https://github.com/Suspence1127/mybots/blob/finalProject/brainCreationDiagram.jpg)<br/>

Each generation a mutation occurs and each has a 33% chance of happening, as explained in the following diagram:<br />
![mutationDiagram](https://github.com/Suspence1127/mybots/blob/finalProject/mutationDiagram.jpg)<br/>

Evolution is conducted and the most fit robot is selected as shown below:<br/>
![selectionDiagram](https://github.com/Suspence1127/mybots/blob/finalProject/selectionDiagram.jpg)<br/>

Detailed look at how the algorithm works:<br />
&nbsp;&nbsp;&nbsp;&nbsp;1. Click "button.py" to start generation of 5 seperate parallelHillclimber.py (PHC) classes<br />
&nbsp;&nbsp;&nbsp;&nbsp;2. 5 random robots are created using solution.py for each iteration of PHC, each with a random number of links between 3 and 15 (configurable in constants.py)<br />
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
&nbsp;&nbsp;&nbsp;&nbsp;4. Evolution commences via the mutate methods in PHC<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a. body#.urdf and brain#.nndf are created for the 5 parents (number of parents configurable in constants.py)<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b. Fitness is recorded (distance travelled in negative x direction) using results from the simulation conducted through runSim.py<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c. Evolution occurs with a 33% chance of a mutation to a synapse weight, adding a link, or removing a link<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;d. body#.urdf and brain#.nndf are created for the 5 children and fitness is recorded<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e. If the fitness of the child is more favorable than the parent, it takes the parent's position<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;f. This continues for 20 generations (configurable in constants.py)<br />
&nbsp;&nbsp;&nbsp;&nbsp;5. Best evolution and its original parent are saved from each seed of PHC<br />
&nbsp;&nbsp;&nbsp;&nbsp;6. The best iteration of the robot and its parent are displayed using runSim.py.<br /> 
&nbsp;&nbsp;&nbsp;&nbsp;7. The fitness of the 5 robots are plotted:<br />
![alt text](https://github.com/Suspence1127/mybots/blob/finalProject/samplePlot.png)<br />
This example has 5 seeds, with each seed evolving 5 robots for 20 generations. The most fit robot from each seed is graphed.

Finally, to see a 5 of the best performing robots (and their original parents), run button.py with seedShift = 30, 49, 60, 100, or 127 in constants.py, which is acts as a checkpoint to reload the best bots. It may take around 3 minutes for these bots to load, depending on the specifications of your computer.

Credits: This assignment was built with assistance from the [r/ludobots](https://www.reddit.com/r/ludobots/) reddit course and the [pyrosim](https://ccappelle.github.io/pyrosim/) python package.