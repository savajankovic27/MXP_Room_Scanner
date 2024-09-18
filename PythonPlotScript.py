from cmath import cos, sin
from os import truncate
from turtle import color
import serial
import math
import numpy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


erase = input("Delete the previous data?(Y/N)")
if(erase == 'Y' or 'y'):
    f = open('graphdata.txt','w')          # the write mode would be opened, this means that the code will be written to the graph data
    truncate                                                                    
    f.close() # everything is deleted if the answer is yes. 

s = serial.Serial('COM5', baudrate = 115200, timeout = 4)                # receive the data from the msp, with the set baud rate and the COM5
print("Opening: " + s.name)   # open file

s.reset_output_buffer()        # input and output buffers enabled
s.reset_input_buffer()

fig = plt.figure(figsize=(10,10))                                              # graph ready
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('z')
ax.set_ylabel('y')
ax.set_zlabel('x')

s.write('s'.encode())                                                           # start the data encoding
  
count = 0
x_line=0
yline=0
z_line=0
z = 0

x = [0]*64      ## one rotation is 64 movements, or 512 steps.                                                                  #array set for one rotation
f = open('graphdata.txt','a')                                                   #append mode. 
while (count != 64):
    x[count] = float(s.readline().decode())                                     #decode the data
    print(x[count], count+1)
    f.write(str(x[count]))                                                      # string conversion
    f.write('\n')                                                                   # next line
    count+=1
f.close()

data = open("graphdata.txt","r")                                                #read only for the text file. 
dataStr = data.read()                                                           #text file put in the string. 
dataList = dataStr.split("\n")                                                   ## separate by spaces /n
for i in range(0,len(dataList),1):                                              
    dataList[i] = str(dataList[i])                                              #place onto the list
data.close()
dataList.pop(len(dataList)-1)                                                

Data = [float(i) for i in dataList]                                            # turn into float for the list
numlines = len(Data)                                                            # the number of measurements used. 

plotOnot = input("Would you like to plot the data?(Y/N)")

if(plotOnot == 'Y'):

    count = 0
    while(count != numlines):                                                   #as long as there are data that can be graphed .

        if(count==64):                                                          
            z+=0.1
        elif(count==128):
            z+=0.1
        elif(count==192):
            z+=0.1
        elif(count==256):
            z+=0.1
        elif(count==320):
            z+=0.1
        elif(count==384):
            z+=0.1
        elif(count==448):
            z+=0.1
        elif(count==512):
            z+=0.1
        elif(count==576):
            z+=0.1
        elif(count==640):
            z+=0.1

        x_line = [(Data[count-1])*cos((count-1)*0.09817477),(Data[count])*cos(count*0.09817477)]    # segment, the equations have been implemented. 
        y_line = [(Data[count-1])*sin((count-1)*0.09817477),(Data[count])*sin(count*0.09817477)]
        if(count <  64):
            z_line = [0,0]
        else:
            z_line = [z,z] 
                                                                                #cartesian plotting of points. 
        ax.scatter( (Data[count])*cos(count*0.09817477) ,(Data[count])*sin(count*0.09817477),z, c = "black", s = 1)

        if(count<64):
            ax.plot(x_line ,y_line,0, color = 'black')                         # if on the plane... 
        else:
            ax.plot(x_line ,y_line,z_line, color = 'black')
        count+=1

    count = 0
    while(count < numlines-64):                                            
        if(count<64):
            z = 0
            x_line = [(Data[count])*cos((count)*0.09817477),(Data[count+64])*cos(count*0.09817477)]
            y_line = [(Data[count])*sin((count)*0.09817477),(Data[count+64])*sin(count*0.09817477)]
            z_line = [0,0.1]
            ax.plot(x_line ,y_line,z_line, color = 'black')
        elif(64<=count<128):
            z = 0.1
            x_line = [(Data[count])*cos((count)*0.09817477),(Data[count+64])*cos(count*0.09817477)]
            y_line = [(Data[count])*sin((count)*0.09817477),(Data[count+64])*sin(count*0.09817477)]
            z_line = [0.1,0.2]
            ax.plot(x_line ,y_line,z_line, color = 'black')
        elif(128<=count<192):
            z = 0.2
            x_line = [(Data[count])*cos((count)*0.09817477),(Data[count+64])*cos(count*0.09817477)]
            y_line = [(Data[count])*sin((count)*0.09817477),(Data[count+64])*sin(count*0.09817477)]
            z_line = [0.2,0.3]
            ax.plot(x_line ,y_line,z_line, color = 'black')
        if(192<=count<256):
            z = 0.3
            x_line = [(Data[count])*cos((count)*0.09817477),(Data[count+64])*cos(count*0.09817477)]
            y_line = [(Data[count])*sin((count)*0.09817477),(Data[count+64])*sin(count*0.09817477)]
            z_line = [z,z+0.1]
            ax.plot(x_line ,y_line,z_line, color = 'black')
        if(256<=count<320):
            z = 0.4
            x_line = [(Data[count])*cos((count)*0.09817477),(Data[count+64])*cos(count*0.09817477)]
            y_line = [(Data[count])*sin((count)*0.09817477),(Data[count+64])*sin(count*0.09817477)]
            z_line = [z,z+0.1]
            ax.plot(x_line ,y_line,z_line, color = 'black')
        if(320<=count<384):
            z = 0.5
            x_line = [(Data[count])*cos((count)*0.09817477),(Data[count+64])*cos(count*0.09817477)]
            y_line = [(Data[count])*sin((count)*0.09817477),(Data[count+64])*sin(count*0.09817477)]
            z_line = [z,z+0.1]
            ax.plot(x_line ,y_line,z_line, color = 'black')
        if(384<=count<448):
            z = 0.6
            x_line = [(Data[count])*cos((count)*0.09817477),(Data[count+64])*cos(count*0.09817477)]    ## repeating the plots for each set of data. 
            y_line = [(Data[count])*sin((count)*0.09817477),(Data[count+64])*sin(count*0.09817477)]
            z_line = [z,z+0.1]
            ax.plot(x_line ,y_line,z_line, color = 'black')
        if(448<=count<512):
            z = 0.7
            x_line = [(Data[count])*cos((count)*0.09817477),(Data[count+64])*cos(count*0.09817477)]
            y_line = [(Data[count])*sin((count)*0.09817477),(Data[count+64])*sin(count*0.09817477)]
            z_line = [z,z+0.1]
            ax.plot(x_line ,y_line,z_line, color = 'black')
        if(512<=count<576):
            z = 0.8
            x_line = [(Data[count])*cos((count)*0.09817477),(Data[count+64])*cos(count*0.09817477)]
            y_line = [(Data[count])*sin((count)*0.09817477),(Data[count+64])*sin(count*0.09817477)]
            z_line = [z,z+0.1]
            ax.plot(x_line ,y_line,z_line, color = 'black')
        if(576<=count<640):
            z = 0.9
            x_line = [(Data[count])*cos((count)*0.09817477),(Data[count+64])*cos(count*0.09817477)]
            y_line = [(Data[count])*sin((count)*0.09817477),(Data[count+64])*sin(count*0.09817477)]
            z_line = [z,z+0.1]
            ax.plot(x_line ,y_line,z_line, color = 'black')
        count+=1
    plt.show()                                          #present the graph

print("Closing: " + s.name )                          #close the COM5. 
s.close()
