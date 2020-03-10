import re
from ansiblelint import AnsibleLintRule
from rules.lib.utils import RuleConfigLoader


class TaskHasInvalidName(AnsibleLintRule):
    # These are Default Values
    id = None
    tags = None
    shortdesc = None
    description = None

    def __init__(self):
        # Override variables if options are defined in external file
        self.rcl = RuleConfigLoader(self.__class__.__name__)
        self.rcl.load_config()
        self.rcl.set_metainfo_to_rule(self)

    def matchtask(self, file, task):
        return self.has_invalid_name(file, task)

    def is_invalid_task_name(self, task_name):
        return re.match(self.rcl.get_config('valid_pattern'), task_name) is None

    def has_invalid_name(self, _file, task):
        if 'name' in task:
            return self.is_invalid_task_name(task["name"])

        return False
