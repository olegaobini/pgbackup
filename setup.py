# from importlib_metadata import entry_points
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pgbackuptool",
    version="0.0.1",
    author="Olega Obini",
    author_email="obiniolega@gmail.com",
    description="A Command Line Backup Tool Buit In Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/olegaobini/pgbackup",
    project_urls={
        "Bug Tracker": "https://github.com/olegaobini/pgbackup/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages("src"),
    python_requires=">=3.6",
    install_requires=["boto3"],
    entry_points={
        'console_scripts': [
            'pgbackup=pgbackup.cli:main'
        ]},
)
