from wunderpy import PWSData


pws = PWSData("Station code", "key")

pws.add_temperature_c(the_date, entry.value)
pws.add_humidity(the_date, entry.value)
pws.add_rainfall_mm(the_date, entry.value)
pws.send_data()
pws.clear()


