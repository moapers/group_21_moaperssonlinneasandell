# script that validates if the project code is up to
# the standard proposed in the course

# to be used if you use Windows
# in the PowerShell, run:
# .\validate.ps1

# run flake8
flake8 .
$flake = $?

# run pylint
pylint ./codeapp
$pyl = $?

# run black
black . --check
$blc = $?

# run mypy
mypy .
$mp = $?

# run isort
isort . --check-only --diff
$is = $?

# run tests and code coverage
coverage run -m pytest --log-cli-level="CRITICAL"
$test = $?
coverage report
$cov = $?

# printing output
if ( $flake ) {
    Write-Output "Flake8`t$([char]0x2705)"
} else {
    Write-Output "Flake8`t$([char]0x274c)"
}

if ( $pyl ) {
    Write-Output "Pylint`t$([char]0x2705)"
} else {
    Write-Output "Pylint`t$([char]0x274c)"
}

if ( $blc ) {
    Write-Output "Black`t$([char]0x2705)"
} else {
    Write-Output "Black`t$([char]0x274c)"
}

if ( $mp ) {
    Write-Output "Mypy`t$([char]0x2705)"
} else {
    Write-Output "Mypy`t$([char]0x274c)"
}

if ( $is ) {
    Write-Output "isort`t$([char]0x2705)"
} else {
    Write-Output "isort`t$([char]0x274c)"
}

if ( $test -and $cov ) {
    Write-Output "Tests`t$([char]0x2705)"
} else {
    Write-Output "Tests`t$([char]0x274c)"
}
