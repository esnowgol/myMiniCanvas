import pytest
from course import CourseManager, Course
from assignment import Assignment, Submission

@pytest.fixture
def assignment():
    return Assignment("50", "1/1/3000", 50)

@pytest.fixture
def submission(assignment):
    return Submission("12", "foo")

def test_submit_assignment(submission, assignment):
    currentSubmissions = len(assignment.submission_list)
    assignment.submit(submission)

    assert(currentSubmissions + 1 == len(assignment.submission_list))
    assert(submission.student_id == "12")
    assert(submission.submission == "foo")
    assert(assignment.assignment_id == "50")
    assert(assignment.due_date == "1/1/3000")
    assert(assignment.course_id == 50)