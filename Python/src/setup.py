from pathlib import Path
from setuptools import setup, find_packages, Extension
import os
import shutil

name = 'cuvis'

REQUIREMENTS = {
    # Installation script (this file) dependencies
    'setup': [
        'setuptools_scm',
    ],
    # Installation dependencies
    # Use with pip install . to install from source
    'install': [
        'Cpython',
        'setuptools < 64',
        'numpy >= 1.23',
        'matplotlib',
        'DateTime',
        'psutil',
        'xarray',
        'PyYAML',
        'scipy',
        'tqdm',
        'ipython',
        'ipywidgets',
        'ipyfilechooser',
        'notebook',
        'PySimpleGui',
        'opencv-python',
        'scikit-learn',
        'dill',
    ],
}

lib_dir = ""
if 'CUVIS' in os.environ:
    lib_dir = os.getenv('CUVIS')
    print('CUVIS SDK found at {}!'.format(lib_dir))
else:
    Exception('CUVIS SDK does not seem to exist on this machine! Make sure that the environment variable CUVIS is set.')


def __createManifest__(subdirs):
    """inventory all files in path and create a manifest file"""
    current = os.path.dirname(__file__)
    relative_paths = [os.path.relpath(path, current) for path in subdirs]
    with open(os.path.join(current, "MANIFEST.in"), "w") as manifest:
        manifest.writelines("recursive-include {} *.pyd".format(" ".join(relative_paths)))


add_il = os.path.join(os.path.dirname(__file__), "cuvis")

__createManifest__([add_il])

setup(
    name=name,
    python_requires='>= 3.9',
    version='0.1',
    packages=find_packages(),
    url='https://www.cubert-hyperspectral.com/',
    license='',
    author='Ben Mueller @ Cubert GmbH, Ulm, Germany',
    author_email='mueller@cubert-gmbh.com',
    description='CUVIS Python SDK. Linked to the cuvis installation at {}.'.format(lib_dir),
    setup_requires=REQUIREMENTS['setup'],
    install_requires=REQUIREMENTS['install'],
    include_package_data=True,
)
