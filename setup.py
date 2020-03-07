import setuptools

setuptools.setup(
        name="ansiblelint_custom_rule_with_opts",
        version="0.0.1",
        description="ansible-lint custom rules with external configuration",
        install_requires=["ansible-lint"],
        packages=setuptools.find_packages(exclude=("tests",)),
)
