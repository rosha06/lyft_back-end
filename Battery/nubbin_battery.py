from Battery.battery import Battery

class NubbinBattery(Battery):
    def __init__(self, current_date:date, last_service_date:date): # type: ignore
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.nubbin_year_need_service = 3


    def need_service(self):
        date_need_service = self.last_service_date.replace(year=self.last_service_date.year + self.nubbin_year_need_service)
        if date_need_service < self.current_date:
            return True
        else:
            return False