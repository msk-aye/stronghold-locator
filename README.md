# stronghold-locator
This is a simple script to find the coordinates of a stronghold in Minecraft with two eye throws, using the angles and positions of the two throws to model two linear eqautions, which can be solved to find the coordinates of the stronghold.

It is a very rough script without an error handling etc. since I will only be using it as intended (lol).

I know there are many tools out there that already do this, and to a higher accuracy with less input information, however, in my mind using those tools is cheating, but using your own tool isn't. Don't question it I don't even understand.

### How it works
This script follows a method I devised, with some inspiration from the GOAT 🐐 Goldstreak 🐐, which basically uses the two points and angles to model two 2D lines, using `tan(-yaw)` for the gradient and the coordinates as `(z -> x, x -> y)`. This is done as Minecraft uses a different coordinate system to the cartesian plane I was taught at school, and so I convert the coordinates to cartesian coordinates by switching the `x` and `z`. After the equations of the lines are obtained, I use the `np.linealg.solve` function to find the intersect.

### How to use
Using the script is simple, you just have to look directly at the centre of an eye after throwing it (be as precise and possible and zoom / decrease FOV to make sure you are in the dead centre), and then press `f3 + c` to copy the position to your clipboard. Paste the output as the first input, then reposition ~50-100 blocks away (preferably perpendulcar to the first throw direction) and repeat the process as the second input. The script will then spit out the Overworld and Nether coordinates for the stronghold.

The script takes exact outputs as given by `f3 + c` so do not alter it.
