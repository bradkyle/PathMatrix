#======================================================================================================================>
# Pathnet Class
#======================================================================================================================>

# The PathMatrix class represents a 3D matrix of machine laerning modules each comprised of a neural net with its internal
# neurons
# it would be efficient if the path-matrix grew with the amount that it learnt

class PathMatrix():

    def __init__(self):
        raise NotImplementedError

    # Initializes the entire pathmatrix network
    # i.e. it creates a matrix of modules, records the configuration of modules
    # adds a final single layer exit matrix comprized of linear modules
    # specifies and initializes the current best path
    def init(self):
        raise NotImplementedError

    # Return all paths that have been initialized within the PathMatrix
    # i.e. a set number of paths have been initialized -> return all of them
    def return_all_paths(self):
        raise NotImplementedError

    # Receives a sample of 2 available paths from the PathMatrix
    # win = path with highest fitness, lose = path with lowest fitness,
    # replaces the lose path with the win path and mutates the new copy of
    # the win (lose) path
    def evolve(self):
        raise NotImplementedError

    #returns a random list of 2 unique paths
    def sample(self):
        raise NotImplementedError

    #returns the best path in the current path matrix
    def return_best_path(self):
        raise NotImplementedError

    #returns a random control
    def return_control(self):
        raise NotImplementedError

    #returns the path of the control
    def return_control_path(self):
        raise NotImplementedError

    #
    def forward(self):
        raise NotImplementedError

    # Takes a 'snapshot' of the pathmatrix in it's current form
    # so that it can be saved .etc
    def snapshot(self):
        raise NotImplementedError

    #saves the current
    def save(self):
        raise NotImplementedError

    #loads a saved model
    def load(self):
        raise NotImplementedError