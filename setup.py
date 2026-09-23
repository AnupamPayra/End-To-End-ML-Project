from setuptools import find_packages, setup
from typing import List


HYPHEN_E_DOT = '-e .'
def get_requirements(fie_path : str)-> List[str]: # This function will return the list of requirements
    requirements = []
    with open(fie_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements: # in requirement.txt file '-e .' exist. it remove it while it occure during acssesing the requirement.txt
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name="mlprojects",
    version='0.0.1',
    author="Anupam Payra",
    author_email="anupampayra5@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)