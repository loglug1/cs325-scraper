# run this file from the command line
# use --in or -i to specify input file of URLs to scrape (REQUIRED)
# use --out or -o to specify directory to output articles to (Optional, Default: ./Data/processed)

from module_1.scraper import CNNScraper
from module_2.fileIO import FileIO
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--in", "-i", dest="file_in", type=str, help="Path to file with a url on each line to scrape and output to file.", required=True)
    parser.add_argument("--out", "-o", dest="file_out", default="Data/processed", type=str, help="Directory to save scraped articles in.", required=False) # Defaults to the project defined output location
    args = parser.parse_args()

    input_file = FileIO(args.file_in)
    urls = input_file.get_line_list()
    for url in urls:
        scraper = CNNScraper(url) #This uses the CNN scraper. You can implement the Scraper interface with another class and change just this line for another news site
        title = scraper.get_title()
        article = scraper.get_article()
        filename = args.file_out + "/" + title.replace(" ", "_") + ".txt"
        if filename != args.file_out + "/.txt": # skips saving if article title ends up blank
            output_file = FileIO(filename)
            output_file.write_data(article)

if __name__=="__main__":
    main()