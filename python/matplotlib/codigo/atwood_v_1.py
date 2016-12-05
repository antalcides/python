#
#Copyright (C) 2012 Diogo Pedro Lopes
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
from visual import*
from visual.text import*

scene.width=500
scene.height=1000
scene.center=(0,6,0)
scene.title="Maquina de Atwood - simulacao"

superficiet=box(pos=(0,-0.5,0), length=10, height=1, width=10, material=materials.wood)
chao=box(pos=(0,0.15,0), length=2, height=0.3, width=2, material=materials.wood)
suporte1=box(pos=(0,6.55,0), length=0.4, height=12.5, width=0.4, material=materials.wood)
suporte2=box(pos=(0,13,0.8), length=0.4, height=0.4, width=2, material=materials.wood)
suporte3=box(pos=(0,13,2), length=4, height=0.4, width=0.4, material=materials.wood)
roldana1=ring(pos=(-1.75,13.1,2.215), axis=(0,0,1), radius=0.25, thickness=0.03)
roldana2=ring(pos=(1.75,13.1,2.215), axis=(0,0,1), radius=0.25, thickness=0.03)
corpo1=box(pos=(-2,6.2,2.215), length=1, height=1, width=1, color=color.blue)
corpo2=box(pos=(2,6.2,2.215), length=1, height=1, width=1, color=color.green)
roldana1b=ellipsoid(pos=(-1.75,13.1,2.215), length=0.5, height=0.5, width=0.001) 
roldana2b=ellipsoid(pos=(1.75,13.1,2.215), length=0.5, height=0.5, width=0.001)

corda=curve(pos=[(-1.75,13.35,2.215),(1.75,13.35,2.215)])
corda1=curve(pos=[(corpo1.pos),(-2,13.1,2.215)])
corda2=curve(pos=[(2,13.1,2.215),(corpo2.pos)])


a=0
a2=0
m1=0
m2=0
dt=0
y0=0
v=0
v0=0
rt=0
g=0
I=0
vi=0
rol=0
pos1=corpo1.pos.y
pos2=corpo2.pos.y


opcao=" "
while opcao not in ['1','2']:
    opcao=input("(1) - Maquina de Atwood padrao\n(2) - Maquina de Atwood com fluido\n")
    if opcao == '1':
        print (' ')
    elif opcao == '2':
        print (' ')
    else:
        print("opcoes 1 ou 2!")

queres=' '
while queres not in ['sim','nao']:
    queres=input('Queres as informacoes carateristicas a simulacao? (sim ou nao)\n')
    if queres=='sim':
        print (' ')
    if queres=='nao':
        print (' ')
    else:
        print(' ')

print("Onde estamos?\n(A) Terra\n(B) Lua\n(C) Plutao\n(D) um planeta com o dobro da aceleraçao gravitica terrestre")
zona=" "
while zona not in ['A','B','C','D']:
    zona=input("Insere a letra correspondente: ")
    if zona=='A':
        g=9.80
    elif zona=='B':
        g=1.67
    elif zona=='C':
        g=5.88
    elif zona=='D':
        g=19.6
    else:
        print("Tem de ser uma das letras acima!")

if queres == 'sim':
    txC3=text(pos=(0,7.6,0.201), axis=(1,0,0), width=0.27, height=0.27, string='A ACELERACAO GRAVITICA E', color=color.black, justify='center')
    tableta=box(pos=(0,7,0), length=6, height=2.5, width=0.401, material=materials.wood)
    txC4=text(pos=(0,6.9,0.201), axis=(1,0,0), width=0.45, height=0.45, string=str(g), color=color.red, justify='center')
    txC5=text(pos=(0,6.4,0.201), axis=(1,0,0), width=0.1, height=0.1, string='METROS POR SEGUNDO (QUADRADO', color=color.black, justify='center')
    aceleracao=label(pos=(0,-3.5,0), box=False, opacity=0)
    tempo=label(pos=(0,-4.5,0), box=False, opacity=0)
    aceleracao.text=('Aceleração = '+str(a)+' (m/s**2)')
    tempo.text=('Tempo = '+str(dt)+' (s)')
    if opcao=='1':
        chaop=frame()
        chao1b=box(frame=chaop, pos=(-2,0.05,2.215), length=1.5, height=0.05, width=1.5)
        chao2b=box(frame=chaop, pos=(2,0.05,2.215), length=1.5, height=0.05, width=1.5)
        placa1=box(frame=chaop, pos=(-2,0.8,1.49), length=1.5, height=1.5, width=0.05)
        placa2=box(frame=chaop, pos=(2,0.8,1.49), length=1.5, height=1.5, width=0.05)
        txC1=text(pos=(-1.9,0.5,1.5151), axis=(1,0,0), width=0.7, height=0.7, string='1', color=color.blue, justify='center')
        txC2=text(pos=(2,0.5,1.5151), axis=(1,0,0), width=0.7, height=0.7, string='2', color=color.green, justify='center')

if queres == 'nao' and opcao=='1':
    chao1b=box(pos=(-2,0.05,2.215), length=1.5, height=0.05, width=1.5)
    chao2b=box(pos=(2,0.05,2.215), length=1.5, height=0.05, width=1.5)

while m1<=0:
    m1=float(input("Qual a massa do corpo 1(em gramas)? "))
    if m1<0:
        print("A massa do corpo tem de ser positiva!")
    if m1==0:
        print("A massa do corpo tem de ser positiva!")
while m2<=0:
    m2=float(input("Qual a massa do corpo 2(em gramas)? "))
    if m2<0:
        print("A massa do corpo tem de ser positiva!")
    if m2==0:
        print("A massa do corpo tem de ser positiva!")

while opcao=='1':
    rate(100)
    dt=dt+0.01
    a1=g*((abs(m2-m1))/(m1+m2))
    v=v0+a*dt
    corpo1.pos.y=pos1+v0*dt-0.5*a*dt**2
    corpo2.pos.y=pos2+v0*dt+0.5*a*dt**2
    corda1.pos=[corpo1.pos,(-2,13.1,2.215)]
    corda2.pos=[(2,13.1,2.215),(corpo2.pos)]
    if m1<m2:
        a=-a1
    if m1>m2:
        a=a1
    if corpo1.pos.y<=0.575 or corpo2.pos.y<=0.575:
        break

liquido=" "
while opcao=='2' and liquido not in ['a','m','e']:
    liquido=input('Qual o fluido que pretendes?\n(a)-agua\n(m)-mercurio\n(e)-etanol\n')
    if liquido == 'a':
        rol=1
        liquid=box(pos=(0,1.4,2.215), length=7.8, height=2.5, width=1.8,color=color.blue, opacity=0.15)
    elif liquido == 'm':
        rol=13.579
        liquid=box(pos=(0,1.4,2.215), length=7.8, height=2.5, width=1.8,color=(0.1,0.1,0.1), opacity=0.35)
        luzm1 = local_light(pos=(-2.5,2.1,2.215), color=(0.9,0.9,0.9))
        luzm2 = local_light(pos=(2.5,2.1,2.215), color=(0.9,0.9,0.9))
    elif liquido == 'e':
        rol=0.79
        liquid=box(pos=(0,1.4,2.215), length=7.8, height=2.5, width=1.8,color=color.cyan, opacity=0.15)
    else:
        print("(a),(m) ou (p)?")

if opcao=='2':
    aquariochao=box(pos=(0,0.05,2.215), length=8, height=0.1, width=2)
    aquariotras=box(pos=(0,1.6,1.265), length=8, height=3, width=0.1, opacity=0.01)
    aquariofrente=box(pos=(0,1.6,3.165), length=8, height=3, width=0.1, opacity=0.006)
    aquarioesquerda=box(pos=(-3.95,1.6,2.215), length=0.1, height=3, width=2, opacity=0.01)
    aquariodireita=box(pos=(3.95,1.6,2.215), length=0.1, height=3, width=2, opacity=0.01)


while opcao=='2':
    rate(100)
    dt=dt+0.01
    a1=g*((m1-m2)/(m1+m2))
    a2=g*((abs(m2-m1)-vi*rol)/(m2+m1))
    I=rol*g*vi
    v=a*dt
    vi=1
    corpo1.pos.y=pos1+v0*dt-0.5*a*dt**2
    corpo2.pos.y=pos2+v0*dt+0.5*a*dt**2
    corda1.pos=[corpo1.pos,(-2,13.1,2.215)]
    corda2.pos=[(2,13.1,2.215),(corpo2.pos)]
    if m1>m2:
        a=a1
        if corpo1.pos.y<=2.6:
            a=a2
    if m1<m2:
        a=-a1
        if corpo2.pos.y<=2.6:
            a=-a2
    if (corpo1.pos.y>=2.55 or corpo2.pos.y>=2.55) and (corpo1.pos.y<=2.65 or corpo2.pos.y<=2.65) and a2<=0:
        break
    if corpo1.pos.y<=0.575 or corpo2.pos.y<=0.575:
        break
