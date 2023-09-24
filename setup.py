from setuptools import find_packages,setup
from typing import List

def get_requirements(file_name:str)->List[str]:
    requirements=[]
    hypen_e_dot='-e .'
    with open(file_name) as file_obj:
        requirements = file_obj.readlines()
        requirements = [lib_name.replace('\n','') for lib_name in requirements]

        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
        return requirements


setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='naveen',
    author_email='navrathoud@gmail.com',
    install_requires= get_requirements('requirement.txt'),
    packages= find_packages()
)