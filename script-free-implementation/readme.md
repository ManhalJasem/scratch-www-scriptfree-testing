Artifacts for "Web Element Identification by Combining NLP and Heuristic Search for Web Testing" presented in SANER2022.

# Preparation

- Install chromedriver: In execute `./install-chrome.sh`
- Download fastText model with subword from [here](https://fasttext.cc/docs/en/english-vectors.html) or [here](https://github.com/facebookresearch/fastText/issues/656) or [here](https://github.com/facebookresearch/fastText/issues/656).
- Put the model in the  `./data/wiki-news-300d-1M-subword.bin`
- Put test case in `./test_cases_metamask_experiment`
- Specify target test cases via `./src/Setting.py`

These directory names can be changed via `./src/Setting.py`

# Build

`pipenv install`

# Run

`pipenv run gen`
