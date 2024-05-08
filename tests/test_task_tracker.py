import pytest
from lib.task_tracker import *

"""
Given an empty string
#task_tracker raises exception
"""
def test_no_task_given():
    task_tracker = TaskTracker()
    with pytest.raises(Exception) as e:
        task_tracker.add_task("")
    error = str(e.value)
    assert error == "No task has been set"
    task_tracker.full_task_list() # raises an error with the message "No task has been set"

"""
Given one task
#task_tracker returns the task
"""
def test_with_one_task():
    task_tracker = TaskTracker()
    task_tracker.add_task("Feed Milo")
    result = task_tracker.full_task_list()
    assert result == ["Feed Milo"]

"""
Given multiple tasks
#task_tracker returns the tasks
"""
def test_with_multiple_tasks_given():
    task_tracker = TaskTracker()
    task_tracker.add_task("Feed Milo")
    task_tracker.add_task("Cut the grass")
    task_tracker.add_task("Take the bins out")
    result = task_tracker.full_task_list()
    assert result == ["Feed Milo", "Cut the grass", "Take the bins out"]

"""

