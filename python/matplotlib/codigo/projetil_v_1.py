#
#Copyright (C) 2012 Iúri Miguel Carolino Martinho
#Escola Secundária da Ramada
#
#This program is free software; you can redistribute it and/or modify it under 
#the terms of the GNU General Public License as published by the Free Software 
#Foundation; either version 2 of the License, or (at your option) any later 
#version.
#
#This program is distributed in the hope that it will be useful, but WITHOUT 
#ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS 
#FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#

from visual import *
vo=0
a=-9.8
an=0
xo=-50
yo=8.65
yo2=-15.35
yo3=-38.35
yo4=31.65
x=0
y=0

print ("consideremos que o chão é feito de madeira")

while an<=0 or an>90:
    an = int(input ("Escolha o angulo de lançamento:"))
    if an<=0 or an>90:
        print ("O angulo tem de estar entre 0 e 90 graus")
    
while vo<=0:
    vo = int(input ("Escolha a velocidade inicial:"))
    if vo <=0:
        print("A velocidade tem que ser positiva")

chao = box(pos=(0,7,0), length=100, height=0.3, width=2, material=materials.wood) 
bola = sphere(pos=(-50,8.65,0), make_trail=True, radius=1.5, material=materials.wood)
chao2 = box(pos=(0,-17,0), length=100, height=0.3, width=2, material=materials.wood) 
bola2 = sphere(pos=(-50,-15.35,0), make_trail=True,  radius=1.5, color=color.orange)
chao3 = box(pos=(0,-40,0), length=100, height=0.3, width=2, material=materials.wood) 
bola3 = sphere(pos=(-50,-38.35,0), make_trail=True, radius=1.5, material=materials.plastic)
chao4 = box(pos=(0,30,0), length=100, height=0.3, width=2, material=materials.wood) 
bola4 = sphere(pos=(-50,31.65,0), make_trail=True, radius=1.5, color=color.blue)
text(text='Madeira', align='center', pos=(-43,3.5,0), height=3, depth=-0.3, color=color.white)
text(text='Borracha', align='center', pos=(-43,-21.5,0), height=3, depth=-0.3, color=color.orange)
text(text='Plástico', align='center', pos=(-43,-43.5,0), height=3, depth=-0.3, color=color.white)
text(text='Vidro', align='center', pos=(-43,26.5,0), height=3, depth=-0.3, color=color.blue)

tx=0
ty=0
ty2=0
ty3=0
ty4=0
vox=vo*math.cos(an*pi/180)
x=xo
voy=vo*math.sin(an*pi/180)
voy2=vo*math.sin(an*pi/180)
voy3=vo*math.sin(an*pi/180)
voy4=vo*math.sin(an*pi/180)
y=yo
y2=yo2
y3=yo3
y4=yo4

while true:
    rate (150)
    tx=tx+0.01
    ty=ty+0.01
    ty2=ty2+0.01
    ty3=ty3+0.01
    ty4=ty4+0.01
    x=xo+vox*tx
    bola.x=x
    bola2.x=x
    bola3.x=x
    bola4.x=x
    y=yo+voy*ty+a/2*ty**2
    y2=yo2+voy2*ty2+a/2*ty2**2
    y3=yo3+voy3*ty3+a/2*ty3**2
    y4=yo4+voy4*ty4+a/2*ty4**2
    bola.y=y
    bola2.y=y2
    bola3.y=y3
    bola4.y=y4
    if y<8.65:
        ty=0
        voy=voy*0.5
    if y2<-15.35:
        ty2=0
        voy2=voy2*0.81
    if y3<-38.35:
        ty3=0
        voy3=voy3*0.65
    if y4<31.65:
        ty4=0
        voy4=voy4*0.77
    if voy2<=0.1:
        break 
        
