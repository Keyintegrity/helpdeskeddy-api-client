import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="helpdeskeddy-api-client",
    version="0.0.2",
    author="devxplorer",
    author_email="devxplorer@gmail.com",
    description="Simple HelpDeskEddy api client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests>=2.22.0"
    ],
)
