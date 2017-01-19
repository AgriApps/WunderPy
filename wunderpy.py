Copyright (C) 2017 Justin Zondagh / Agri Apps

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

import requests
import urllib


class PWSData(object):

        base_url = None

        data = None


        def __init__(self, id, password):

                self.base_url = "https://weatherstation.wunderground.com/weatherstation/updateweatherstation.php"
                self.data = {}
                self.parameters = {}
                self.parameters["action"] = "updateraw"
                self.parameters["ID"] = id
                self.parameters["PASSWORD"] = password


        def add_data(self, date, type, value):

                if date not in self.data:
                        self.data[date] = []

                new = { 

                        "date": date,
                        "type": type,
                        "value": str(value)
                }       

                self.data[date].append(new)

	def clear(self):
		self.data = {}

	def add_temperature_c(self, date, value):
		self.add_data(date, "tempf", (value * 9.0 / 5.0) + 32)


	def add_humidity(self, date, value):
		self.add_data(date, "humidity", value)

	def add_rainfall_mm(self, date, value):
		self.add_data(date, "rainin", value / 25.4)

        
        def send_data(self):


                for date, reading in self.data.iteritems():

			url = "%s?" % self.base_url

			for p, value in self.parameters.iteritems():
			
				url = "%s%s=%s&" % (url, p, urllib.quote_plus(value))


			url = "%s%s=%s&" % (url, "dateutc", urllib.quote_plus(date))



			for r in reading:

				url = "%s%s=%s&" % (url, r['type'], urllib.quote_plus(r['value']))


			try: 
				res = requests.get(url)
			except requests.exceptions.RequestException as e:
        			return "Error: {}".format(e)
			except requests.exceptions.ConnectionError as e:
				return "Error: {}".format(e)
			except Exception as e:
                                return "Error: {}".format(e)


