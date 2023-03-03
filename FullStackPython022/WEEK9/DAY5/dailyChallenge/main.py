from datetime import datetime
import datetime


class Airline:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.planes = []

    def __repr__(self):
        return self.name


class Airplane:
    id = 0

    def __init__(self, current_location, company):
        self.id = Airplane.id
        self.current_location = current_location
        self.company = company
        self.next_flights = []
        current_location.planes.append(self)
        company.planes.append(self)
        Airplane.id += 1

    def fly(self, destination):
        list_of_flights = [flight for flight in self.next_flights if flight.destination == destination]
        if not list_of_flights:
            print("This plane doesn't have flights to this destination!")
        else:
            list_of_flights[0].take_off()
            list_of_flights[0].land()
            self.next_flights.remove(list_of_flights[0])

    def location_on_date(self, date):
        list_of_flights = [flight for flight in self.next_flights if flight.date <= date]
        if not list_of_flights:
            return self.current_location
        return list_of_flights[-1].destination

    def available_on_date(self, date, location):
        if self.location_on_date(date) != location:
            return False
        return not any(flight for flight in self.next_flights if flight.date == date)


class Flight:
    def __init__(self, date: datetime.date, destination, origin, plane):
        self.ID = f"{destination.city}{plane.company.id}{str(date)}"
        self.date = date
        self.destination = destination
        self.origin = origin
        self.plane = plane

    def take_off(self):
        self.plane.current_location = None
        self.origin.scheduled_departures.remove(self)

    def land(self):
        self.plane.current_location = self.destination
        self.destination.scheduled_arrivals.remove(self)


class Airport:
    def __init__(self, city):
        self.city = city
        self.planes = []
        self.scheduled_departures = []
        self.scheduled_arrivals = []

    def schedule_flight(self, destination, date_time, companies):
        for company in companies:
            for plane in company.planes:
                if plane.available_on_date(date_time, self):
                    new_flight = Flight(date_time, destination, self, plane)
                    self.scheduled_departures.append(new_flight)
                    destination.scheduled_arrivals.append(new_flight)
                    plane.next_flights.append(new_flight)
                    break
            else:
                continue
            break
        else:
            print(
                f'There are no available planes with the following parameters! (departure: {self.city}; destination: {destination.city}; date: {date_time})')
            return

        self.scheduled_departures.sort(key=lambda flight: flight.date)
        destination.scheduled_arrivals.sort(key=lambda flight: flight.date)
        plane.next_flights.sort(key=lambda flight: flight.date)

    def info(self, start_date, end_date):
        list_of_departures = list(
            filter(lambda flight: start_date <= flight.date <= end_date, self.scheduled_departures))
        list_of_arrivals = list(filter(lambda flight: start_date <= flight.date <= end_date, self.scheduled_arrivals))
        print(f"Airport {self.city} schedule:")
        print('Departures')
        if list_of_departures:
            for flight in list_of_departures:
                print(
                    f"Date - {flight.date}; Destination - {flight.destination}; Company - {flight.plane.company.name}; Plane ID - {flight.plane.id}")
        else:
            print('no departures')

        print('Arrivals')
        if list_of_arrivals:
            for flight in list_of_arrivals:
                print(
                    f"Date - {flight.date}; Origin - {flight.origin}; Company - {flight.plane.company.name}; Plane ID - {flight.plane.id}")
        else:
            print('no arrivals')


# Test Code

ukraine_air = Airline('AA', 'Flyuia')
elal_air = Airline('EA', 'ElAl Airlines')
list_companies = [ukraine_air, elal_air]

ben_gurion = Airport('Tel Aviv')
lviv = Airport('Lviv')

aa_1 = Airplane(ben_gurion, ukraine_air)
aa_2 = Airplane(lviv, ukraine_air)

ben_gurion.schedule_flight(lviv, datetime.date(2023, 4, 4), list_companies)
ben_gurion.schedule_flight(lviv, datetime.date(2023, 4, 7), list_companies)

lviv.schedule_flight(ben_gurion, datetime.date(2023, 4, 5), list_companies)
ben_gurion.schedule_flight(lviv, datetime.date(2023, 4, 6), list_companies)

ben_gurion.info(datetime.date(2023, 4, 1), datetime.date(2023, 4, 10))
lviv.info(datetime.date(2023, 4, 1), datetime.date(2023, 4, 10))

aa_1.fly(lviv)
aa_1.fly(ben_gurion)

ben_gurion.info(datetime.date(2023, 4, 1), datetime.date(2023, 4, 10))
lviv.info(datetime.date(2023, 4, 1), datetime.date(2023, 4, 10))
