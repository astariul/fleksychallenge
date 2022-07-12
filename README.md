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

### Prepare the dataset

To prepare the dataset, just run :

```bash
fleksychallenge prepare
```

It will download the dataset, preprocess it, and save the preprocessed data files locally.

---

By default, files are saved under the folder `tweet_dataset`, but you can change that behavior with the `--dataset` argument. For example:

```bash
fleksychallenge prepare --dataset ../my/folder
```

### Train

Once the dataset is ready, you can start training the model with :

```bash
fleksychallenge train
```

It will train the model and save it under `sentiment_model` by default.

---

By default the model is trained on GPU. If you would like to train on CPU instead, you can specify the `--cpu` argument :

```bash
fleksychallenge train --cpu
```

---

You can change where to save the model by specifying the `--model` argument. For example :

```bash
fleksychallenge train --model my_model
```

---

If you preprocessed your dataset in a different folder, you must specify the location with the `--dataset` argument (similarly to the `prepare` command):

```bash
fleksychallenge train --dataset ../my/folder
```

---

A default configuration file is provided for training. You can also generate your own configuration file for training. To do this, head over to [Spacy documentation](https://spacy.io/usage/training#quickstart) and copy-paste the generated config in a file called `base_config.cfg`.

Then, run :

```bash
python -m spacy init fill-config ./base_config.cfg ./config.cfg
```

It will save the full config file at `config.cfg`.

Once your config file is generated, you can launch the training with :

```bash
fleksychallenge train --config config.cfg
```

### Test

After training your model, you should test it ! You can do that with :

```bash
fleksychallenge test
```

It will load your trained model and compute several metrics (accuracy, precision, recall, F-1 score).

If you have to pick a single metric for comparing different models, you should pick Recall (as advised in [the original paper of TweetEval](https://arxiv.org/pdf/2010.12421.pdf))

---

As before, you can specify a different dataset to use for testing with the `--dataset` argument, or a different model to load with the `--model` argument.

Also, the test set of TweetEval is quite big (+12k samples), so by default the testing script will only evaluate the model on the first 100 samples. You can change this behavior by specifying the `--full` argument :

```bash
fleksychallenge test --full
```


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
