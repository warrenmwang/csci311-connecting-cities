# CSCI311: Connecting Cities
## Group Members: Cuong Nguyen, Warren Wang, Liam Stott, Alex Bigley

Please use Python version `3.11.0`. (Big speed improvements!)

The user will have the options to select the following parameters on the command line to run the project:
- option of algorithm (kruskal (1) or prim (2))
- dataset inputfile
- MST output file (edges formatted same as inputfile)

An example command to run our project using Kruskal's Algorithm on the TG dataset with an output filename of outfile.txt:
`python ./main.py 1 ./datasets/TG.txt outfile.txt`