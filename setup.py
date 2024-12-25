from setuptools import setup, find_packages

setup(
    name='ColorPalettes',
    version='0.4.0',
    description='A package for pre-defined color palettes',
    author='You Iida',
    author_email='youiida@gmail.com',
    url='https://github.com/youiida/ColorPalettes',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
)