from setuptools import setup, find_packages

setup(
        name = "headlines",
        version = "0.1",
        description = "Learn flask",
        packages = find_packages(),
        install_requires = ["flask", "feedparser"],
        )
