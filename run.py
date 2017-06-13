# ======================================================================================================================>
# Run the PathMatrix in a specified manner
# ======================================================================================================================>
# Checks whether the PathMatrix will utilize gpu or cpu, how many processors it will use whether or not it is training or
# inference sets the global episodes tensorflow sessions, co-ordinators and workers as well as the device that is used .etc
# Interprets the environment and various logging and set up procedures
# Load model/'s, Save model/'s .etc
# Create dirs
# Can even be used to run a genetic algorithm on the PathMatrix itself.
# Sets the nature of the selection i.e. batch or pair selection.

class Run():
    # Set the number of workers, model path
    def __init__(self):
        raise NotImplementedError
        #place run code in init

    # takes in config set in init and runns the pathnet
    def run(self):
        raise NotImplementedError

    # setup all the workers with their respective
    # arguments before they are run in run
    def setup_workers(self):
        raise NotImplementedError

    # create all directories if they don't already exist
    def setup_dirs(self):
        raise NotImplementedError















