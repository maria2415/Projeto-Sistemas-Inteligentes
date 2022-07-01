## si27s-project

### virtualenv setup

```
virtualenv venv
source venv/bin/activate  # if on linux / macOS
.venv\Scripts\activate    # if on windows
```

### requirements setup

```
(venv) pip install -U pip setuptools wheel
(venv) pip install -U spacy
(venv) python -m spacy download pt_core_news_md # portuguese
```
