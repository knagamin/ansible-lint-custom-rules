import unittest
import ansiblelint
from rules import TaskHasInvalidName


class TestTaskHasValidName(unittest.TestCase):
    rules = ansiblelint.RulesCollection()
    rules.register(TaskHasInvalidName.TaskHasInvalidName())

    def test_success(self):
        with open("tests/task_has_invalid_name_failure.yml") as fobj:
            runner = ansiblelint.Runner(self.rules, fobj.name, [], [], [])
            result = runner.run()
            self.assertTrue(len(result) > 0, result)
