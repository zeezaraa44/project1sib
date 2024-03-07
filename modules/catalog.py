from modules.book import Book
from modules.magazine import Magazine
from modules.cd import Cd
from modules.dvd import Dvd


class Catalog():
    def __init__(self, catalog):
        self.catalog = catalog

    def search(self, input_search):
        list_result = []
        for catalog_item in self.catalog:
            for item in catalog_item:
                if input_search.lower() in item.title.lower():
                    if type(item) is Magazine:
                        list_result.append(f'Title: {item.title}, Volume: {item.volume}, Type Catalogue: Magazine')
                    elif type(item) is Book:
                        list_result.append(f'Title: {item.title}, DDS Number: {item.dds_number}, Type Catalogue: Book')
                    elif type(item) is Dvd:
                        list_result.append(f'Title: {item.title}, Directors: {item.directors}, Type Catalogue: Dvd')
                    elif type(item) is Cd:
                        list_result.append(f'Title: {item.title}, Artist: {item.artist}, Type Catalogue: Cd')
        return list_result
