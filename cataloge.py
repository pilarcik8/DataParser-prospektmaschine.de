class Cataloge:
    def __init__(self, id_: int):
        self.id = id_

        self._title = None
        self._thumbnail = None
        self._shop_name = None
        self._valid_from = None
        self._valid_to = None
        self._parsed_time = None

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value: str):
        self._title = value.strip()

    @property
    def thumbnail(self):
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, value: str):
        self._thumbnail = value

    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value: str):
        self._shop_name = value.strip()

    @property
    def valid_from(self):
        return self._valid_from

    @valid_from.setter
    def valid_from(self, value):
        self._valid_from = value

    @property
    def valid_to(self):
        return self._valid_to

    @valid_to.setter
    def valid_to(self, value):
        self._valid_to = value

    @property
    def parsed_time(self):
        return self._parsed_time

    @parsed_time.setter
    def parsed_time(self, value):
        self._parsed_time = value

    def to_dict(self):
        return {
            "id": self.id,
            "title": self._title,
            "thumbnail": self._thumbnail,
            "shop_name": self._shop_name,
            "valid_from": self._valid_from,
            "valid_to": self._valid_to,
            "parsed_time": self._parsed_time,
        }
