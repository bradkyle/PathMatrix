#======================================================================================================================>
# Modules
#======================================================================================================================>

class Module():
    def __init__(self):
        raise NotImplementedError

    #
    def exec_import(self):
        raise NotImplementedError

    #
    def execute(self):
        raise NotImplementedError

    # This function switches a bool value
    # True -> False, False -> True
    def switch_active(self):
        raise NotImplementedError

    #
    def set_input(self):
        raise NotImplementedError

    #
    def return_previous_module(self):
        raise NotImplementedError

    #
    def get_position(self):
        raise NotImplementedError

    #
    def return_num_runs(self):
        raise NotImplementedError

    #
    def setup(self):
        raise NotImplementedError


# Fully Connected module ===============================================================================>
class FullyConnected(Module): #todo possibly could inherit from two classes mainly the tensorflow class and the module class
    def __init__(self):
        Module.__init__(self)
        raise NotImplementedError

#  Reduce Sum module ===============================================================================>
class ReduceSum(Module): #todo possibly could inherit from two classes mainly the tensorflow class and the module class
    def __init__(self):
        Module.__init__(self)
        raise NotImplementedError

#  Dynamic RNN module ===============================================================================>
class DynamicRnn(Module): #todo possibly could inherit from two classes mainly the tensorflow class and the module class
    def __init__(self):
        Module.__init__(self)
        raise NotImplementedError

#  2D Convolutional module ===============================================================================>
class Conv2d(Module): #todo possibly could inherit from two classes mainly the tensorflow class and the module class
    def __init__(self):
        Module.__init__(self)
        raise NotImplementedError

#  Slim 2D Convolutional module ===============================================================================>
class SlimConv2d(Module): #todo possibly could inherit from two classes mainly the tensorflow class and the module class
    def __init__(self):
        Module.__init__(self)
        raise NotImplementedError