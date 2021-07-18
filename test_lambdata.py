"""basic unit test for Lambdata package"""

from random import randint
import pytest
import lambdata as ld
from lambdata import oop_example


# testing __init__ in lambdata


def test_increment_int():
    """Making sure increment works"""
    x0 = 0
    y0 = ld.increment(x0) # = 1
    assert y0 == 1

    x1 = 100
    y1 = ld. increment(x1) # 101
    assert y1 == 101


def test_increment_float():
    """make sure increment works for floats"""
    x0 = 10.5
    y0 = ld.increment(x0)
    assert y0 == 11.5


def test_increment_neg_int():
    """make sure increment works for negative intergers"""
    x0 = -1
    y0 = ld.increment(x0)
    assert y0 == 0


def test_increment_neg_float():
    """works for negative floats"""
    x0 = -1.5
    y0 = ld.increment(x0) # -0.5
    assert y0 == -0.5


def test_colors():
    """tets that COLORS contains correct items"""
    assert "Cyan" in ld.COLORS
    assert "Mauve" in ld.COLORS
    assert "Blue" in ld.COLORS
    assert "Brown" not in ld.COLORS
    assert "Yellow" not in ld.COLORS


def   test_number():
    """Test the number of elements in COLORS"""
    assert len(ld.COLORS) == 4


# test oop_examples
user1 = ld.oop_example.SocialMediaUser(name= 'Nick', location= 'Arizona')
user2 = ld.oop_example.SocialMediaUser(name= 'Carl', location= 'Costa Rica', upvotes= 250)


def test_SMU_constructor():
    """test name works properly"""
    # test name
    assert user1.name.lower() == 'nick'
    assert user2.name.lower() == 'carl'
    # test location
    assert user1.location.lower() == 'arizona'
    assert user2.location.lower() == 'costa rica'
    # test upvotes
    assert user1.upvotes == 0 # checks default
    assert user2.upvotes == 250


def test_unpopular():
    """test to make sure 0 upvotes is unpopular"""
    assert isinstance(user1.is_popular(), bool)
    assert not user1.is_popular()

def test_popular():
    """test to make sure 250 upvotes is popular"""
    assert isinstance(user1.is_popular(), bool)
    assert user2.is_popular()


def test_SMU_constructor_types():
    assert isinstance(user1.name, str)
    assert isinstance(user1.location, str)
    assert isinstance(user1.upvotes, int)
