import pytest
from course import CourseManager, Course
from assignment import Assignment

@pytest.fixture
def courseManager():
    return CourseManager()

@pytest.fixture
def course(courseManager):
    return Course(courseManager.generate_id(), "Cosc381", "Winter 2024", [3,4])


def test_create_a_course(courseManager):
    #Arrange
    #Act
    courseID = courseManager.create_a_course("100", "winter", [1, 2, 3])
    #Assert
    assert(courseID != None)
    assert(type(courseID) is int)

def test_find_a_course(courseManager):
    #Arrange
    #Act
    courseID = courseManager.create_a_course("105", "fall", [1, 2])
    course = courseManager.find_a_course(courseID)
    #Assert
    assert(course != None)
    assert(type(course) is Course)
    assert(course.course_code == "105")
    assert(course.semester == "fall")
    assert(course.teacher_list == [1,2])

def test_generate_id(courseManager):
    a = courseManager.generate_id()
    b = courseManager.generate_id()
    assert(a+1 == b)

def test_import_studets(course):
    course.import_students(["Steve", "Jeff", "Stephen", "Jefferson"])
    assert(course.student_list == ["Steve", "Jeff", "Stephen", "Jefferson"])

def test_create_an_assignment(course):
    currentAssignments = len(course.assignment_list)
    course.create_an_assignment("5/15/2024")

    assert(currentAssignments + 1 == len(course.assignment_list))
    assert(type(course.assignment_list[len(course.assignment_list)-1]) is Assignment)
    assert(course.assignment_list[len(course.assignment_list)-1].due_date == "5/15/2024")

def test_generate_assignment_id(course):
    a = course.generate_assignment_id()
    b = course.generate_assignment_id()
    assert(a+1 == b)