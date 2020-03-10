r""" Load and manage external configuration for Ansible Lint Rules
"""

import os
import yaml

CURDIR = os.path.dirname(__file__)
CONFIG_PATH = os.path.join(CURDIR, "..", "..", ".ansible-lint-custom.yml")
DEFAULT_ATTRS = ('id', 'tags', 'shortdesc', 'description')


def load_custom_rule_config(path):
    """ Load external configuration file
    """
    if os.path.exists(path):
        with open(path, "r") as file:
            try:
                config = yaml.safe_load(file)
                return config
            except yaml.YAMLError:
                pass
    return None


class RuleConfigLoader(object):
    """ Load and manage external configuration for Ansible Lint Rules
    """

    config = None

    def __init__(self, rulename, path=CONFIG_PATH):
        self.rulename = rulename
        self.path = path

    def load_config(self):
        """ Load configuration of the rule
        """
        self.config = load_custom_rule_config(self.path)[self.rulename]

    def set_metainfo_to_rule(self, rule):
        """ Set meta information (id, tags, shortdesc, description)
            to a `AnsibleLintRule` object
        """
        for attr in DEFAULT_ATTRS:
            if attr in self.config:
                setattr(rule, attr, self.config[attr])

    def get_config(self, key=None):
        """ Get whole configurations or single one
        :param key: a specific configuration
        """
        return self.config[key] if key else self.config
