class Cataloge:
    def __init__(
        self,
        title_param,
        thumbnail_param,
        shop_name_param,
        valid_from_param,
        valid_to_param,
        parsed_time_param
    ):
        self.title = title_param
        self.thumbnail = thumbnail_param
        self.shop_name = shop_name_param
        self.valid_from = valid_from_param
        self.valid_to = valid_to_param
        self.parsed_time = parsed_time_param

    def to_dict(self):
        return {
            "title": self.title,
            "thumbnail": self.thumbnail,
            "shop_name": self.shop_name,
            "valid_from": self.valid_from,
            "valid_to": self.valid_to,
            "parsed_time": self.parsed_time,
        }
