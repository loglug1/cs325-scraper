from modules import scraper
from modules import fileIO
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--in", "-i", dest="file_in", type=str, help="Path to file with a url on each line to scrape and output to file.", required=True)
    parser.add_argument("--out", "-o", dest="file_out", default=".", type=str, help="Directory to save scraped articles in.", required=False)
    args = parser.parse_args()

    urls = fileIO.get_line_list(args.file_in)
    for url in urls:
        source = scraper.get_source(url)
        title = scraper.get_cnn_title(source)
        article = scraper.get_cnn_article(source)
        filename = args.file_out + "/" + title.replace(" ", "_") + ".txt"
        if filename != args.file_out + "/.txt":
            fileIO.write_file(filename, article)

if __name__=="__main__":
    main()