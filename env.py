#======================================================================================================================>
# Env Class
#======================================================================================================================>


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