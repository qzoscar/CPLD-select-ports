# CPLD-select-ports
The CPLD has limited IOs and in our Verilog we shal not define IOS more than 76 for EP570. However in our automation assignment algorithm we do below:

1.	Analysis all pins that are need to be used.
2.	Sort the pins list.
3.	Divide the pin list into different buses, with below algorithm
If Used_io[i] - Used_io[i-1] > 7, then we create a new bus group.
Else combine them into a continues bus range.
7 here is a experimental value.

The limitation of this algorithm is that we will waste some ios, and result in define too many ios in Verilog that exceed the limitation, e.g. for below list
Used IO-Pins:  [2, 3, 8, 15, 16, 17, 18, 19, 20, 21, 40, 42, 49, 50, 57, 61, 67, 70, 73, 74, 75, 81, 83, 85, 87, 91]
Above algorithm we give us 2 Buses 
bus_scope
[(2, 21), (40, 91)]

We actual use 26 pins, but we define 20 + 52 = 72 pins.

Can anyone propose an self-adaptive algorithm in python which can return the less used Pins? Meanwhile the overall buses shall not exceed 12? And the continues pins shall be in one group.
