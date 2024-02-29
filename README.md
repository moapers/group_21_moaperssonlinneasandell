# Example project for the final project of the EEN060/EEN065 courses

Example of the final project of EEN060/EEN065 courses.

## Installing dependencies

```
pip install flask gunicorn matplotlib python-dotenv redis types-redis pytest coverage toml flake8 requests mypy pylint types-requests isort black lorem-text bs4 pep8-naming
```


## Files to be modified

Here is list of the files that you will need to change:
- [models.py](codeapp/models.py): file where you should create your dataclass.
- [utils.py](codeapp/utils.py): file responsible for downloading the dataset and extracting the statistics.
- [routes.py](codeapp/routes.py): file responsible for serving the web page and the plot.
- [home.html](codeapp/templates/home.html): file where you should create a table with the statistics.
- [about.html](codeapp/templates/about.html): file where you should add your names and the objective of your project.
- [base.html](codeapp/templates/base.html): file where you should put your names in the copyright.


## Sequence of steps

Here is the recommended sequence of steps that you need to follow to complete your final project:

1. Setup your database configuration
  - Create a new file called `.env` and copy the content of the [.env_example](.env_example) into it.
  - Set your DB number and password in the newly created [.env](.env) file.
  - Run `pytest -k database` to test if the connection is successful. You should see a green message with *1 passed*.
2. Create the class that models the object of your database in the file [models.py](codeapp/models.py).
  - Note that this class needs to be a `dataclass`.
  - To test if this step is correct, run `pytest -k models`. You should see a green message with *1 passed*.
3. Populate the [utils.py](codeapp/utils.py) with the correct code to obtain and save the dataset.
  - To test if this step is correct, run `pytest -k data_list`.
4. Create the routes for the web services by implementing the functions `get_json_dataset` and `get_json_stats` in the [routes.py](codeapp/routes.py) file.
5. Implement the route for the web page.
  - Start with the table by implementing the route `home` in the [routes.py](codeapp/routes.py) file.
  - Implement the visualization code for the table in the [home.html](codeapp/templates/home.html). To test this step, run `pytest -k html`.
  - Implement your about page [about.html](codeapp/templates/about.html) and [base.html](codeapp/templates/base.html). If your name has special characters, check [this page](https://usefulwebtool.com/characters-swedish). To test this step, run `pytest -k html`.
  - Implement the `image` route in the [routes.py](codeapp/routes.py) file. To test this part, run `pytest -k image`.


## Useful links and commands

### Pick the color for your project

You can get the HEX code for the colors in your plot through this Google tool:
https://g.co/kgs/ydsBD9

### Running your project

In order to run your project, you should open a terminal and type the following command:

`python manage.py run`

Alternatively, you can run it by going to the *Run and Debug* tab (CTRL/CMD+SHIFT+D) and *start debugging* (F5).

### Validating your entire project

To validate your project, you can run in the terminal the following command.

For MS Windows:

`.\validate.ps1`

For macOS or Linux:

`./validate.sh`

### Running the tests

To run the tests of your project, without running the entire validation suite, you can run in the terminal:

`pytest`

### Fixing HTML errors related to special characters

If you have special characters in your name, use the `Entity Name` column of this webpage: https://usefulwebtool.com/characters-swedish
