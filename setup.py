from setuptools import setup, find_packages

setup(
    name="location",
    version="1.1",
    packages=find_packages(),
    description="A custom Location data type for handling latitude, longitude, and altitude.",
    author="David",
    author_email="dcortes@nexmachina.com",
    url="https://github.com/DcortesNexmachina/LocationDataType.git",  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
