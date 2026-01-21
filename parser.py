class Parser:
    def parse_container_to_cards(self, container):
        return container.select(
            "div.brochure-thumb.col-xs-6.col-sm-3"
        )
    
    def parse_title(self, div):
        title_tag = div.select_one("h3.brochure-title")
        return title_tag.text.strip() if title_tag else None
    
    def parse_thumbnail(self, div):
        img_tag = div.select_one("img.brochure-image")
        return img_tag['src'] if img_tag and 'src' in img_tag.attrs else None
    
    def parse_valid_from(self, div):
        valid_from_tag = div.select_one("span.valid-from")
        return valid_from_tag.text.strip() if valid_from_tag else None
    
    def parse_valid_to(self, div):
        valid_to_tag = div.select_one("span.valid-to")
        return valid_to_tag.text.strip() if valid_to_tag else None

