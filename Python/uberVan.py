from car import Car

class UberVan(Car):
    typeCarAccepted = str
    seatsMaterial = str

    def __init__(self, license, driver, typeCarAccepted, seatsMaterial):
        super.__init__(self, license, driver)
        self.typeCarAccepted = typeCarAccepted
        self.seatsMaterial = seatsMaterial