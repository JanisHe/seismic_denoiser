import os
from setuptools import setup

AUTHORS = ('Janis Heuel'),

setup(
    name='seismic denoiser',
    version='0.0.1',
    author=AUTHORS,
    author_email='janis.heuel@ruhr-uni-bochum.de',
    description=('Denoising Autoencoder to remove noise from seismic  data'),
    license=' GNU General Public License (version 3 or higher)',
    url='',
    packages=[],
    install_requires=[],
    python_requires='>=3',
    long_description='README.md',
    keywords=[],
    classifiers=[
        'Development Status :',
        'License :: GNU General Public License (version 3 or higher)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent, but only tested on Ubuntu and Debian',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic ::',
        'Intended Audience :: Science/Research'
    ],
)


# Clone package PyCWT from GitHub
os.system("git clone https://github.com/regeirk/pycwt.git")

# Run Setup file of PyCWT
os.chdir('pycwt/')
os.system('python setup.py install')
# Create an empty file __init__.py in the pycwt directory, otherwise the package will not be recognised correctly.
f_init = open("__init__.py", "w")
f_init.close()

print("\n" + "#" * 20)
print("To train your first model run 'python run_model_from_parfile.py ./model_parfile' from the command line.")
print("A model is trained from the example dataset. Change the parfile to train your first own model.")
print("#" * 20 + "\n")
