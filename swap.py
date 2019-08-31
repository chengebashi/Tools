#!/usr/bin/env python3
# -*-conding:utf-8-*-
import math

def second10(num):
    '''二进制转十进制'''
    c = 0
    num = num[::-1]
    for i in range(len(num)):
        a = int(num[i])
        if a == 1:
            c = c + pow(2, i)
    return c

def second8(num):
    '''二进制转八进制'''
    a = len(num) % 3
    if a == 1:
        num = '00' + num
    if a == 2:
        num = '0' + num
    num = [int(x) for x in num]
    good = len(num) / 3 - 1
    c = 0
    for i in range(0, len(num), 3):
        s = num[i:i+3]
        b = second10(s)
        c = c + b * pow(10, good)
        c = int(c)
        good -= 1
    return  c

def second16(num):
    '''二进制转十六进制'''
    a = len(num) % 4
    if a == 1:
        num = '000' + num
    if a == 2:
        num = '00' + num
    if a == 3:
        num = '0' + num
    num = [int(x) for x in num]
    c = ''
    for i in range(0, len(num), 4):
        s = num[i:i+4]
        vessel = second10(s)
        if vessel == 10:
            vessel = 'A'
        if vessel == 11:
            vessel = 'B'
        if vessel == 12:
            vessel = 'C'
        if vessel == 13:
            vessel = 'D'
        if vessel == 14:
            vessel = 'E'
        if vessel == 15:
            vessel = 'F'
        c = c + str(vessel)
    return c


def tenth2(num):
    '''十进制转二进制'''
    num = int(num)
    c = ''
    while num > 0:
        s = int(num % 2)
        num = int(num / 2)
        c = str(s) + c
    return c

def tenth8(num):
    '''十进制转八进制'''
    a = tenth2(num)
    return second8(a)

def tenth16(num):
    '''十进制转16进制'''
    a = tenth2(num)
    return second16(a)


# number = str(input('请输入16进制数:'))
def eighth2(num):
    c = ''
    for i in num:
        if i == '0':
            a = '000'
        if i == '1':
            a = '001'
        if i == '2':
            a = '010'
        if i == '3':
            a = '011'
        if i == '4':
            a = '100'
        if i == '5':
            a = '101'
        if i == '6':
            a = '110'
        if i == '7':
            a = '111'
        c = c + a
    return int(c)

def eighth10(num):
    a = eighth2(num)
    b = second10(str(a))
    return b

def eighth16(num):
    a = eighth2(num)
    b = second16(str(a))
    return b

def sixth2(num):
    c = ''
    for i in num:
        if i == '0':
            a = '0000'
        if i == '1':
            a = '0001'
        if i == '2':
            a = '0010'
        if i == '3':
            a = '0011'
        if i == '4':
            a = '0100'
        if i == '5':
            a = '0101'
        if i == '6':
            a = '0110'
        if i == '7':
            a = '0111'
        if i == '8':
            a = '1000'
        if i == '9':
            a = '1001'
        if i == 'A':
            a = '1010'
        if i == 'B':
            a = '1011'
        if i == 'C':
            a = '1100'
        if i == 'D':
            a = '1101'
        if i == 'E':
            a = '1110'
        if i == 'F':
            a = '1111'
        c = c + a
    return int(c)

def sixth8(num):
    a = sixth2(num)
    c = second8(str(a))
    return c

def sixth10(num):
    a = sixth2(num)
    c = second10(str(a))
    return c
