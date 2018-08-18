import setuptools

with open("README.md", "r") as f:
    long_description = f.read()
    
setuptools.setup(
    name="pycommons",
    version="0.1.0",
    author="Chaoqian Xu",
    author_email="chaoranxu@gmail.com",
    description="Common utilities for python apps.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xuchaoqian/pycommons.git",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    )
) 
