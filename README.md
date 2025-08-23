# Ice Breaker
Project set up:

Clone repository with specific SSH key:
```bash
git clone -c "core.sshCommand=ssh -i ~/.ssh/key_name" ssh_url
```

Install pipenv if you don't have it:
```bash
pip install pipenv or brew install pipenv
```
To synchronize your environment with the Pipfile.lock, run:
```bash
pipenv sync
```
To activate the virtual environment, run:
```bash
pipenv shell
```
From Pipfile (for initial setup or when Pipfile.lock is not present): If you are setting up a new project or want Pipenv to resolve and install the latest compatible versions based on your Pipfile:
```bash
pipenv install
```