import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


reqs = []

extras_require = {
    "hook": ["pre-commit~=2.15"],
    "lint": ["isort~=5.9", "black~=22.1", "flake518~=1.2", "darglint~=1.8"],
}
extras_require["all"] = sum(extras_require.values(), [])

setuptools.setup(
    name="fleksychallenge",
    version="1.0.0.dev0",
    author="Nicolas REMOND",
    author_email="remondnicola@gmail.com",
    description="Part 1 of the Fleksy NLP challenge",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/astariul/fleksychallenge",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=reqs,
    extras_require=extras_require,
)
