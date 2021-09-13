"# protei_autotests" 
## Creating Virtual Environments
```
python -m venv protei-env
```
Run 
```
protei-env\Scripts\activate.bat
```
Install all the necessary packages from requirements.txt file
```
python -m pip install -r requirements.txt
```
## Run tests
### all tests
```
pytest -v -s tests.py
```
### login tests
```
pytest -v -s -m login_tests tests.py
```
### input tests
```
pytest -v -s -m input_tests tests.py
```
