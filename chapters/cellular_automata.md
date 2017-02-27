# Title 

Cellular Automata

# Tags

engineering, math, technology, computer science

# Introduction

Cellular automata provides a simple introduction to a number of computer science basics to kids. Firstly, it teaches *algorithms*, or recipes. Given a set of rules, when the kids follow them they get to see real results. Secondly, it teachs *binary logic operators* like XOR (exclusive OR). 

The development of [cellular automata](https://en.wikipedia.org/wiki/Cellular_automaton) (CA) systems is typically attributed to Stanisław Ulam and John von Neumann, who were both researchers at the Los Alamos National Laboratory in New Mexico in the 1940s. Ulam was studying the growth of crystals and von Neumann was imagining a world of self-replicating robots. That’s right, robots that build copies of themselves. Once we see some examples of CA visualized, it’ll be clear how one might imagine modeling crystal growth; the robots idea is perhaps less obvious. Consider the design of a robot as a pattern on a grid of cells (think of filling in some squares on a piece of graph paper). Now consider a set of simple rules that would allow that pattern to create copies of itself on that grid. This is essentially the process of a CA that exhibits behavior similar to biological reproduction and evolution.

CA has a number of simple "rules" that define system behavior, like "If my neighbors are both active, I am inactive" and the like. The rules are all given numbers, but they're not sequential for historical reasons. These rules have various numbers as their names, and all exhibit interesting behaviors given their inputs. 

The subject rule for this exercise, Rule 90, is one of the simplest, a simple neighbor XOR. That is, in a 1 dimensional CA system (e.g. a line), the next state for the cell in the middle of 3 is simply the result of the XOR of its left and right neighbors. E.g. "000" becomes "1" in the next state, "100" becomes "1" in the next state and so on. You traverse the given line in windows of 3 cells and calculate the rule for the next iteration of the following row's center cell based on the current one while the two outer cells are influenced by their respective neighbors. Here are the rules showing the conversion from one set of cells to another:

| "111" | "101" | "010" | "000" | "110" | "100" | "011" | "001"
|-----------|------------|------------|-----------|------------|------------|------------|------------
| 0  | 0  | 0  | 0  | 1  | 1  | 1  | 1  |

# Materials 

For this exercise, you'll need a **pencil and graph paper**. We used also used a small piece of stiff paper to make a T-shaped window, easing the kids' calculations - it highlights the three cells from the previous row that matter and the one we have to fill in for the current row. 

# Exercise

We did a couple of inputs. The first one was a single block filled in at the top of the graph paper. As the kids work their way, left to right, on the next line, they fill in two squares. The next line, those two squares start to move apart. On the next line they complete a triangle. After this, keep going. You'll develop the [Sierpinski Sieve](http://mathworld.wolfram.com/SierpinskiSieve.html) or the Sierpinski Triangle - a triangle fractal where the centers are triangular cutouts. 

For another input, we did a random row with randomly filled in squares in the first line, and then had them calculate the next several lines. This randomness creates random rows below it.

# Discussions

From here we talked about a couple of things. 

First we talked about the binary XOR rule and created a truth table for A and B, the two cells on the left and right (ignoring the one in the middle) of the previous row. This two cells determine the middle cell in the next row. If they match, the next row's middle cell is filled in; if they differ then the cell is not filled in:

| A | B | Result 
|---|---|-------
| Filled | Filled | Filled
| Empty  | Empty  | Filled
| Empty  | Filled | Empty
| Filled | Empty  | Empty

Then we talked about how cellular automata sort of show how natural phenomenon work. For instance, these patterns emerge on a macroscopic scale like forest populations, and microscope patterns such as mollusk shells. 

# Results 

Overall this exercise was well-received by my older son (the younger son was away that evening). He really got into it, and enjoyed giving me sample inputs, as well. 

# References

Weisstein, Eric W. "Elementary Cellular Automaton." From MathWorld--A Wolfram Web Resource. http://mathworld.wolfram.com/ElementaryCellularAutomaton.html