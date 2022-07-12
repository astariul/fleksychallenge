<h1 align="center">fleksychallenge</h1>
<p align="center">
Part 1 of the Fleksy NLP challenge
</p>

<p align="center">
    <a href="https://github.com/astariul/pytere/releases"><img src="https://img.shields.io/github/release/astariul/pytere.svg" alt="GitHub release" /></a>
    <a href="https://github.com/astariul/pytere/actions/workflows/pytest.yaml"><img src="https://github.com/astariul/pytere/actions/workflows/pytest.yaml/badge.svg" alt="Test status" /></a>
    <a href="https://github.com/astariul/pytere/actions/workflows/lint.yaml"><img src="https://github.com/astariul/pytere/actions/workflows/lint.yaml/badge.svg" alt="Lint status" /></a>
    <img src=".github/badges/coverage.svg" alt="Coverage status" />
    <a href="https://astariul.github.io/pytere"><img src="https://img.shields.io/website?down_message=failing&label=docs&up_color=green&up_message=passing&url=https%3A%2F%2Fastariul.github.io%2Fpytere" alt="Docs" /></a>
    <br>
    <a href="https://pycqa.github.io/isort/"><img src="https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat" alt="isort" /></a>
    <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="black" /></a>
    <a href="https://github.com/PyCQA/flake8"><img src="https://img.shields.io/badge/code%20style-flake8-blue" alt="flake8" /></a>
    <a href="https://github.com/terrencepreilly/darglint"><img src="https://img.shields.io/badge/docstrings-darglint-blue" alt="darglint" /></a>
    <a href="https://github.com/pre-commit/pre-commit"><img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white" alt="pre-commit"></a>
    <a href="https://github.com/astariul/pytere/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="licence" /></a>
</p>

<p align="center">
  <a href="#description">Description</a> •
  <a href="#install">Install</a> •
  <a href="#usage">Usage</a> •
  <a href="#contribute">Contribute</a>
</p>


<h2 align="center">Description</h2>

This is my implementation for the Fleksy NLP challenge (part 1).

The goal of this repository is to provide an interface to :

* Retrieve and clean a Twitter dataset, for sentiment analysis
* Train a sentiment analysis model using `Scikit-learn` or `Spacy` and following best practices for the metrics (for ranking the model against other SOTA models)


<h2 align="center">Install</h2>

Install the package with :


```
pip install fleksychallenge
```

---

For development, you can install it locally by first cloning the repository :

```
git clone https://github.com/astariul/fleksychallenge.git
cd fleksychallenge
pip install -e .
```


<h2 align="center">Usage</h2>

TODO


<h2 align="center">Contribute</h2>

To contribute, install the package locally, create your own branch, add your code, and open a PR !

### Pre-commit hooks

Pre-commit hooks are set to check the code added whenever you commit something.

If you never ran the hooks before, install it with :

```bash
pre-commit install
```

---

Then you can just try to commit your code. If you code does not meet the quality required by linters, it will not be committed. You can just fix your code and try to commit again !

---

You can manually run the pre-commit hooks with :

```bash
pre-commit run --all-files
```
