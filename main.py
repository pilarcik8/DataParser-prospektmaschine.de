import json

from scraper import Scraper
from parser import Parser
from datetime import datetime
from cataloge import Cataloge

def main():
    url = "https://www.prospektmaschine.de/hypermarkte/"
    container_selector = "div.row.row-flex"

    # 1. Scraper stiahne stránku a vráti container
    scraper = Scraper(url, container_selector)
    container = scraper.get_container()

    # 2. Parser rozbije container na karty s udajmi
    parser = Parser()
    brochure_cards = parser.parse_container_to_cards(container)

    #3 Z každej karty vytiahne udaje
    if brochure_cards is None:
        print("Nenašli sa žiadne brožúry.")
        return
    
    catalogs = []

    for card in brochure_cards:
        title = parser.parse_title(card)
        thumbnail = parser.parse_thumbnail(card)

        detail_url = parser.parse_detail_url(card)
        shop_name = parser.parse_shop_name_from_url(detail_url)

        valid_from, valid_to = parser.parse_valid_dates_usa(card)
        parsed_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        catalog = Cataloge(
            title_param=title,
            thumbnail_param=thumbnail,
            shop_name_param=shop_name,
            valid_from_param=valid_from,
            valid_to_param=valid_to,
            parsed_time_param=parsed_time
        )
        catalogs.append(catalog)

    #4 Uložíme do JSON súboru
    data_for_json = [c.to_dict() for c in catalogs]

    with open("catalogs.json", "w", encoding="utf-8") as f:
        json.dump(data_for_json, f, ensure_ascii=False, indent=4)

    print("Uložené do catalogs.json")

if __name__ == "__main__":
    main()





