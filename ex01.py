
import math
import time

# Get the current time in seconds from the epoch
seconds_from_epoch = time.time()
#print(f"Current time in seconds from the epoch in scientific notation: {seconds_from_epoch:.2e}")

exponent = int(math.floor(math.log10(abs(seconds_from_epoch))))
mantissa = seconds_from_epoch / (10 ** exponent)
mantissa = round(mantissa, 2)

print(seconds_from_epoch)
print(format(seconds_from_epoch, ',.4f'))
#print(f"Current time in seconds from the epoch in scientific notation: {mantissa}e{exponent}")

print("Seconds since January 1, 1970: " + format(seconds_from_epoch, ',.4f') \
      + " or " + str(mantissa) + "e+" + str(exponent) + " in scientific notation")
print(time.strftime("%b %d %Y"))
