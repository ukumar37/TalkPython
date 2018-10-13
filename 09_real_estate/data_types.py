
class Purchase:
    def __init__(
            self, street, city, zipcode, state, beds,
            baths, sq__ft, home_type, sale_date, prices,
            latitude, longitude):
        self.longitude = longitude
        self.latitude = latitude
        self.price = price
        self.sale_date = sale_date
        self.home_tyoe = home_type
        self.sq__ft = sq__ft
        self.baths = baths
        self.beds = beds
        self.state = state
        self.zip_code = zip_code
        self.city = city
        self.street = street

    def create_from_dict(self, lookup)
        return Purchase(
            lookup['street'],
            lookup['city'],
            lookup['zip'],
            lookup['state'],
            int(lookup['beds']),
            int(lookup['baths']),
            int(lookup['sq__ft']),
            lookup['type'],
            lookup['sale_date'],
            float(lookup['price']),
            float(lookup['longitude']),
            float(lookup['latitude']))