# bookbot

Tutorial project based on the course "Build a local dev environment" from [boot.dev](https://www.boot.dev).

Using Python, main.py will use a `books/book_name` to generate a report of the number of words within the text file as well as character counts for alphabetic characters.

## NOTES

### General

- `export PATH=$PATH:/some/new/directory` | update PATH

```bash
# Linux or WSL (bash)
code ~/.bashrc

# this prints "hello there" to the screen
echo "hello there"
```

- `cd ~/` | change directory to home directory
- `ls` | list all files and folders in the current directory
- `mkdir folder_name` | create a new folder
- `cd folder_name` | navigate to new folder
- `rm name_of_file` | delete file in directory

### Github

#### Create repo

- create project repo on github.com
- from a local folder use git to clone a github.com repo
  - `git clone https://github.com/username/repo_name`

#### Commit changes

- `git add .` | stage the change
- `git commit -m "commit message"` | commit the change locally with comment
- `git push origin main` | push the change to github.com

### Install Python

- `pyenv install -v 3.12.1` | install Python 3.12.1
- `pyenv global 3.12.1` | set version as default
- `python --version` | verify
