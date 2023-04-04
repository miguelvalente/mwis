# Maximum Weight Independent Set 🦁🐗🦓

This project is an implementation of the Maximum Weight Independent Set problem for trees in Python. A live demo of the project can be accessed through Streamlit [here](https://miguelvalente-mwis-mwisapphome-xxwek5.streamlit.app). You can upload your own JSON so as long as you follow the following strcture [JSON format example](https://github.com/miguelvalente/mwis/blob/master/mwis/tests/example.json).


## Run on CLI
To run the program locally you need to install its dependencies

### Install
1. Install [Poetry](https://python-poetry.org/docs/#installation)
2. Clone the repository
3. Run `poetry install` in the root folder
4. Run `poetry shell` to open a shell with the environment activated

### Run 

If you run on CLI the root of the tree is included by default. To remove that behaviour pass the argument `--no-include-king`. Complete details obtain by using the `--help` flag.


```bash
python mwis/main.py /path/to/json.json --no-include-king
```
```bash
python mwis/main.py --help
```

__Run the example case__
```bash
`python mwis/main.py mwis/tests/example.json`
```