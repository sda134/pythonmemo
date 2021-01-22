import spidev
import time
import sys
#import binascii

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 100000 
#spi.mode = 0b01

#t_sb = 0
#filt = 0
#spi3w_en = 0	# 0:4wires 1:3wires
#config_reg = (t_sb << 5) | (filt << 2) | spi3w_en

osrs_t = 0b001
osrs_p = 0b001
mode = 0b01
ctrl_meas = (osrs_t << 5) | (osrs_p << 2) | mode	

spi.xfer2([0b01110100,ctrl_meas])

def read_data(address :int, data :bytes) -> bytes:
	ret = spi.xfer2([0xF7,0x00,0x00,0x00])
	return ret


while True: 
    try:		
		hum_data = spi.xfer2([0xFC,0x00,0x00])
		temp_data = spi.xfer2([0xF9,0x00,0x00,0x00])
		press_data = read_data(0xF7)

		print(press_data)
		time.sleep(1)

    except KeyboardInterrupt:
        spi.close()
        sys.exit()              



	

