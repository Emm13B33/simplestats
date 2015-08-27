from stats import mean
from nose.tools import assert_equal

#testing our new mean function
def test_mean():
	assert_equal(mean([2,4]), 3)
#test_mean()

def test_float_mean():
	assert_equal(mean([1,2]), 1.5)
#test_float_mean()

def test_long_mean():
	assert_equal(mean([2,4,6,8]), 5)
#test_long_mean()

