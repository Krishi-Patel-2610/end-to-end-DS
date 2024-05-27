from setuptools import setup, find_packages
from typing import List

REQUIREMENTS_PATH = "requirements.txt"
TRIGGER = "-e ."

def get_requirements(file_path : str) -> List[str]:
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if TRIGGER in requirements:
            requirements.remove(TRIGGER)
    return requirements

setup(
    name = 'end-to-end-DS',
    version = '3.8.0',
    author = 'Krishi Patel',
    packages = find_packages(),
    install_requires = get_requirements(REQUIREMENTS_PATH)

)