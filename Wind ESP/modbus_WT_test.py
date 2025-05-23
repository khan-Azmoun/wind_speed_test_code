
import time
from machine import Pin, UART
from umodbus.serial import Serial as ModbusRTUMaster
# Define the pins for Modbus communication
#rtu_pins = (Pin(0), Pin(1))
rtu_pins = (Pin(16), Pin(17))
# Define the starting address to read from
#starting_address =
starting_address=0x00  #0BCC

# Define the quantity of registers to read
qty = 2
# Initialize Modbus RTU Master
#host = ModbusRTUMaster(baudrate=4800, data_bits=8, stop_bits=1, parity=None, pins=rtu_pins, ctrl_pin=None, uart_id=0)
host = ModbusRTUMaster(baudrate=4800, data_bits=8, stop_bits=1, parity=None, pins=rtu_pins, ctrl_pin=None, uart_id=2)
# Continuous reading loop
while True:
    try:
        print('INPUT REGISTER request test.')
        print('Reading qty={} from starting address {}:'.format(qty, starting_address))

        # Read input registers from the slave device
        values = host.read_holding_registers(slave_addr=0x01, starting_addr=starting_address, register_qty=qty, signed=False)

        # Print the result
        #print('Result: {}'.format(values[1]))
        print('Holding register value: ' + ' '.join('{:d}'.format(x) for x in values))


    except Exception as e:
        print('An error occurred:', e)

    # Wait for 5 seconds before the next reading
    time.sleep(10)
