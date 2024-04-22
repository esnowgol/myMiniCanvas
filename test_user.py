import pytest
from user import UserManager,User

@pytest.fixture
def userManager():
    return UserManager()

@pytest.fixture
def user():
    return User(5, "Steve", "pwd", "Admin")

def test_generate_id(userManager):
    a = userManager.generate_id()
    b = userManager.generate_id()
    assert(a+1 == b)

def test_create_a_user(userManager):
    length = len(userManager.user_list)
    userManager.create_a_user("Steve", "pwd", "Admin")

    assert(length+1 == len(userManager.user_list))
    assert(type(userManager.user_list[len(userManager.user_list)-1]) is User)


def test_find_a_user(userManager):
    userManager.create_a_user("Jeff", "myPass", "Student")
    users = userManager.find_users([userManager.counter])
    assert(len(users) > 0)