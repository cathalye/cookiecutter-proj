msg = """

        \   /
         .-.
     -- (   ) --
         `-´
        /   \

           /\
          /  \
         / /\ \
        / /  \ \
     /\/_/____\_\
    /  \      /  \
   / /\ \    / /\ \
  / /  \ \  / /  \ \

If you have not done so already, create a conda environment for your new
project with:

cd {{cookiecutter.project_slug}}
conda create --name {{cookiecutter.project_slug}} python=3.12
conda activate {{cookiecutter.project_slug}}
conda env export > environment.yml

Install your new project in your local conda environment with:

pip install -e .

########################################################

Don't forget to sync to GitHub:

git init .

Create an empty github repository "{{cookiecutter.project_slug}}" with no readme

git remote add origin https://github.com/username/{{cookiecutter.project_slug}}.git

You will need to manually add data to .gitignore to prevent it from syncing to
version control.

"""
