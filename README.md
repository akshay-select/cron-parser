# Cron Expression Parser

## Overview

This project provides a Python-based cron expression parser that allows users to interpret and validate cron expressions. Cron expressions are used to schedule jobs in Unix-like operating systems, specifying the exact time and date when a command should be executed.

## Features

- Parse and validate cron expressions.
- Support for standard cron fields: minute, hour, day of month, month, day of week, and command.
- Displays a expanded schedule in a table format! 

## Installation

Clone the repository:

```sh 
git clone https://github.com/akshay-select/cron-parser.git
```

## Usage
```sh
cd cron-parser

python3 main.py "cron expression here"
```
Example: 
```sh
python3 main.py "22-30/30 1 2 1-3 1/2 command1"

---------------------------
minute       | [22]
hour         | [1]
day of month | [2]
month        | [1, 2, 3]
day of week  | [1, 3, 5]
command      | command1
---------------------------
```

## Test
Use the below command to run tests! 
```sh
python3 -m unittest discover -s tests             
```

## Possible Improvements
- Error handling can be improved to catch the invalid inputs and provide more details! 
- Error handling can be improved to check for error messages. 
- More tests to be added to cover wide range of scenarios...
- Verify command? 