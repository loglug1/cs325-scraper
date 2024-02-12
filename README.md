# CS325 Project 1: Web Scraper
This is a simple web scraper written in Python using PyQuery and requests. The scraper module has functions built in for scraping CNN articles but has functions that accept jQuery selectors that could be used for other sites.

## Usage
Clone and change directory to the repository by running the following commands

    $ git clone https://github.com/loglug1/cs325-scraper.git
    $ cd cs325-scraper

Import conda environment from requirements.yml using the following command

    $ conda env create -f requirements.yml
    $ conda activate scraper

Run the program

    $ python main.py --in url.in --out output

This example will scrape articles from each site listed in the file `url.in` and export them to txt files inside the `output` directory.