from ansiblelint import AnsibleLintRule
from rules.lib.utils import load_custom_rule_options
import re


class TaskHasInvalidName(AnsibleLintRule):
    # These are Default Values
    id = None
    description = None
    tags = None
    opts = None

    def __init__(self):
        # Override variables if options are defined in external file
        self.opts = load_custom_rule_options(self.__class__.__name__)
        try:
            self.id = self.opts['id']
            self.shortdesc = self.opts['shortdesc']
            self.description = self.opts['description']
            self.shortdesc = self.opts['shortdesc']
            self.tags = self.opts['tags']
        except KeyError:
            pass

    def matchtask(self, file, task):
        return self.has_invalid_name(file, task)

    def is_invalid_task_name(self, task_name):
        return re.match(self.opts['valid_pattern'], task_name) is None

    def has_invalid_name(self, _file, task):
        if 'name' in task:
            return self.is_invalid_task_name(task["name"])

        return False
