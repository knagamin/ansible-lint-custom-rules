import os
import yaml

CUSTOM_CONFIG_PATH = ".ansible-lint-custom.yml"

def load_custom_rule_options(rulename):
    options = None
    if os.path.exists(CUSTOM_CONFIG_PATH):
        with open(CUSTOM_CONFIG_PATH, "r") as file:
            try:
                options = yaml.safe_load(file)
                return options[rulename]
            except yaml.YAMLError:
                pass
    return None
