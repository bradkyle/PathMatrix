# ======================================================================================================================>
# Path
# ======================================================================================================================>

#set learninng rate to low as in the article

class Path():

    # Should have a local scope representative of whether the path
    # is the main one i.e. in the pathmatrix or is one utilized by
    # a worker path instance
    def __init__(self):
        raise NotImplementedError

    #returns the path
    def return_path(self):
        raise NotImplementedError

    #trains the local model
    def train_model(self):
        raise NotImplementedError

    # runs the interactive session with the environments
    # sets the respective reward, values and policy .etc
    # Sets tensorflow summaries
    # essentially uses the trained model above to enact
    # an action which it then attributes a value and a policy
    # towards.
    # after run has been completed on 2 paths -> the 2 paths
    # are compared and the best one is chosen and the worst one
    # is removed.
    def run(self):
        raise NotImplementedError

    # loops through entire path running apply
    # mutation on each module within it.
    def mutate(self):
        raise NotImplementedError

    # change the path to within a ratio of the dimensions
    # of the path matrix (or any method that will mutate it
    # so that all possible options are accounted for).
    def apply_mutation(self):
        raise NotImplementedError

    # copy the new path passed to it and replace the old
    # path with the new one.
    def overwrite(self):
        raise NotImplementedError

    # returns a path initialized with None/ np.Nan.
    def return_none_path(self):
        raise NotImplementedError

    # returns a path.
    def return_empty_path(self):
        raise NotImplementedError

    # makes a copy of the path to be used in an.
    # operation
    def return_copy(self):
        raise NotImplementedError

    # Used to set worker path parameters to that
    # of the source/main target graph.
    def update_target_path(self):
        raise NotImplementedError

# ======================================================================================================================>
# Worker
# ======================================================================================================================>
# A worker agent is analagous of a electrical flow in the brain -> i.e. multiple exist at the same time. strengthening
# Pathways as they pass through the brain
# worker creates a local copy of a Path and is run
# in multiple Processes
class Worker(Path):
    def __init__(self):
        Path.__init__(self)
        raise NotImplementedError

