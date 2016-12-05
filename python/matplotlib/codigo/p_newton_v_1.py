#
#Copyright (C) 2012 Diogo Vieira
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

from math import*
from visual import *

bola=sphere(pos=(0,0,0), radius=0.0005)
bola1=sphere(pos=(-6,0,0), radius=2)
bola2=sphere(pos=(6,0,0), radius=2)
bola3=sphere(pos=(-2,0,0), radius=2)
bola4=sphere(pos=(2,0,0), radius=2)
suporte1=cylinder(pos=(-6,10,0), radius=0.2, axis=(0,0,2))
suporte2=cylinder(pos=(6,10,0), radius=0.2, axis=(0,0,2))
suporte3=cylinder(pos=(-2,10,0), radius=0.2, axis=(0,0,2))
suporte4=cylinder(pos=(2,10,0), radius=0.2, axis=(0,0,2))
fio1=curve(pos=[(suporte1.pos),(bola1.pos)])
fio2=curve(pos=[(suporte2.pos),(bola2.pos)])
fio3=curve(pos=[(suporte3.pos),(bola3.pos)])
fio4=curve(pos=[(suporte4.pos),(bola4.pos)])

opçao=' '
while opçao not in ['1','2','3','4']:
    opçao=input("(1) - 1 bola lançada\n(2) - 2 bolas lançadas\n(3) - 3 bolas lançadas\n(4) - 4 bolas lançadas\n")
    if opçao == '1':
        print (' ')
    elif opçao == '2':
        print (' ')
    elif opçao == '3':
        print (' ')
    elif opçao == '4':
        print (' ')
    else:
        print("opcoes 1, 2, 3 ou 4!")

angulo0=float(input("Qual o ângulo inicial? "))


dt=0.01
l=10
angulo=(180-angulo0)*pi/180
g=-10
omega = 0

while opçao=='1':
    rate (250)
    omega+=-g*sin (angulo)*dt/l
    angulo+=omega*dt
    bola.pos=(l*sin(angulo),l*cos(angulo)+10,0)
    fio2.pos=[(suporte2.pos),(bola2.pos)]
    fio1.pos=[(suporte1.pos),(bola1.pos)]
    fio3.pos=[(suporte3.pos),(bola3.pos)]
    fio4.pos=[(suporte4.pos),(bola4.pos)]
    if bola.pos.x<=0:
        bola1.pos=(-6+l*sin(angulo),l*cos(angulo)+10,0)
        bola2.pos=(6,0,0)
    if bola.pos.x>=0:
        bola1.pos=(-6,0,0)
        bola2.pos=(6+l*sin(angulo),l*cos(angulo)+10,0)

while opçao=='2':
    rate (250)
    omega+=-g*sin (angulo)*dt/l
    angulo+=omega*dt
    bola.pos=(l*sin(angulo),l*cos(angulo)+10,0)
    fio2.pos=[(suporte2.pos),(bola2.pos)]
    fio1.pos=[(suporte1.pos),(bola1.pos)]
    fio3.pos=[(suporte3.pos),(bola3.pos)]
    fio4.pos=[(suporte4.pos),(bola4.pos)]
    if bola.pos.x<=0:
        bola1.pos=(-6+l*sin(angulo),l*cos(angulo)+10,0)
        bola2.pos=(6,0,0)
        bola3.pos=(-2+l*sin(angulo),l*cos(angulo)+10,0)
        bola4.pos=(2,0,0)
    if bola.pos.x>=0:
        bola1.pos=(-6,0,0)
        bola2.pos=(6+l*sin(angulo),l*cos(angulo)+10,0)
        bola3.pos=(-2,0,0)
        bola4.pos=(2+l*sin(angulo),l*cos(angulo)+10,0)
        
while opçao=='3':
    rate (250)
    omega+=-g*sin (angulo)*dt/l
    angulo+=omega*dt
    bola.pos=(l*sin(angulo),l*cos(angulo)+10,0)
    fio2.pos=[(suporte2.pos),(bola2.pos)]
    fio1.pos=[(suporte1.pos),(bola1.pos)]
    fio3.pos=[(suporte3.pos),(bola3.pos)]
    fio4.pos=[(suporte4.pos),(bola4.pos)]
    if bola.pos.x<=0:
        bola1.pos=(-6+l*sin(angulo),l*cos(angulo)+10,0)
        bola2.pos=(6,0,0)
        bola3.pos=(-2+l*sin(angulo),l*cos(angulo)+10,0)
        bola4.pos=(2+l*sin(angulo),l*cos(angulo)+10,0)
    if bola.pos.x>=0:
        bola1.pos=(-6,0,0)
        bola2.pos=(6+l*sin(angulo),l*cos(angulo)+10,0)
        bola3.pos=(-2+l*sin(angulo),l*cos(angulo)+10,0)
        bola4.pos=(2+l*sin(angulo),l*cos(angulo)+10,0)

while opçao=='4':
    rate (250)
    omega+=-g*sin (angulo)*dt/l
    angulo+=omega*dt
    bola.pos=(l*sin(angulo),l*cos(angulo)+10,0)
    fio2.pos=[(suporte2.pos),(bola2.pos)]
    fio1.pos=[(suporte1.pos),(bola1.pos)]
    fio3.pos=[(suporte3.pos),(bola3.pos)]
    fio4.pos=[(suporte4.pos),(bola4.pos)]
    bola1.pos=(-6+l*sin(angulo),l*cos(angulo)+10,0)
    bola2.pos=(6+l*sin(angulo),l*cos(angulo)+10,0)
    bola3.pos=(-2+l*sin(angulo),l*cos(angulo)+10,0)
    bola4.pos=(2+l*sin(angulo),l*cos(angulo)+10,0)
