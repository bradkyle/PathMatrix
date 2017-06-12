#======================================================================================================================>
# Env Class
#======================================================================================================================>
# Run through training for a set number of iterations and then use inference whereby multiple environments can simultaneousely
#

class Env():
    def __init__(self):
        raise NotImplementedError

    def create_env(self):
        raise NotImplementedError

    def generate_actions(self):
        raise NotImplementedError

    def action(self):
        raise NotImplementedError

    def is_episode_finished(self):
        raise NotImplementedError

# ======================================================================================================================>
# Environments
# ======================================================================================================================>
# It would be efficient if multiple environments could be trained apon at the same time
# ideas: car driving, robotics, natural language, natural language generatioon, trading & portfolio management, game playing
# For instance in robotics the environment would consist of the information fed from the sensors.
# frame rate
# Environments contain inherent interpreters which return the previous rewards and the state to the agent to perform
# an action


# Flash environment ===============================================================================================>
class FlashEnv(Env):
    def __init__(self):
        Env.__init__(self)
        raise NotImplementedError

# Flash environment ===============================================================================================>
class AtariEnv(Env):
    def __init__(self):
        Env.__init__(self)
        raise NotImplementedError

# Deepmind lab environment ========================================================================================>
class DeepmindLabEnv(Env):
    def __init__(self):
        Env.__init__(self)
        raise NotImplementedError

# Cryptocurrency trading environment ==============================================================================>
class CryptoTradeEnv(Env):
    def __init__(self):
        Env.__init__(self)
        raise NotImplementedError

# Stock Trading environment =======================================================================================>
class StockTradeEnv(Env):
    def __init__(self):
        Env.__init__(self)
        raise NotImplementedError

# Forex Trading environment =======================================================================================>
class ForexTradeEnv(Env):
    def __init__(self):
        Env.__init__(self)
        raise NotImplementedError

# Commodoties Trading environment =================================================================================>
class CommodotiesTradeEnv(Env):
    def __init__(self):
        Env.__init__(self)
        raise NotImplementedError

# V Rep Robots environment ========================================================================================>
class VRepRobotEnv(Env):
    def __init__(self):
        Env.__init__(self)
        raise NotImplementedError

# Gazebo robots environment =======================================================================================>
class GazeboRobotEnv(Env):
    def __init__(self):
        Env.__init__(self)
        raise NotImplementedError

# Webots robots environments ======================================================================================>
class WebotsRobotEnv(Env):
    def __init__(self):
        Env.__init__(self)
        raise NotImplementedError

# Natural language understanding environment ======================================================================>
class LangEnv(Env):
    def __init__(self):
        Env.__init__(self)
        raise NotImplementedError

# Flash environment ===============================================================================================>
class RobotEnv(Env):
    def __init__(self):
        Env.__init__(self)
        raise NotImplementedError

# Amber Environment ==============================================================================================>
class AmberEnv(Env):
    # in the amber environment -> each entity will contain its own interpreter and agent to which actions and rewards as
    # well as states could be fed respectively
    # The environment in this instance would be the entirety of the omnigraph
    def __init__(self):
        Env.__init__(self)
        raise NotImplementedError

#======================================================================================================================>
# Rewards
#======================================================================================================================>
# Selection of rewards could be an external process that would include both reinforcement learning representative of
# taught behaviour (given as a series of states). As well as genetic rewards .etc
# Rewards is a dynamic referable class that is actively set by the environment


#======================================================================================================================>
# Actions
#======================================================================================================================>


#======================================================================================================================>
# State
#======================================================================================================================>


#======================================================================================================================>
# Cropscreen Class
#======================================================================================================================>
class CropScreen():
    def __init__(self):
        raise NotImplementedError

    def observation(self):
        raise NotImplementedError

#======================================================================================================================>
# Utilities
#======================================================================================================================>