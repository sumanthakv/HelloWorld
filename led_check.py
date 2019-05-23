from auto_instr import *
curr_cmpl=(.2)
addr= gpib.addr(0,5)
import numpy as np
# addr_temp=gpib.addr(0,17)
# soak=120
# t_sweep=[85,125]
datalog.filename = 'led_5mm_red'
datalog.header('Device', 'voltage', 'current(mA)')
ke2400.on(addr)
ke2400.off(addr)
ke2400.forVmeasI(addr,0, curr_cmpl)
device='red'
device=device.upper()
for v in np.arange(1,3.4,.1):
    read_current=ke2400.forVmeasI(addr, v, curr_cmpl)
    read_current=1000*read_current
    data = [str(device), v, float(read_current)]
    print(data)
    datalog.data(data)


