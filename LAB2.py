import adafruit_bme680
import time
import board

i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

bme680.sea_level_pressure = 1013.25

timeout = 30

timeout_start = time.time()

while time.time() < timeout_start + timeout:
# 	print("\nTemperature: %0.1f C" % bme680.temperature)
# 	print("Gas: %d ohm" %bme680.gas)
# 	print("Humidity: %0.1f %%" % bme680.relative_humidity)
# 	print("Pressure: %0.3f hPa" % bme680.pressure)
# 	print("Altitude = %0.2f meters" % bme680.altitude)
# 	seconds = time.time()
# 	local_time = time.ctime(seconds)
# 	print("Local time:", local_time)
	print("\nLocal time: %s. Temperature: %0.1f C. Gas: %d ohm. Humidity: %0.1f %%. Pressure: %0.3f hPa. Altitude = %0.2f meters." % (local_time, bme680.temperature, bme680.gas, bme680.relative_humidity, bme680.pressure, bme680.altitude))
	time.sleep(2)
