from setuptools import setup, find_packages


setup(
    name="octopus",
    version="0.0.1",
    description="for octopus-lovers <3",
    long_description = "Example for live-editing packages",
    url="https://github.com/atisor73/octopus",
    license="MIT",
    author='Rosita Fu',
    packages=find_packages(),
    install_requires=['numpy'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ]
)