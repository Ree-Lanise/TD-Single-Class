class TaskTracker():
    def __init__(self):
        self._task = []

    def add_task(self, task):
        if task == "":
            raise Exception("No task has been set")
        self._task.append(task)

    def full_task_list(self):
        return self._task

    def mark_if_complete(self):
        pass

    def remove_when_complete(self):
        pass
