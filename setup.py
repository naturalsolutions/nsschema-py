import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="renecovalidator",
    version="0.0.1",
    author="Natural Solutions",
    author_email="author@example.com",
    description="Reneco Validator package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    install_requires=[
        'jsonschema>2.6.0'
    ],
    dependency_links=['git+https://github.com/Julian/jsonschema.git@master#egg=jsonschema-3.0.0'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)