# script that validates if the project code is up to
# the standard proposed in the course

# to be used if you use Linux or macOS
# in the shell, with your virtual environment activated, run:
# source validate.sh

flake8 .
flake=$?

pylint ./codeapp
pyl=$?

black . --check
blc=$?

mypy .
mp=$?

isort . --check-only --diff
is=$?

coverage run -m pytest --log-cli-level="CRITICAL"
coverage report
cov=$?

# printing output
if [ $flake -eq 0 ]
then
    echo -e "Flake8\t\u2705"
else
    echo -e "Flake8\t\u274c"
fi

if [ $pyl -eq 0 ]
then
    echo -e "Pylint\t\u2705"
else
    echo -e "Pylint\t\u274c"
fi

if [ $blc -eq 0 ]
then
    echo -e "Black\t\u2705"
else
    echo -e "Black\t\u274c"
fi

if [ $mp -eq 0 ]
then
    echo -e "Mypy\t\u2705"
else
    echo -e "Mypy\t\u274c"
fi

if [ $is -eq 0 ]
then
    echo -e "isort\t\u2705"
else
    echo -e "isort\t\u274c"
fi

if [ $cov -eq 0 ]
then
    echo -e "Tests\t\u2705"
else
    echo -e "Tests\t\u274c"
fi
