from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='UTT-WORKSHOP-PROJECT-pkg-anderson05',
    version='0.0.1',
    description='utt-workshop git',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='utt-g4',
    author_email="wachenguessi@gmail.com",
    url="https://github.com/charx6/utt-workshop3.git",
    project_urls={
        "Bug Tracker": "https://github.com/LacErnest/Bicash-Mobile-App/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    packages=find_packages(),
    license='MIT',
)
