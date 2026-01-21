from scrapper import Scrapper
from parser import Parser


def main():
    url = "https://www.prospektmaschine.de/hypermarkte/"
    container_selector = "div.row.row-flex"

    # 1. Scraper stiahne stránku a vráti container
    scrapper = Scrapper(url, container_selector)
    container = scrapper.get_container()
    print("1.")

    # 2. Parser rozbije container na karty s udajmi
    parser = Parser()
    brochure_cards = parser.parse_container_to_cards(container)
    print("2.")

    #3 Z každej karty vytiahne udaje
    if brochure_cards is None:
        print("Nenašli sa žiadne brožúry.")
        return
    
    for div in brochure_cards:
        title = parser.parse_title(div)
        thumbnail = parser.parse_thumbnail(div)
        valid_from = parser.parse_valid_from(div)
        valid_to = parser.parse_valid_to(div)

        print(f"Title: {title}")
        print(f"Thumbnail: {thumbnail}")
        print(f"Valid From: {valid_from}")
        print(f"Valid To: {valid_to}")
        print("-" * 40)
        
    print("3.")
    
if __name__ == "__main__":
    main()





