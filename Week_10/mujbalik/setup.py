from setuptools import setup, find_packages

setup(
    name='mujbalik',
    version='1.0.0',
    packages=find_packages(),
    install_requires=['pytest']  # potřebujeme akorát pytest pro unit testy
)
