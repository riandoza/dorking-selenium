# Python Selenium Search Engine

## Introduction

This is a simple python script that uses selenium to search for keywords on google and save the results in a csv file. The script can be used as a starting point for scraping data from websites using selenium. It's designed to be easy to use and customize, but it's also flexible enough to suit any specific needs.

## Requirements

To run this script, you will need to have the following installed:

- Python 3.x
- selenium
- csv
- chromedriver (will automatically download at first time if isn't available)

You can install these using pip:

```
pip install -r requirements.txt
```

## Usage

To use this script, simply run the following command:

```
python main.py -i input.txt
```

where `input.txt` is the text file containing the keywords to search for.
This will search for the keyword on google and save the results in a `output/google.csv` file. You can customize the output file name and other options by editing the code.
