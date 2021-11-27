from setuptools import setup

setup(
    name = "basic_stats",
    version = "0.0.1",
    author = "Andrew Sheerin",
    packages=['basic_stats'],
    install_requires=['numpy','scipy.io', 'random', 'matplotlib.pyplot'],
)

