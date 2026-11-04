import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'lab02_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
         # Include all launch files.
        (os.path.join('share', package_name, 'launch'), glob('launch/*')),
        # Include all config files.
        (os.path.join('share', package_name, 'config'), glob('config/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Morad Boumasdour, Leonardo Carreras',
    maintainer_email='S364165@studenti.polito.it ,S360909@studenti.polito.it',
    description='Bump and  go Controller',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'controller = lab02_pkg.controller:main',
        ],
    },
)
