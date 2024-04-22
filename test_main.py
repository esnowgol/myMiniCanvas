from main import app,CourseManager
import main
from fastapi.testclient import TestClient
from user import UserManager
#from course import CourseManager
import pytest


client = TestClient(app)

@pytest.fixture
def courseManager():
    return CourseManager()

@pytest.fixture
def userManager():
    return UserManager()

def test_weclome():
    response = client.get("/")
    assert(response.status_code == 200);
    assert(response.text == "\"Welcome to our miniCanvas!\"")

from unittest.mock import patch
@patch('builtins.print')
def test_post_a_course(mock_print, courseManager):
    classes = main.coursemanager.counter
    response = client.post("/courses/Cosc101?semester=fall",json=[1])
    #course_id, course_code, semester, teacher_list
    mock_print.assert_called_with("ID: " + str(1) + ", name: John, type: student")
    assert(response.status_code == 200)
    assert(main.coursemanager.counter == classes+1)
    assert(response.text == str(classes+1))
    assert(main.coursemanager.course_list[len(main.coursemanager.course_list)-1].course_code == "Cosc101")
    assert(main.coursemanager.course_list[len(main.coursemanager.course_list)-1].semester == "fall")

@patch('builtins.print')
def test_import_students(mock_print, courseManager):
    classes = main.coursemanager.counter
    response = client.put("/courses/1/students",json=[1])
    #, "teacher_id_list": [101, 102]
    mock_print.assert_called_with(True)
    #mock_print.assert_called_with("target id:" + str(1))
    #mock_print.assert_called_with("True")
    assert(response.status_code == 200)
    