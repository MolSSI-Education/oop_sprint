import pytest
from student import Student, GradStudent, UndergradStudent


# can't create an instance of Student class if it has any @abstractmethod
# s = Student(name='Doaa', ID='453535', GPA=2.3, status='Grad')  # Raise error

# Those are okay
s1 = GradStudent(name='Joe Smith', ID='453535', GPA=2.7)
s2 = UndergradStudent(name='Sally Smith', ID='453535', GPA=2.7)


def test_name():
    assert s1.name == 'Joe Smith'
    assert s2.name == 'Sally Smith'
    # assert s.name == 'Doaa'


def test_GPA():
    assert s1.get_GPA() == 2.7
    assert s2.get_GPA() == 2.7
    # assert s.get_GPA() == 2.3


def test_pass():
    assert not s1.is_pass()
    assert s2.is_pass()


def test_advisor():
    advisor = 'Shaffer'
    s1.set_advisor(advisor)
    assert s1.get_advisor() == advisor


def test_ID():
    with pytest.raises(AttributeError):
        id = s1.__ID()
