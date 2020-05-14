import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="ieugwaspy",
    version="0.1.7",
    author="Tom Gaunt",
    author_email="tom@biocompute.org.uk",
    description="Python interface to IEU GWAS database API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://mrcieu.github.io/ieugwaspy/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["requests"],
)
