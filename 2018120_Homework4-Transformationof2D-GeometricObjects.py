#Name : Vrinda Narayan
#Roll Number : 2018120
#Section : A
#Group : 8
import matplotlib.pyplot as plt
from math import *
def multiply(trans, x, y):
    '''to multiply two matrices'''
    coord=[x,y,1]
    l=[]
    for i in range(3):
        s=0
        for j in range(3):
            s=s+trans[i][j]*coord[j]
        l=l+[s]
    return l
def scale_poly(x,y,command):
    command[1]=int(command[1])
    command[2]=int(command[2])
    #scale is the 3x3 matrix according to the sheet
    scale=[[command[1],0,0],[0,command[2],0],[0,0,1]]
    for i in range(len(x)):
        #all the matrices are multiplied and points updated
        trans=multiply(scale,x[i],y[i])
        x[i]=trans[0]
        y[i]=trans[1]
def rotate_poly(x,y,command):
    command[1]=(int(command[1])/180)*pi
    #requiered matrix to multiply
    scale=[[cos(command[1]),-sin(command[1]),0],[sin(command[1]),cos(command[1]),0],[0,0,1]]
    for i in range(len(x)):
        #all the matrices are multiplied and points updated
        trans=multiply(scale,x[i],y[i])
        x[i]=trans[0]
        y[i]=trans[1]
def translate_poly(x,y,command):
    command[1]=int(command[1])
    command[2]=int(command[2])
    #requiered matrix to translate
    scale=[[1,0,command[1]],[0,1,command[2]],[0,0,1]]
    for i in range(len(x)):
        #all the points are updates
        trans=multiply(scale,x[i],y[i])
        x[i]=trans[0]
        y[i]=trans[1]
def polygon():
	x=list(map(int,input().split(' ')))
	y=list(map(int,input().split(' ')))
	#x and y coordinate inputed and stored as list, x[0] added in the end to complete the polynomial
	x=x+[x[0]]
	y=y+[y[0]]
	command=input().split()
	plt.ion()
	while command[0]!='quit':
            #command is inputed till we quit
            plt.plot(x,y)
            plt.show()
            if command[0]=='S':
                scale_poly(x,y,command)
            if command[0]=='R':
                rotate_poly(x,y,command)
            if command[0]=='T':
                translate_poly(x,y,command)
            #changes are reflected in the original list
            print(x[:-1])
            print(y[:-1])
            plt.plot(x,y)
            plt.show()
            command=input().split()
def disc():
    arg=list(map(int,input().split()))
    d=0
    x=[]
    y=[]
    #this loop converts a disc to a polygon with a lot of points
    #the distance between points is dx and dy
    while d<2*pi:
        x=x+[arg[0]+arg[2]*cos(d)]
        y=y+[arg[1]+arg[2]*sin(d)]
        d=d+0.002
    #command is inputed
    command=input().split()
    plt.ion()
    while command[0]!='quit':
            plt.plot(x,y)
            plt.show()
            if command[0]=='S':
                #scaling function same for any polygon
                scale_poly(x,y,command)
                blah=arg[2]
                #when scaling is done, the radius changes
                arg[2]=command[1]*blah
                arg=arg+[command[2]*blah]
                print(arg)
            if command[0]=='R':
                rotate_poly(x,y,command)
                #when we rotate an ellipse, it's axis changes but not the centre or radius
                print(arg)
            if command[0]=='T':
                translate_poly(x,y,command)
                #translate : we shift our ellipse hence centre changes
                arg[0]=arg[0]+command[1]
                arg[1]=arg[1]+command[2]
                print(arg)
            plt.plot(x,y)
            plt.show()
            command=input().split()
        
figure=input()
#if input is disc, disc function is called and otherwise polygon function is calles
if figure=='disc':
	disc()
if figure=='polygon':
	polygon()
