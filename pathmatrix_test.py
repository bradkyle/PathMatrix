import unittest

#======================================================================================================================>
# Pathnet Testing
#======================================================================================================================>

class PathMatrixTest(unittest.TestCase):

    # Ensure that a matrix representing the dimentions
    # provided has been created and that the final layers
    # have been appended.
    def test_init(self):
        raise NotImplementedError

    # Make sure that all of the paths have been returned.
    def test_return_all_paths(self):
        raise NotImplementedError

    # Test that the function doesn't run when the batch
    # selector is turned on and that it can handle equal
    # fitness situations.
    def test_evolve(self):
        raise NotImplementedError

    # Test that 2 unique paths are returned given
    # a set of paths.
    def test_sample(self):
        raise NotImplementedError

    # Test that the best path is returned given
    # a set of paths.
    def test_return_best_path(self):
        raise NotImplementedError

    # Test that a random sample is returned from
    # a set of paths
    def test_return_control(self):
        raise NotImplementedError

    # Test that a path is returned representative of the
    # control
    def test_return_control_path(self):
        raise NotImplementedError

    # Test that an accurate snap shot is taken
    def test_snapshot(self):
        raise NotImplementedError

    # Test that the PathMatrix can be saved correctly
    def test_save(self):
        raise NotImplementedError

    # Test that the PathMatrix can be loaded correctly
    def test_load(self):
        raise NotImplementedError

# ======================================================================================================================>
# Selector Testing
# ======================================================================================================================>

class SelectorTest(unittest.TestCase):

    def test_get_weak(self):
        raise NotImplementedError

    def test_select(self):
        raise NotImplementedError