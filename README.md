# DabioHome
Custom webserver with home page for all my needs

---
###Simple notes for pipenv

Using the pipenv will subsitute the need for a virtual environment, make sure you have pipenv installed globally.
You can then run the below and it will automagically create the necessary files.

```bash
pipenv install flask    # this will create the pipfile and pipfile.lock for you
pipenv shell            # Will start the shell so all packages are available for you within the pip file
pipenv run              # Will run your code if you have not run the shell command
```