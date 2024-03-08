from module_1.scraper import CNNScraper
from module_2 import fileIO
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--in", "-i", dest="file_in", type=str, help="Path to file with a url on each line to scrape and output to file.", required=True)
    parser.add_argument("--out", "-o", dest="file_out", default="Data/processed", type=str, help="Directory to save scraped articles in.", required=False) # Defaults to the project defined output location
    args = parser.parse_args()

    urls = fileIO.get_line_list(args.file_in)
    for url in urls:
        scraper = CNNScraper(url) #This uses the CNN scraper. You can implement the Scraper interface with another class and change just this line for another news site
        title = scraper.get_title()
        article = scraper.get_article()
        filename = args.file_out + "/" + title.replace(" ", "_") + ".txt"
        if filename != args.file_out + "/.txt":
            fileIO.write_file(filename, article)

if __name__=="__main__":
    main()