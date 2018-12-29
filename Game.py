#!/usr/bin env python3
# Make a Flying type and Ice type by the end of break
import random
from time import sleep
class Characters:
    def __init__(self, health, type, name):
        self.health = health
        self.type = type
        self.name = name
C = 0
def H():
    print('Valid Moves:')
    print('Fireball')
    print('Fire Fang')
    print('Flame Thrower')
    print('Life Steal')
    print('(Cough) Type in all Lowercase (Cough)')
    A2 = input('Type in the move you want to use: ')
    if A2 == 'fireball':
        Value = random.randint(1, 10)
        Value1 = random.randint(10, 50)
        if Value == 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
            print('Fireball Hits!')
            P2.health -= Value1
        elif Value == 10:
            print('Fireball Missed')
        elif Value == 1:
            print('Fireball was Super Affective!')
            Value1 *= 2
            P2.health -= Value1
        print('')
        print(P2.name, '         V.S.        ', P1.name)
        print(P2.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A2 == 'fire fang':
        Value2 = random.randint(10, 30)
        Value9 = random.randint(1, 10)
        if Value9 == 1:
            print('Fire Fang Missed!')
        elif Value9 == 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10:
            print('Fire Fang Hit!')
            P2.health -= Value2 
        elif Value9 == 2:
            print('Fire Fang was Super Affective')
            Value2 *= 2
            P2.health -= Value2 
        print('')
        print(P2.name, '         V.S.        ', P1.name)
        print(P2.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A2 == 'flame thrower':
        Value3 = random.randint(1 ,20)
        Value4 = random.randint(1, 20)
        Value5 = random.randint(1, 20)
        Value6 = random.randint(1, 5)
        if Value6 == 1:
            print('First Burn Missed!')
            Value6 = random.randint(1, 5)
            if Value6 != 2:
                P2.health -= Value3 + Value4 + Value5
                Value6 = 1
            elif Value6 == 2:
                print('Second Burn also Missed')
                Value6 = random.randint(1, 5)
                if Value6 != 2:
                    P2.health -= Value3 + Value4
                    Value6 = 1
                elif Value6 == 3:
                    print('Third Burn Also Missed')
                    Value6 = 1
        elif Value6 == 2 or 3 or 4:
            print('Flame Thrower Hit!')
        elif Value6 == 5:
            print('It was Super Affective')
            Value3 *= 2
            Value4 *= 2
            Value5 *= 2
            P2.health -= Value3 + Value4 + Value5
        print('')
        print(P2.name, '         V.S.        ', P1.name)
        print(P2.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A2 == 'life steal':
        print('Life Steal Worked!')
        Value8 = random.randint(10, 30)
        P2.health -= Value8
        Value8 *= 2
        P1.health += Value8
        print('')
        print(P2.name, '         V.S.         ', P1.name)
        print(P2.health,'hp', '                 ', P1.health, 'hp')
        print('')
    else:
        print('Your punishment for not typing correctly. LOSE A TURN!')        
        print('')
        print(P2.name, '         V.S.        ', P1.name)
        print(P2.health,'hp', '                 ', P1.health, 'hp')
        print('')
def H1():
    print('Valid Moves:')
    print('Fireball')
    print('Fire Fang')
    print('Flame Thrower')
    print('Life Steal')
    print('(Cough) Type in all Lowercase (Cough)')
    A2 = input('Type in the move you want to use: ')
    if A2 == 'fireball':
        Value = random.randint(1, 10)
        Value1 = random.randint(10, 50)
        if Value == 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
            print('Fireball Hits!')
            C.health -= Value1
        elif Value == 10:
            print('Fireball Missed')
        elif Value == 1:
            print('Fireball was Super Affective!')
            Value1 *= 2
            C.health -= Value1
        print('')
        print(C.name, '         V.S.        ', P1.name)
        print(C.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A2 == 'fire fang':
        Value2 = random.randint(10, 30)
        Value9 = random.randint(1, 10)
        if Value9 == 1:
            print('Fire Fang Missed!')
        elif Value9 == 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10:
            print('Fire Fang Hit!')
            C.health -= Value2 
        elif Value9 == 2:
            print('Fire Fang was Super Affective')
            Value2 *= 2
            C.health -= Value2 
        print('')
        print(C.name, '         V.S.        ', P1.name)
        print(C.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A2 == 'flame thrower':
        Value3 = random.randint(1 ,20)
        Value4 = random.randint(1, 20)
        Value5 = random.randint(1, 20)
        Value6 = random.randint(1, 5)
        if Value6 == 1:
            print('First Burn Missed!')
            Value6 = random.randint(1, 5)
            if Value6 != 2:
                P2.health -= Value3 + Value4 + Value5
                Value6 = 1
            elif Value6 == 2:
                print('Second Burn also Missed')
                Value6 = random.randint(1, 5)
                if Value6 != 3:
                    P2.health -= Value3 + Value4
                    Value6 = 1
                elif Value6 == 3:
                    print('Third Burn Also Missed')
                    Value6 = 1
        elif Value6 == 2 or 3 or 4:
            print('Flame Thrower Hit!')
            C.health -= Value3
            C.health -= Value4
            C.health -= Value5
        elif Value6 == 5:
            print('It was Super Affective')
            Value3 *= 2
            Value4 *= 2
            Value5 *= 2
            C.health -= Value3 + Value4 + Value5
        print('')
        print(C.name, '         V.S.        ', P1.name)
        print(C.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A2 == 'life steal':
        print('Life Steal Worked!')
        Value8 = random.randint(10, 30)
        C.health -= Value8
        Value8 *= 2
        P1.health += Value8
        print('')
        print(C.name, '         V.S.         ', P1.name)
        print(C.health,'hp', '                 ', P1.health, 'hp')
        print('')
    else:
        print('Your punishment for not typing correctly. LOSE A TURN!')        
        print('')
        print(C.name, '         V.S.        ', P1.name)
        print(C.health,'hp', '                 ', P1.health, 'hp')
        print('')
def H2():
    print('Valid Moves:')
    print('Fireball')
    print('Fire Fang')
    print('Flame Thrower')
    print('Life Steal')
    print('(Cough) Type in all Lowercase (Cough)')
    A2 = input('Type in the move you want to use: ')
    if A2 == 'fireball':
        Value = random.randint(1, 10)
        Value1 = random.randint(10, 50)
        if Value == 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
            print('Fireball Hits!')
            P1.health -= Value1
        elif Value == 10:
            print('Fireball Missed')
        elif Value == 1:
            print('Fireball was Super Affective!')
            Value1 *= 2
            P1.health -= Value1
        print('')
        print(P2.name, '         V.S.        ', P1.name)
        print(P2.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A2 == 'fire fang':
        Value2 = random.randint(10, 30)
        Value9 = random.randint(1, 10)
        if Value9 == 1:
            print('Fire Fang Missed!') 
        elif Value9 == 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10:
            print('Fire Fang Hit!')
            P1.health -= Value2
        elif Value9 == 2:
            print('Fire Fang was Super Affective')
            Value2 *= 2
            P1.health -= Value2 
        print('')
        print(P2.name, '         V.S.        ', P1.name)
        print(P2.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A2 == 'flame thrower':
        Value3 = random.randint(1 ,20)
        Value4 = random.randint(1, 20)
        Value5 = random.randint(1, 20)
        Value6 = random.randint(1, 5)
        if Value6 == 1:
            print('First Burn Missed!')
            Value6 = random.randint(1, 5)
            if Value6 != 2:
                P1.health -= Value3 + Value4 + Value5
                Value6 = 1
            elif Value6 == 2:
                print('Second Burn also Missed')
                Value6 = random.randint(1, 5)
                if Value6 != 3:
                    P1.health -= Value3 + Value4
                    Value6 = 1
                elif Value6 == 3:
                    print('Third Burn Also Missed')
                    Value6 = 1
        elif Value6 == 2 or 3 or 4:
            print('Flame Thrower Hit!')
            P1.health -= Value3
            P1.health -= Value4
            P1.health -= Value5
        elif Value6 == 5:
            print('It was Super Affective')
            Value3 *= 2
            Value4 *= 2
            Value5 *= 2
            P.health -= Value3 + Value4 + Value5
        print('')
        print(P2.name, '         V.S.        ', P1.name)
        print(P2.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A2 == 'life steal':
        print('Life Steal Worked!')
        Value8 = random.randint(10, 30)
        P1.health -= Value8
        Value8 *= 2
        P2.health += Value8
        print('')
        print(P2.name, '         V.S.         ', P1.name)
        print(P2.health,'hp', '                 ', P1.health, 'hp')
        print('')
    else:
        print('Your punishment for not typing correctly. LOSE A TURN!')        
        print('')
        print(P2.name, '         V.S.        ', P1.name)
        print(P2.health,'hp', '                 ', P1.health, 'hp')
        print('')
def H3():
    print('Valid Moves:')
    print('Fireball')
    print('Fire Fang')
    print('Flame Thrower')
    print('Life Steal')
    print('(Cough) Type in all Lowercase (Cough)')
    A2 = input('Type in the move you want to use: ')
    if A2 == 'fireball':
        Value = random.randint(1, 10)
        Value1 = random.randint(10, 50)
        if Value == 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
            print('Fireball Hits!')
            P3.health -= Value1
        elif Value == 10:
            print('Fireball Missed')
        elif Value == 1:
            print('Fireball was Super Affective!')
            Value1 *= 2
            P3.health -= Value1
        print('')
        print(P3.name, '         V.S.        ', P1.name)
        print(P3.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A2 == 'fire fang':
        Value2 = random.randint(10, 30)
        Value9 = random.randint(1, 10)
        if Value9 == 1:
            print('Fire Fang Missed!') 
        elif Value9 == 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10:
            print('Fire Fang Hit!')
            P3.health -= Value2
        elif Value9 == 2:
            print('Fire Fang was Super Affective')
            Value2 *= 2
            P3.health -= Value2 
        print('')
        print(P3.name, '         V.S.        ', P1.name)
        print(P3.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A2 == 'flame thrower':
        Value3 = random.randint(1 ,20)
        Value4 = random.randint(1, 20)
        Value5 = random.randint(1, 20)
        Value6 = random.randint(1, 5)
        if Value6 == 1:
            print('First Burn Missed!')
            Value6 = random.randint(1, 5)
            if Value6 != 2:
                P2.health -= Value3 + Value4 + Value5
                Value6 = 1
            elif Value6 == 2:
                print('Second Burn also Missed')
                Value6 = random.randint(1, 5)
                if Value6 != 3:
                    P2.health -= Value3 + Value4
                    Value6 = 1
                elif Value6 == 3:
                    print('Third Burn Also Missed')
                    Value6 = 1
        elif Value6 == 2 or 3 or 4:
            print('Flame Thrower Hit!')
            P3.health -= Value3
            P3.health -= Value4
            P3.health -= Value5
        elif Value6 == 5:
            print('It was Super Affective')
            Value3 *= 2
            Value4 *= 2
            Value5 *= 2
            P3.health -= Value3 + Value4 + Value5
        print('')
        print(P3.name, '         V.S.        ', P1.name)
        print(P3.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A2 == 'life steal':
        print('Life Steal Worked!')
        Value8 = random.randint(10, 30)
        P3.health -= Value8
        Value8 *= 2
        P1.health += Value8
        print('')
        print(P3.name, '         V.S.         ', P1.name)
        print(P3.health,'hp', '                 ', P1.health, 'hp')
        print('')
    else:
        print('Your punishment for not typing correctly. LOSE A TURN!')        
        print('')
        print(P3.name, '         V.S.        ', P1.name)
        print(P3.health,'hp', '                 ', P1.health, 'hp')
        print('')
def H4():
    print('Valid Moves:')
    print('Fireball')
    print('Fire Fang')
    print('Flame Thrower')
    print('Life Steal')
    print('(Cough) Type in all Lowercase (Cough)')
    A2 = input('Type in the move you want to use: ')
    if A2 == 'fireball':
        Value = random.randint(1, 10)
        Value1 = random.randint(10, 50)
        if Value == 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
            print('Fireball Hits!')
            P3.health -= Value1
        elif Value == 10:
            print('Fireball Missed')
        elif Value == 1:
            print('Fireball was Super Affective!')
            Value1 *= 2
            P3.health -= Value1
        print('')
        print(P2.name, '         V.S.        ', P3.name)
        print(P2.health,'hp', '                 ', P3.health, 'hp')
        print('')
    elif A2 == 'fire fang':
        Value2 = random.randint(10, 30)
        Value9 = random.randint(1, 10)
        if Value9 == 1:
            print('Fire Fang Missed!') 
        elif Value9 == 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10:
            print('Fire Fang Hit!')
            P3.health -= Value2
        elif Value9 == 2:
            print('Fire Fang was Super Affective')
            Value2 *= 2
            P3.health -= Value2 
        print('')
        print(P2.name, '         V.S.        ', P3.name)
        print(P2.health,'hp', '                 ', P3.health, 'hp')
        print('')
    elif A2 == 'flame thrower':
        Value3 = random.randint(1 ,20)
        Value4 = random.randint(1, 20)
        Value5 = random.randint(1, 20)
        Value6 = random.randint(1, 5)
        if Value6 == 1:
            print('First Burn Missed!')
            Value6 = random.randint(1, 5)
            if Value6 != 2:
                P3.health -= Value3 + Value4 + Value5
                Value6 = 1
            elif Value6 == 2:
                print('Second Burn also Missed')
                Value6 = random.randint(1, 5)
                if Value6 != 3:
                    P3.health -= Value3 + Value4
                    Value6 = 1
                elif Value6 == 3:
                    print('Third Burn Also Missed')
                    Value6 = 1
        elif Value6 == 2 or 3 or 4:
            print('Flame Thrower Hit!')
            P3.health -= Value3
            P3.health -= Value4
            P3.health -= Value5
        elif Value6 == 5:
            print('It was Super Affective')
            Value3 *= 2
            Value4 *= 2
            Value5 *= 2
            P3.health -= Value3 + Value4 + Value5
        print('')
        print(P2.name, '         V.S.        ', P3.name)
        print(P2.health,'hp', '                 ', P3.health, 'hp')
        print('')
    elif A2 == 'life steal':
        print('Life Steal Worked!')
        Value8 = random.randint(10, 30)
        P1.health -= Value8
        Value8 *= 2
        P2.health += Value8
        print('')
        print(P2.name, '         V.S.         ', P1.name)
        print(P2.health,'hp', '                 ', P1.health, 'hp')
        print('')
    else:
        print('Your punishment for not typing correctly. LOSE A TURN!')        
        print('')
        print(P2.name, '         V.S.        ', P1.name)
        print(P2.health,'hp', '                 ', P1.health, 'hp')
        print('')
def H5():
    print('Valid Moves:')
    print('Fireball')
    print('Fire Fang')
    print('Flame Thrower')
    print('Life Steal')
    print('(Cough) Type in all Lowercase (Cough)')
    A2 = input('Type in the move you want to use: ')
    if A2 == 'fireball':
        Value = random.randint(1, 10)
        Value1 = random.randint(10, 50)
        if Value == 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
            print('Fireball Hits!')
            P1.health -= Value1
        elif Value == 10:
            print('Fireball Missed')
        elif Value == 1:
            print('Fireball was Super Affective!')
            Value1 *= 2
            P1.health -= Value1
        print('')
        print(P3.name, '         V.S.        ', P1.name)
        print(P3.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A2 == 'fire fang':
        Value2 = random.randint(10, 30)
        Value9 = random.randint(1, 10)
        if Value9 == 1:
            print('Fire Fang Missed!') 
        elif Value9 == 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10:
            print('Fire Fang Hit!')
            P1.health -= Value2
        elif Value9 == 2:
            print('Fire Fang was Super Affective')
            Value2 *= 2
            P1.health -= Value2 
        print('')
        print(P3.name, '         V.S.        ', P1.name)
        print(P3.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A2 == 'flame thrower':
        Value3 = random.randint(1 ,20)
        Value4 = random.randint(1, 20)
        Value5 = random.randint(1, 20)
        Value6 = random.randint(1, 5)
        if Value6 == 1:
            print('First Burn Missed!')
            Value6 = random.randint(1, 5)
            if Value6 != 2:
                P2.health -= Value3 + Value4 + Value5
                Value6 = 1
            elif Value6 == 2:
                print('Second Burn also Missed')
                Value6 = random.randint(1, 5)
                if Value6 != 3:
                    P2.health -= Value3 + Value4
                    Value6 = 1
                elif Value6 == 3:
                    print('Third Burn Also Missed')
                    Value6 = 1
        elif Value6 == 2 or 3 or 4:
            print('Flame Thrower Hit!')
            P1.health -= Value3
            P1.health -= Value4
            P1.health -= Value5
        elif Value6 == 5:
            print('It was Super Affective')
            Value3 *= 2
            Value4 *= 2
            Value5 *= 2
            P.health -= Value3 + Value4 + Value5
        print('')
        print(P3.name, '         V.S.        ', P1.name)
        print(P3.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A2 == 'life steal':
        print('Life Steal Worked!')
        Value8 = random.randint(10, 30)
        P1.health -= Value8
        Value8 *= 2
        P3.health += Value8
        print('')
        print(P3.name, '         V.S.         ', P1.name)
        print(P3.health,'hp', '                 ', P1.health, 'hp')
        print('')
    else:
        print('Your punishment for not typing correctly. LOSE A TURN!')        
        print('')
        print(P3.name, '         V.S.        ', P1.name)
        print(P3.health,'hp', '                 ', P1.health, 'hp')
        print('')
def H6():
    print('Valid Moves:')
    print('Fireball')
    print('Fire Fang')
    print('Flame Thrower')
    print('Life Steal')
    print('(Cough) Type in all Lowercase (Cough)')
    A2 = input('Type in the move you want to use: ')
    if A2 == 'fireball':
        Value = random.randint(1, 10)
        Value1 = random.randint(10, 50)
        if Value == 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
            print('Fireball Hits!')
            P2.health -= Value1
        elif Value == 10:
            print('Fireball Missed')
        elif Value == 1:
            print('Fireball was Super Affective!')
            Value1 *= 2
            P2.health -= Value1
        print('')
        print(P2.name, '         V.S.        ', P3.name)
        print(P2.health,'hp', '                 ', P3.health, 'hp')
        print('')
    elif A2 == 'fire fang':
        Value2 = random.randint(10, 30)
        Value9 = random.randint(1, 10)
        if Value9 == 1:
            print('Fire Fang Missed!')
        elif Value9 == 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10:
            print('Fire Fang Hit!')
            P2.health -= Value2 
        elif Value9 == 2:
            print('Fire Fang was Super Affective')
            Value2 *= 2
            P2.health -= Value2 
        print('')
        print(P2.name, '         V.S.        ', P3.name)
        print(P2.health,'hp', '                 ', P3.health, 'hp')
        print('')
    elif A2 == 'flame thrower':
        Value3 = random.randint(1 ,20)
        Value4 = random.randint(1, 20)
        Value5 = random.randint(1, 20)
        Value6 = random.randint(1, 5)
        if Value6 == 1:
            print('First Burn Missed!')
            Value6 = random.randint(1, 5)
            if Value6 != 2:
                P2.health -= Value3 + Value4 + Value5
                Value6 = 1
            elif Value6 == 2:
                print('Second Burn also Missed')
                Value6 = random.randint(1, 5)
                if Value6 != 3:
                    P2.health -= Value3 + Value4
                    Value6 = 1
                elif Value6 == 3:
                    print('Third Burn Also Missed')
                    Value6 = 1
        elif Value6 == 2 or 3 or 4:
            print('Flame Thrower Hit!')
        elif Value6 == 5:
            print('It was Super Affective')
            Value3 *= 2
            Value4 *= 2
            Value5 *= 2
            P2.health -= Value3 + Value4 + Value5
        print('')
        print(P2.name, '         V.S.        ', P3.name)
        print(P2.health,'hp', '                 ', P3.health, 'hp')
        print('')
    elif A2 == 'life steal':
        print('Life Steal Worked!')
        Value8 = random.randint(10, 30)
        P2.health -= Value8
        Value8 *= 2
        P3.health += Value8
        print('')
        print(P2.name, '         V.S.         ', P3.name)
        print(P2.health,'hp', '                 ', P3.health, 'hp')
        print('')
    else:
        print('Your punishment for not typing correctly. LOSE A TURN!')        
        print('')
        print(P2.name, '         V.S.        ', P3.name)
        print(P2.health,'hp', '                 ', P3.health, 'hp')
        print('')
#//////////////////////////////////////////////////////////////////////////
def T():
    print('Valid Moves:')
    print('Electro Punch')
    print('Thunder Shock')
    print('Obsorb')
    print('Thunder Wave')
    print('(Cough) Type in all Lowercase (Cough)')
    A1 = input('Type in the move you want to use:  ')
    if A1 == 'electro punch':
        value1 = random.randint(1, 10)
        value2 = random.randint(1, 40)
        if value1 == 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
            print('Electro Punch Hits!')
            P1.health -= value2
        elif value1 == 1:
            print('It was super affective!')
            value2 *= 2
            P1.health -= value2
        elif value1 == 10:
            print('Electro Punch Missed!')
        print('')
        print(P2.name, '         V.S.        ', P1.name)
        print(P2.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A1 == 'thunder shock':
        value3 = random.randint(1,5)
        value4 = random.randint(1, 24)
        if value3 == 2 or 3 or 4 or 5:
            print('Thunder Shock Hits!')
            P1.health -= value4
        elif value3 == 1:
            print('It was super affective')
            value4 *= 2
            P1.health -= value4
        elif value3 == 5:
            print('Thunder Shock Missed')
        print('')
        print(P2.name, '         V.S.        ', P1.name)
        print(P2.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A1 == "obsorb":
        print('Obsorb Worked!')
        value5 = random.randint(10, 30)
        P1.health -= value5
        value5 *= 2
        P2.health += value5
        print('')
        print(P2.name, '         V.S.        ', P1.name)
        print(P2.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A1 == 'thunder wave':
        value6 = random.randint(1, 10)
        value8 = 100
        if value6 == 1 or 6 or 7 or 8 or 9:
            print('Thunder Wave Hits!')
            P1.health -= value8
        elif value6 == 2 or 3 or 4 or 5:
            print('Thunder Wave Missed!')
        elif value6 == 10:
            P1.health -= value8
            print('It was Super Affective!')
            value8 *= 2
            P1.health -= value8
        print('')
        print(P2.name, '         V.S.        ', P1.name)
        print(P2.health,'hp', '                 ', P1.health, 'hp')
        print('')
    else:
        print('Your punishment for not typing correctly. LOSE A TURN!')
        print('')
        print(P2.name, '         V.S.        ', P1.name)
        print(P2.health,'hp', '                 ', P1.health, 'hp')
        print('')
def T1():
    print('Valid Moves:')
    print('Electro Punch')
    print('Thunder Shock')
    print('Obsorb')
    print('Thunder Wave')
    print('(Cough) Type in all Lowercase (Cough)')
    A1 = input('Type in the move you want to use:  ')
    if A1 == 'electro punch':
        value1 = random.randint(1, 10)
        value2 = random.randint(1, 40)
        if value1 == 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
            print('Electro Punch Hits!')
            C.health -= value2
        elif value1 == 1:
            print('It was super affective!')
            value2 *= 2
            C.health -= value2
        elif value1 == 10:
            print('Electro Punch Missed!')
        print('')
        print(C.name, '         V.S.        ', P1.name)
        print(C.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A1 == 'thunder shock':
        value3 = random.randint(1,5)
        value4 = random.randint(1, 24)
        if value3 == 2 or 3 or 4 or 5:
            print('Thunder Shock Hits!')
            C.health -= value4
        elif value3 == 1:
            print('It was super affective')
            value4 *= 2
            C.health -= value4
        elif value3 == 5:
            print('Thunder Shock Missed')
        print('')
        print(C.name, '         V.S.        ', P1.name)
        print(C.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A1 == "obsorb":
        print('Obsorb Worked!')
        value5 = random.randint(10, 30)
        C.health -= value5
        value5 *= 2
        P1.health += value5
        print('')
        print(C.name, '         V.S.        ', P1.name)
        print(C.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A1 == 'thunder wave':
        value6 = random.randint(1, 10)
        value8 = 100
        if value6 == 1 or 6 or 7 or 8 or 9:
            print('Thunder Wave Hits!')
            C.health -= value8
        elif value6 == 2 or 3 or 4 or 5:
            print('Thunder Wave Missed!')
        elif value6 == 10:
            print('It was Super Affective!')
            value8 *= 2
            C.health -= value8
        print('')
        print(C.name, '         V.S.        ', P1.name)
        print(C.health,'hp', '                 ', P1.health, 'hp')
        print('')
    else:
        print('Your punishment for not typing correctly. LOSE A TURN!')
        print('')
        print(C.name, '         V.S.        ', P1.name)
        print(C.health,'hp', '                 ', P1.health, 'hp')
        print('')
def T2():
    print('Valid Moves:')
    print('Electro Punch')
    print('Thunder Shock')
    print('Obsorb')
    print('Thunder Wave')
    print('(Cough) Type in all Lowercase (Cough)')
    A1 = input('Type in the move you want to use:  ')
    if A1 == 'electro punch':
        value1 = random.randint(1, 10)
        value2 = random.randint(1, 40)
        if value1 == 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
            print('Electro Punch Hits!')
            P2.health -= value2
        elif value1 == 1:
            print('It was super affective!')
            value2 *= 2
            P2.health -= value2
        elif value1 == 10:
            print('Electro Punch Missed!')
        print('')
        print(P2.name, '         V.S.        ', P1.name)
        print(P2.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A1 == 'thunder shock':
        value3 = random.randint(1,5)
        value4 = random.randint(1, 24)
        if value3 == 2 or 3 or 4 or 5:
            print('Thunder Shock Hits!')
            P2.health -= value4
        elif value3 == 1:
            print('It was super affective')
            value4 *= 2
            P2.health -= value4
        elif value3 == 5:
            print('Thunder Shock Missed')
        print('')
        print(P2.name, '         V.S.        ', P1.name)
        print(P2.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A1 == "obsorb":
        print('Obsorb Worked!')
        value5 = random.randint(10, 30)
        P2.health -= value5
        value5 *= 2
        P1.health += value5
        print('')
        print(P2.name, '         V.S.        ', P1.name)
        print(P2.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A1 == 'thunder wave':
        value6 = random.randint(1, 10)
        value8 = 100
        if value6 == 1 or 6 or 7 or 8 or 9:
            print('Thunder Wave Hits!')
            P2.health -= value8
        elif value6 == 2 or 3 or 4 or 5:
            print('Thunder Wave Missed!')
        elif value6 == 10:
            print('It was Super Affective!')
            value8 *= 2
            P2.health -= value8
        print('')
        print(P2.name, '         V.S.        ', P1.name)
        print(P2.health,'hp', '                 ', P1.health, 'hp')
        print('')
    else:
        print('Your punishment for not typing correctly. LOSE A TURN!')
        print('')
        print(P2.name, '         V.S.        ', P1.name)
        print(P2.health,'hp', '                 ', P1.health, 'hp')
        print('')
def T3():
    print('Valid Moves:')
    print('Electro Punch')
    print('Thunder Shock')
    print('Obsorb')
    print('Thunder Wave')
    print('(Cough) Type in all Lowercase (Cough)')
    A1 = input('Type in the move you want to use:  ')
    if A1 == 'electro punch':
        value1 = random.randint(1, 10)
        value2 = random.randint(1, 40)
        if value1 == 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
            print('Electro Punch Hits!')
            P3.health -= value2
        elif value1 == 1:
            print('It was super affective!')
            value2 *= 2
            P3.health -= value2
        elif value1 == 10:
            print('Electro Punch Missed!')
        print('')
        print(P3.name, '         V.S.        ', P1.name)
        print(P3.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A1 == 'thunder shock':
        value3 = random.randint(1,5)
        value4 = random.randint(1, 24)
        if value3 == 2 or 3 or 4 or 5:
            print('Thunder Shock Hits!')
            P3.health -= value4
        elif value3 == 1:
            print('It was super affective')
            value4 *= 2
            P3.health -= value4
        elif value3 == 5:
            print('Thunder Shock Missed')
        print('')
        print(P2.name, '         V.S.        ', P1.name)
        print(P2.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A1 == "obsorb":
        print('Obsorb Worked!')
        value5 = random.randint(10, 30)
        P3.health -= value5
        value5 *= 2
        P1.health += value5
        print('')
        print(P3.name, '         V.S.        ', P1.name)
        print(P3.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A1 == 'thunder wave':
        value6 = random.randint(1, 10)
        value8 = 100
        if value6 == 1 or 6 or 7 or 8 or 9:
            print('Thunder Wave Hits!')
            P3.health -= value8
        elif value6 == 2 or 3 or 4 or 5:
            print('Thunder Wave Missed!')
        elif value6 == 10:
            print('It was Super Affective!')
            value8 *= 2
            P3.health -= value8
        print('')
        print(P3.name, '         V.S.        ', P1.name)
        print(P3.health,'hp', '                 ', P1.health, 'hp')
        print('')
    else:
        print('Your punishment for not typing correctly. LOSE A TURN!')
        print('')
        print(P3.name, '         V.S.        ', P1.name)
        print(P3.health,'hp', '                 ', P1.health, 'hp')
        print('')
def T4():
    print('Valid Moves:')
    print('Electro Punch')
    print('Thunder Shock')
    print('Obsorb')
    print('Thunder Wave')
    print('(Cough) Type in all Lowercase (Cough)')
    A1 = input('Type in the move you want to use:  ')
    if A1 == 'electro punch':
        value1 = random.randint(1, 10)
        value2 = random.randint(1, 40)
        if value1 == 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
            print('Electro Punch Hits!')
            P3.health -= value2
        elif value1 == 1:
            print('It was super affective!')
            value2 *= 2
            P3.health -= value2
        elif value1 == 10:
            print('Electro Punch Missed!')
        print('')
        print(P2.name, '         V.S.        ', P3.name)
        print(P2.health,'hp', '                 ', P3.health, 'hp')
        print('')
    elif A1 == 'thunder shock':
        value3 = random.randint(1,5)
        value4 = random.randint(1, 24)
        if value3 == 2 or 3 or 4 or 5:
            print('Thunder Shock Hits!')
            P3.health -= value4
        elif value3 == 1:
            print('It was super affective')
            value4 *= 2
            P3.health -= value4
        elif value3 == 5:
            print('Thunder Shock Missed')
        print('')
        print(P2.name, '         V.S.        ', P3.name)
        print(P2.health,'hp', '                 ', P3.health, 'hp')
        print('')
    elif A1 == "obsorb":
        print('Obsorb Worked!')
        value5 = random.randint(10, 30)
        P3.health -= value5
        value5 *= 2
        P2.health += value5
        print('')
        print(P2.name, '         V.S.        ', P3.name)
        print(P2.health,'hp', '                 ', P3.health, 'hp')
        print('')
    elif A1 == 'thunder wave':
        value6 = random.randint(1, 10)
        value8 = 100
        if value6 == 1 or 6 or 7 or 8 or 9:
            print('Thunder Wave Hits!')
            P3.health -= value8
        elif value6 == 2 or 3 or 4 or 5:
            print('Thunder Wave Missed!')
        elif value6 == 10:
            P3.health -= value8
            print('It was Super Affective!')
            value8 *= 2
            P3.health -= value8
        print('')
        print(P2.name, '         V.S.        ', P3.name)
        print(P2.health,'hp', '                 ', P3.health, 'hp')
        print('')
    else:
        print('Your punishment for not typing correctly. LOSE A TURN!')
        print('')
        print(P2.name, '         V.S.        ', P3.name)
        print(P2.health,'hp', '                 ', P3.health, 'hp')
        print('')
def T5():
    print('Valid Moves:')
    print('Electro Punch')
    print('Thunder Shock')
    print('Obsorb')
    print('Thunder Wave')
    print('(Cough) Type in all Lowercase (Cough)')
    A1 = input('Type in the move you want to use:  ')
    if A1 == 'electro punch':
        value1 = random.randint(1, 10)
        value2 = random.randint(1, 40)
        if value1 == 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
            print('Electro Punch Hits!')
            P1.health -= value2
        elif value1 == 1:
            print('It was super affective!')
            value2 *= 2
            P1.health -= value2
        elif value1 == 10:
            print('Electro Punch Missed!')
        print('')
        print(P3.name, '         V.S.        ', P1.name)
        print(P3.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A1 == 'thunder shock':
        value3 = random.randint(1,5)
        value4 = random.randint(1, 24)
        if value3 == 2 or 3 or 4 or 5:
            print('Thunder Shock Hits!')
            P1.health -= value4
        elif value3 == 1:
            print('It was super affective')
            value4 *= 2
            P1.health -= value4
        elif value3 == 5:
            print('Thunder Shock Missed')
        print('')
        print(P3.name, '         V.S.        ', P1.name)
        print(P3.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A1 == "obsorb":
        print('Obsorb Worked!')
        value5 = random.randint(10, 30)
        P1.health -= value5
        value5 *= 2
        P3.health += value5
        print('')
        print(P3.name, '         V.S.        ', P1.name)
        print(P3.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A1 == 'thunder wave':
        value6 = random.randint(1, 10)
        value8 = 100
        if value6 == 1 or 6 or 7 or 8 or 9:
            print('Thunder Wave Hits!')
            P1.health -= value8
        elif value6 == 2 or 3 or 4 or 5:
            print('Thunder Wave Missed!')
        elif value6 == 10:
            P1.health -= value8
            print('It was Super Affective!')
            value8 *= 2
            P1.health -= value8
        print('')
        print(P3.name, '         V.S.        ', P1.name)
        print(P3.health,'hp', '                 ', P1.health, 'hp')
        print('')
    else:
        print('Your punishment for not typing correctly. LOSE A TURN!')
        print('')
        print(P3.name, '         V.S.        ', P1.name)
        print(P3.health,'hp', '                 ', P1.health, 'hp')
        print('')
def T6():
    print('Valid Moves:')
    print('Electro Punch')
    print('Thunder Shock')
    print('Obsorb')
    print('Thunder Wave')
    print('(Cough) Type in all Lowercase (Cough)')
    A1 = input('Type in the move you want to use:  ')
    if A1 == 'electro punch':
        value1 = random.randint(1, 10)
        value2 = random.randint(1, 40)
        if value1 == 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
            print('Electro Punch Hits!')
            P2.health -= value2
        elif value1 == 1:
            print('It was super affective!')
            value2 *= 2
            P2.health -= value2
        elif value1 == 10:
            print('Electro Punch Missed!')
        print('')
        print(P2.name, '         V.S.        ', P3.name)
        print(P2.health,'hp', '                 ', P3.health, 'hp')
        print('')
    elif A1 == 'thunder shock':
        value3 = random.randint(1,5)
        value4 = random.randint(1, 24)
        if value3 == 2 or 3 or 4 or 5:
            print('Thunder Shock Hits!')
            P2.health -= value4
        elif value3 == 1:
            print('It was super affective')
            value4 *= 2
            P2.health -= value4
        elif value3 == 5:
            print('Thunder Shock Missed')
        print('')
        print(P2.name, '         V.S.        ', P3.name)
        print(P2.health,'hp', '                 ', P3.health, 'hp')
        print('')
    elif A1 == "obsorb":
        print('Obsorb Worked!')
        value5 = random.randint(10, 30)
        P2.health -= value5
        value5 *= 2
        P3.health += value5
        print('')
        print(P2.name, '         V.S.        ', P3.name)
        print(P2.health,'hp', '                 ', P3.health, 'hp')
        print('')
    elif A1 == 'thunder wave':
        value6 = random.randint(1, 10)
        value8 = 100
        if value6 == 1 or 6 or 7 or 8 or 9:
            print('Thunder Wave Hits!')
            P2.health -= value8
        elif value6 == 2 or 3 or 4 or 5:
            print('Thunder Wave Missed!')
        elif value6 == 10:
            print('It was Super Affective!')
            value8 *= 2
            P2.health -= value8
        print('')
        print(P2.name, '         V.S.        ', P3.name)
        print(P2.health,'hp', '                 ', P3.health, 'hp')
        print('')
    else:
        print('Your punishment for not typing correctly. LOSE A TURN!')
        print('')
        print(P2.name, '         V.S.        ', P3.name)
        print(P2.health,'hp', '                 ', P3.health, 'hp')
        print('')
#///////////////////////////////////////////////////////////////////////////
def G():
    # Moves are Giga Drain, Frenzy Plant, Leaf Storm, and Razor Leaf
    print('Valid Moves:')
    print('Giga Drain')
    print('Frenzy Plant')
    print('Leaf Storm')
    print('Razor Leaf')
    print('(Type everything in lowercase)')
    A4 = input('What move do you want to use: ')
    if A4 == 'giga drain':
        v1 = random.randint(30, 70)
        v2 =  random.randint(1, 5)
        if v2 == 1 or 2 or 3:
            print('Giga Drain Hit!')
            P2.health -= v1
            P1.health += v1
        elif v2 == 4:
            print('It was super affective')
            v1 *= 2
            P2.health -= v1
            P1.health += v1
        elif v2 == 5:
            print('Giga Drain Missed!')
        print('')
        print(P2.name, '         V.S.        ', P1.name)
        print(P2.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A4 == 'frenzy plant':
        v3 = random.randint(1, 10)
        v4 = random.randint(1, 10)
        v5 = random.randint(1, 10)
        v6 = random.randint(1, 10)
        v7 = random.randint(1, 10)
        v8 = random.randint(1, 5)
        if v8 == 1:
            print('First Chomp Missed!')
            v8 = random.randint(1, 5)
            if v8 != 2:
                P2.health -= v4 + v5 + v6 + v7
                v8 = 1
            elif v8 == 2:
                print('Second Chomp Missed!')
                v8 = random.randint(1, 5)
                if v8 != 3:
                    P2.health -= v5 + v6 + v7
                    v8 = 1
                elif v8 == 3:
                    print('Third Chomp Missed!')
                    v8 = random.randint(1, 5)
                    if v8 != 4:
                        P2.health -= v6 + v7
                        v8 = 1
                    elif v8 == 4:
                        print('Fourth Chomp Missed!')
                        v8 = random.randint(1, 5)
                        if v8 != 5:
                            P2.health -= v7
                            v8 = 1
                        elif v8 == 5:
                            print('All Chomps Missed!')
                            v8 = 1
        elif v8 == 2 or 3 or 4:
            print('Frenzy Plant Hit!')
            P2.health -= v3 + v4 + v5 + v6 +v7
        elif v8 == 5:
            print('It was Super Affective')
            v3 *= 2
            v4 *= 2
            v5 *= 2
            v6 *= 2
            v7 *= 2
            P2.health -= v3 + v4 + v5 + v6 +v7
        print('')
        print(P2.name, '         V.S.        ', P1.name)
        print(P2.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A4 == 'leaf storm':
        v9 = random.randint(1, 50)
        v10 = random.randint(1, 10)
        if v10 == 1:
            print('Leaf Storm Missed!')
        if v10 == 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
            print('Leaf Storm Hit!')
            P2.health =- v9
        if v10 == 10:
            print('It was Super Affective')
            v9 *= 2
            P2.health =- v9
        print('')
        print(P2.name, '         V.S.        ', P1.name)
        print(P2.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A4 == 'razor leaf':
        v11 = random.randint(10, 60)
        v12 = random.randint(1, 10)
        if v12 == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8:
            print('Razor Leaf Hit!')
            P2.health -= v11
        elif v12 == 9:
            print('Razor Leaf Missed!')
        elif v12 == 10:
            print('It was Super Affective!')
            v11 *= 2
            P2.health -= v11
        print('')
        print(P2.name, '         V.S.        ', P1.name)
        print(P2.health,'hp', '                 ', P1.health, 'hp')
        print('')
    else:
        print('Your punishment for not typing correctly. LOSE A TURN!')
        print('')
        print(P2.name, '         V.S.        ', P1.name)
        print(P2.health,'hp', '                 ', P1.health, 'hp')
        print('')
def G1():
    # Moves are Giga Drain, Frenzy Plant, Leaf Storm, and Razor Leaf
    print('Valid Moves:')
    print('Giga Drain')
    print('Frenzy Plant')
    print('Leaf Storm')
    print('Razor Leaf')
    print('(Type everything in lowercase)')
    A4 = input('What move do you want to use: ')
    if A4 == 'giga drain':
        v1 = random.randint(30, 70)
        v2 =  random.randint(1, 5)
        if v2 == 1 or 2 or 3:
            print('Giga Drain Hit!')
            C.health -= v1
            P1.health += v1
        elif v2 == 4:
            print('It was super affective')
            v2 *= 2
            C.health -= v1
            P1.health += v1
        elif v2 == 5:
            print('Giga Drain Missed!')
        print('')
        print(C.name, '         V.S.        ', P1.name)
        print(C.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A4 == 'frenzy plant':
        v3 = random.randint(1, 10)
        v4 = random.randint(1, 10)
        v5 = random.randint(1, 10)
        v6 = random.randint(1, 10)
        v7 = random.randint(1, 10)
        v8 = random.randint(1, 5)
        if v8 == 1:
            print('First Chomp Missed!')
            v8 = random.randint(1, 5)
            if v8 != 2:
                C.health -= v4 + v5 + v6 + v7
                v8 = 1
            elif v8 == 2:
                print('Second Chomp Missed!')
                v8 = random.randint(1, 5)
                if v8 != 3:
                    C.health -= v5 + v6 + v7
                    v8 = 1
                elif v8 == 3:
                    print('Third Chomp Missed!')
                    v8 = random.randint(1, 5)
                    if v8 != 4:
                        C.health -= v6 + v7
                        v8 = 1
                    elif v8 == 4:
                        print('Fourth Chomp Missed!')
                        v8 = random.randint(1, 5)
                        if v8 != 5:
                            C.health -= v7
                            v8 = 1
                        elif v8 == 5:
                            print('All Chomps Missed!')
                            v8 = 1
        elif v8 == 2 or 3 or 4:
            print('Frenzy Plant Hit!')
            C.health -= v3 + v4 + v5 + v6 +v7
        elif v8 == 5:
            print('It was Super Affective')
            v3 *= 2
            v4 *= 2
            v5 *= 2
            v6 *= 2
            v7 *= 2
            C.health -= v3 + v4 + v5 + v6 +v7
        print('')
        print(C.name, '         V.S.        ', P1.name)
        print(C.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A4 == 'leaf storm':
        v9 = random.randint(1, 50)
        v10 = random.randint(1, 10)
        if v10 == 1:
            print('Leaf Storm Missed!')
        elif v10 == 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
            print('Leaf Storm Hit!')
            C.health -= v9
        elif v10 == 10:
            print('It was Super Affective')
            v9 *= 2
            C.health -= v9
        print('')
        print(C.name, '         V.S.        ', P1.name)
        print(C.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A4 == 'razor leaf':
        v11 = random.randint(10, 60)
        v12 = random.randint(1, 10)
        if v12 == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8:
            print('Razor Leaf Hit!')
            C.health -= v11
        elif v12 == 9:
            print('Razor Leaf Missed!')
        elif v12 == 10:
            print('It was Super Affective!')
            v11 *= 2
            C.health -= v11
        print('')
        print(C.name, '         V.S.        ', P1.name)
        print(C.health,'hp', '                 ', P1.health, 'hp')
        print('')
    else:
        print('Your punishment for not typing correctly. LOSE A TURN!')
        print('')
        print(C. name, '         V.S.        ', P1.name)
        print(C.health,'hp', '                 ', P1.health, 'hp')
        print('')
def G2():
    # Moves are Giga Drain, Frenzy Plant, Leaf Storm, and Razor Leaf
    print('Valid Moves:')
    print('Giga Drain')
    print('Frenzy Plant')
    print('Leaf Storm')
    print('Razor Leaf')
    print('(Type everything in lowercase)')
    A4 = input('What move do you want to use: ')
    if A4 == 'giga drain':
        v1 = random.randint(30, 70)
        v2 =  random.randint(1, 5)
        if v2 == 1 or 2 or 3:
            print('Giga Drain Hit!')
            P1.health -= v1
            P2.health += v1
        elif v2 == 4:
            print('It was super affective')
            v1 *= 2
            P1.health -= v1
            P2.health += v1
        elif v2 == 5:
            print('Giga Drain Missed!')
        print('')
        print(P2.name, '         V.S.        ', P1.name)
        print(P2.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A4 == 'frenzy plant':
        v3 = random.randint(1, 10)
        v4 = random.randint(1, 10)
        v5 = random.randint(1, 10)
        v6 = random.randint(1, 10)
        v7 = random.randint(1, 10)
        v8 = random.randint(1, 5)
        if v8 == 1:
            print('First Chomp Missed!')
            v8 = random.randint(1, 5)
            if v8 != 2:
                P1.health -= v4 + v5 + v6 + v7
                v8 = 1
            elif v8 == 2:
                print('Second Chomp Missed!')
                v8 = random.randint(1, 5)
                if v8 != 3:
                    P1.health -= v5 + v6 + v7
                    v8 = 1
                elif v8 == 3:
                    print('Third Chomp Missed!')
                    v8 = random.randint(1, 5)
                    if v8 != 4:
                        P1.health -= v6 + v7
                        v8 = 1
                    elif v8 == 4:
                        print('Fourth Chomp Missed!')
                        v8 = random.randint(1, 5)
                        if v8 != 3:
                            P1.health -= v7
                            v8 = 1
                        elif v8 == 5:
                            print('All Chomps Missed!')
                            V8 = 1
        elif v8 == 2 or 3 or 4:
            print('Frenzy Plant Hit!')
            P1.health -= v3 + v4 + v5 + v6 +v7
        elif v8 == 5:
            print('It was Super Affective')
            v3 *= 2
            v4 *= 2
            v5 *= 2
            v6 *= 2
            v7 *= 2
            P1.health -= v3 + v4 + v5 + v6 +v7
        print('')
        print(P2.name, '         V.S.        ', P1.name)
        print(P2.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A4 == 'leaf storm':
        v9 = random.randint(1, 50)
        v10 = random.randint(1, 10)
        if v10 == 1:
            print('Leaf Storm Missed!')
        if v10 == 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
            print('Leaf Storm Hit!')
            P1.health =- v9
        if v10 == 10:
            print('It was Super Affective')
            v9 *= 2
            P1.health =- v9
        print('')
        print(P2.name, '         V.S.        ', P1.name)
        print(P2.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A4 == 'razor leaf':
        v11 = random.randint(10, 60)
        v12 = random.randint(1, 10)
        if v12 == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8:
            print('Razor Leaf Hit!')
            P1.health -= v11
        elif v12 == 9:
            print('Razor Leaf Missed!')
        elif v12 == 10:
            print('It was Super Affective!')
            v11 *= 2
            P1.health -= v11
        print('')
        print(P2.name, '         V.S.        ', P1.name)
        print(P2.health,'hp', '                 ', P1.health, 'hp')
        print('')
    else:
        print('Your punishment for not typing correctly. LOSE A TURN!')
        print('')
        print(P2.name, '         V.S.        ', P1.name)
        print(P2.health,'hp', '                 ', P1.health, 'hp')
        print('')
def G3():
    # Moves are Giga Drain, Frenzy Plant, Leaf Storm, and Razor Leaf
    print('Valid Moves:')
    print('Giga Drain')
    print('Frenzy Plant')
    print('Leaf Storm')
    print('Razor Leaf')
    print('(Type everything in lowercase)')
    A4 = input('What move do you want to use: ')
    if A4 == 'giga drain':
        v1 = random.randint(30, 70)
        v2 =  random.randint(1, 5)
        if v2 == 1 or 2 or 3:
            print('Giga Drain Hit!')
            P3.health -= v1
            P1.health += v1
        elif v2 == 4:
            print('It was super affective')
            v1 *= 2
            P3.health -= v1
            P1.health += v1
        elif v2 == 5:
            print('Giga Drain Missed!')
        print('')
        print(P3.name, '         V.S.        ', P1.name)
        print(P3.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A4 == 'frenzy plant':
        v3 = random.randint(1, 10)
        v4 = random.randint(1, 10)
        v5 = random.randint(1, 10)
        v6 = random.randint(1, 10)
        v7 = random.randint(1, 10)
        v8 = random.randint(1, 5)
        if v8 == 1:
            print('First Chomp Missed!')
            v8 = random.randint(1, 5)
            if v8 != 2:
                P3.health -= v4 + v5 + v6 + v7
                v8 = 1
            elif v8 == 2:
                print('Second Chomp Missed!')
                v8 = random.randint(1, 5)
                if v8 != 3:
                    P3.health -= v5 + v6 + v7
                    v8 = 1
                elif v8 == 3:
                    print('Third Chomp Missed!')
                    v8 = random.randint(1, 5)
                    if v8 != 4:
                        P3.health -= v6 + v7
                        v8 = 1
                    elif v8 == 4:
                        print('Fourth Chomp Missed!')
                        v8 = random.randint(1, 5)
                        if v8 != 2:
                            P3.health -= v7
                            v8 = 1
                        elif v8 == 5:
                            print('All Chomps Missed!')
                            v8 = 1
        elif v8 == 2 or 3 or 4:
            print('Frenzy Plant Hit!')
            P3.health -= v3 + v4 + v5 + v6 +v7
        elif v8 == 5:
            print('It was Super Affective')
            v3 *= 2
            v4 *= 2
            v5 *= 2
            v6 *= 2
            v7 *= 2
            P3.health -= v3 + v4 + v5 + v6 +v7
        print('')
        print(P3.name, '         V.S.        ', P1.name)
        print(P3.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A4 == 'leaf storm':
        v9 = random.randint(1, 50)
        v10 = random.randint(1, 10)
        if v10 == 1:
            print('Leaf Storm Missed!')
        if v10 == 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
            print('Leaf Storm Hit!')
            P3.health =- v9
        if v10 == 10:
            print('It was Super Affective')
            v9 *= 2
            P3.health =- v9
        print('')
        print(P3.name, '         V.S.        ', P1.name)
        print(P3.health,'hp', '                 ', P1.health, 'hp')
        print('')
        
    elif A4 == 'razor leaf':
        v11 = random.randint(10, 60)
        v12 = random.randint(1, 10)
        if v12 == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8:
            print('Razor Leaf Hit!')
            P3.health -= v11
        elif v12 == 9:
            print('Razor Leaf Missed!')
        elif v12 == 10:
            print('It was Super Affective!')
            v11 *= 2
            P3.health -= v11
        print('')
        print(P3.name, '         V.S.        ', P1.name)
        print(P3.health,'hp', '                 ', P1.health, 'hp')
        print('')
    else:
        print('Your punishment for not typing correctly. LOSE A TURN!')
        print('')
        print(P3.name, '         V.S.        ', P1.name)
        print(P3.health,'hp', '                 ', P1.health, 'hp')
        print('')
def G4():
    # Moves are Giga Drain, Frenzy Plant, Leaf Storm, and Razor Leaf
    print('Valid Moves:')
    print('Giga Drain')
    print('Frenzy Plant')
    print('Leaf Storm')
    print('Razor Leaf')
    print('(Type everything in lowercase)')
    A4 = input('What move do you want to use: ')
    if A4 == 'giga drain':
        v1 = random.randint(30, 70)
        v2 =  random.randint(1, 5)
        if v2 == 1 or 2 or 3:
            print('Giga Drain Hit!')
            P3.health -= v1
            P2.health += v1
        elif v2 == 4:
            print('It was super affective')
            v1 *= 2
            P3.health -= v1
            P2.health += v1
        elif v2 == 5:
            print('Giga Drain Missed!')
        print('')
        print(P2.name, '         V.S.        ', P3.name)
        print(P2.health,'hp', '                 ', P3.health, 'hp')
        print('')
    elif A4 == 'frenzy plant':
        v3 = random.randint(1, 10)
        v4 = random.randint(1, 10)
        v5 = random.randint(1, 10)
        v6 = random.randint(1, 10)
        v7 = random.randint(1, 10)
        v8 = random.randint(1, 5)
        if v8 == 1:
            print('First Chomp Missed!')
            v8 = random.randint(1, 5)
            if v8 != 2:
                P3.health -= v4 + v5 + v6 + v7
                v8 = 1
            elif v8 == 2:
                print('Second Chomp Missed!')
                v8 = random.randint(1, 5)
                if v8 != 3:
                    P3.health -= v5 + v6 + v7
                    v8 = 1
                elif v8 == 3:
                    print('Third Chomp Missed!')
                    v8 = random.randint(1, 5)
                    if v8 != 4:
                        P3.health -= v6 + v7
                        v8 = 1
                    elif v8 == 4:
                        print('Fourth Chomp Missed!')
                        v8 = random.randint(1, 5)
                        if v8 != 2:
                            P3.health -= v7
                            v8 = 1
                        elif v8 == 5:
                            print('All Chomps Missed!')
                            v8 = 1
        elif v8 == 2 or 3 or 4:
            print('Frenzy Plant Hit!')
            P3.health -= v3 + v4 + v5 + v6 +v7
        elif v8 == 5:
            print('It was Super Affective')
            v3 *= 2
            v4 *= 2
            v5 *= 2
            v6 *= 2
            v7 *= 2
            P3.health -= v3 + v4 + v5 + v6 +v7
        print('')
        print(P2.name, '         V.S.        ', P3.name)
        print(P2.health,'hp', '                 ', P3.health, 'hp')
        print('')
    elif A4 == 'leaf storm':
        v9 = random.randint(1, 50)
        v10 = random.randint(1, 10)
        if v10 == 1:
            print('Leaf Storm Missed!')
        if v10 == 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
            print('Leaf Storm Hit!')
            P3.health =- v9
        if v10 == 10:
            print('It was Super Affective')
            v9 *= 2
            P3.health =- v9
        print('')
        print(P2.name, '         V.S.        ', P3.name)
        print(P2.health,'hp', '                 ', P3.health, 'hp')
        print('')
    elif A4 == 'razor leaf':
        v11 = random.randint(10, 60)
        v12 = random.randint(1, 10)
        if v12 == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8:
            print('Razor Leaf Hit!')
            P3.health -= v11
        elif v12 == 9:
            print('Razor Leaf Missed!')
        elif v12 == 10:
            print('It was Super Affective!')
            v11 *= 2
            P3.health -= v11
        print('')
        print(P2.name, '         V.S.        ', P3.name)
        print(P2.health,'hp', '                 ', P3.health, 'hp')
        print('')
    else:
        print('Your punishment for not typing correctly. LOSE A TURN!')
        print('')
        print(P2.name, '         V.S.        ', P3.name)
        print(P2.health,'hp', '                 ', P3.health, 'hp')
        print('')
def G5():
    # Moves are Giga Drain, Frenzy Plant, Leaf Storm, and Razor Leaf
    print('Valid Moves:')
    print('Giga Drain')
    print('Frenzy Plant')
    print('Leaf Storm')
    print('Razor Leaf')
    print('(Type everything in lowercase)')
    A4 = input('What move do you want to use: ')
    if A4 == 'giga drain':
        v1 = random.randint(30, 70)
        v2 =  random.randint(1, 5)
        if v2 == 1 or 2 or 3:
            print('Giga Drain Hit!')
            P1.health -= v1
            P3.health += v1
        elif v2 == 4:
            print('It was super affective')
            v1 *= 2
            P1.health -= v1
            P3.health += v1
        elif v2 == 5:
            print('Giga Drain Missed!')
        print('')
        print(P3.name, '         V.S.        ', P1.name)
        print(P3.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A4 == 'frenzy plant':
        v3 = random.randint(1, 10)
        v4 = random.randint(1, 10)
        v5 = random.randint(1, 10)
        v6 = random.randint(1, 10)
        v7 = random.randint(1, 10)
        v8 = random.randint(1, 5)
        if v8 == 1:
            print('First Chomp Missed!')
            v8 = random.randint(1, 5)
            if v8 != 2:
                P1.health -= v4 + v5 + v6 + v7
                v8 = 1
            elif v8 == 2:
                print('Second Chomp Missed!')
                v8 = random.randint(1, 5)
                if v8 != 3:
                    P1.health -= v5 + v6 + v7
                    v8 = 1
                elif v8 == 3:
                    print('Third Chomp Missed!')
                    v8 = random.randint(1, 5)
                    if v8 != 4:
                        P1.health -= v6 + v7
                        v8 = 1
                    elif v8 == 4:
                        print('Fourth Chomp Missed!')
                        v8 = random.randint(1, 5)
                        if v8 != 2:
                            P1.health -= v7
                            v8 = 1
                        elif v8 == 5:
                            print('All Chomps Missed!')
                            v8 = 1
        elif v8 == 2 or 3 or 4:
            print('Frenzy Plant Hit!')
            P1.health -= v3 + v4 + v5 + v6 +v7
        elif v8 == 5:
            print('It was Super Affective')
            v3 *= 2
            v4 *= 2
            v5 *= 2
            v6 *= 2
            v7 *= 2
            P1.health -= v3 + v4 + v5 + v6 +v7
        print('')
        print(P3.name, '         V.S.        ', P1.name)
        print(P3.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A4 == 'leaf storm':
        v9 = random.randint(1, 50)
        v10 = random.randint(1, 10)
        if v10 == 1:
            print('Leaf Storm Missed!')
        if v10 == 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
            print('Leaf Storm Hit!')
            P1.health =- v9
        if v10 == 10:
            print('It was Super Affective')
            v9 *= 2
            P1.health =- v9
        print('')
        print(P3.name, '         V.S.        ', P1.name)
        print(P3.health,'hp', '                 ', P1.health, 'hp')
        print('')
    elif A4 == 'razor leaf':
        v11 = random.randint(10, 60)
        v12 = random.randint(1, 10)
        if v12 == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8:
            print('Razor Leaf Hit!')
            P1.health -= v11
        elif v12 == 9:
            print('Razor Leaf Missed!')
        elif v12 == 10:
            print('It was Super Affective!')
            v11 *= 2
            P1.health -= v11
        print('')
        print(P3.name, '         V.S.        ', P1.name)
        print(P3.health,'hp', '                 ', P1.health, 'hp')
        print('')
    else:
        print('Your punishment for not typing correctly. LOSE A TURN!')
        print('')
        print(P3.name, '         V.S.        ', P1.name)
        print(P3.health,'hp', '                 ', P1.health, 'hp')
        print('')
def G6():
    # Moves are Giga Drain, Frenzy Plant, Leaf Storm, and Razor Leaf
    print('Valid Moves:')
    print('Giga Drain')
    print('Frenzy Plant')
    print('Leaf Storm')
    print('Razor Leaf')
    print('(Type everything in lowercase)')
    A4 = input('What move do you want to use: ')
    if A4 == 'giga drain':
        v1 = random.randint(30, 70)
        v2 =  random.randint(1, 5)
        if v2 == 1 or 2 or 3:
            print('Giga Drain Hit!')
            P2.health -= v1
            P3.health += v1
        elif v2 == 4:
            print('It was super affective')
            v1 *= 2
            P2.health -= v1
            P3.health += v1
        elif v2 == 5:
            print('Giga Drain Missed!')
        print('')
        print(P2.name, '         V.S.        ', P3.name)
        print(P2.health,'hp', '                 ', P3.health, 'hp')
        print('')
    elif A4 == 'frenzy plant':
        v3 = random.randint(1, 10)
        v4 = random.randint(1, 10)
        v5 = random.randint(1, 10)
        v6 = random.randint(1, 10)
        v7 = random.randint(1, 10)
        v8 = random.randint(1, 5)
        if v8 == 1:
            print('First Chomp Missed!')
            v8 = random.randint(1, 5)
            if v8 != 2:
                P2.health -= v4 + v5 + v6 + v7
                v8 = 1
            elif v8 == 2:
                print('Second Chomp Missed!')
                v8 = random.randint(1, 5)
                if v8 != 3:
                    P2.health -= v5 + v6 + v7
                    v8 = 1
                elif v8 == 3:
                    print('Third Chomp Missed!')
                    v8 = random.randint(1, 5)
                    if v8 != 4:
                        P2.health -= v6 + v7
                        v8 = 1
                    if v8 == 4:
                        print('Fourth Chomp Missed!')
                        v8 = random.randint(1, 5)
                        if v8 != 2:
                            P2.health -= v7
                            v8 = 1
                        if v8 == 5:
                            print('All Chomps Missed!')
                            v8 = 1
        elif v8 == 2 or 3 or 4:
            print('Frenzy Plant Hit!')
            P2.health -= v3 + v4 + v5 + v6 +v7
        elif v8 == 5:
            print('It was Super Affective')
            v3 *= 2
            v4 *= 2
            v5 *= 2
            v6 *= 2
            v7 *= 2
            P2.health -= v3 + v4 + v5 + v6 +v7
        print('')
        print(P2.name, '         V.S.        ', P3.name)
        print(P2.health,'hp', '                 ', P3.health, 'hp')
        print('')
    elif A4 == 'leaf storm':
        v9 = random.randint(1, 50)
        v10 = random.randint(1, 10)
        if v10 == 1:
            print('Leaf Storm Missed!')
        if v10 == 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
            print('Leaf Storm Hit!')
            P2.health =- v9
        if v10 == 10:
            print('It was Super Affective')
            v9 *= 2
            P2.health =- v9
        print('')
        print(P2.name, '         V.S.        ', P3.name)
        print(P2.health,'hp', '                 ', P3.health, 'hp')
        print('')
    elif A4 == 'razor leaf':
        v11 = random.randint(10, 60)
        v12 = random.randint(1, 10)
        if v12 == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8:
            print('Razor Leaf Hit!')
            P2.health -= v11
        elif v12 == 9:
            print('Razor Leaf Missed!')
        elif v12 == 10:
            print('It was Super Affective!')
            v11 *= 2
            P2.health -= v11
        print('')
        print(P2.name, '         V.S.        ', P3.name)
        print(P2.health,'hp', '                 ', P3.health, 'hp')
        print('')
    else:
        print('Your punishment for not typing correctly. LOSE A TURN!')
        print('')
        print(P2.name, '         V.S.        ', P3.name)
        print(P2.health,'hp', '                 ', P3.health, 'hp')
        print('')
#////////////////////////////////////////////////////////////////////////////
def C1():
    #Moves is Shadowball, Drain, Triple Night Slash, and Dark Void
    A3 = random.randint(1, 4)
    if A3 == 1:
        C.health -=100
        P1.health -=100
        print('Dark Void Hit!')
        print('')
        print(C.name, '         V.S.        ', P1.name)
        print(C.health,'hp', '                 ', P1.health, 'hp')
        print('')
    if A3 == 2:
        V1 = random.randint(10, 30)
        V8 = random.randint(1, 5)
        if V8 == 3 or 4 or 5:
            print('Shadow Ball Hit!')
            P1.health -= V1
        elif V8 == 1:
            print('It was Super Affective')
            V1 *= 2
            P1.health -= V1
        elif V8 == 2:
            print('Shadow Ball Missed')
        print('')
        print(C.name, '         V.S.        ', P1.name)
        print(C.health,'hp', '                 ', P1.health, 'hp')
        print('')
    if A3 == 3:
        V2 = random.randint(10, 30)
        V7 = random.randint(1, 8)
        P1.health -= V2
        V2 *= 2
        C.health += V2
        print('Drain Hit!')
        print('')
        print(C.name, '         V.S.        ', P1.name)
        print(C.health,'hp', '                 ', P1.health, 'hp')
        print('')
    if A3 == 4:
        V3 = random.randint(1 ,20)
        V4 = random.randint(1, 20)
        V5 = random.randint(1, 20)
        V6 = random.randint(1, 5)
        if V6 == 1:
            print('First Slash Missed!')
            V6 = random.randint(1, 5)
            if V6 != 2:
                P1.health -= V3 + V4 + V5
                V6 = 1
            elif V6 == 2:
                print('Second Slash also Missed')
                V6 = random.randint(1, 5)
                if V6 != 3:
                    P1.health -= V3 + V4 + V5
                    V6 = 1
                elif V6 == 3:
                    print('Third Slash Also Missed')
                    V6 = 1
        if V6 == 4:
            print('It was Super Affective')
            V3 *= 2
            V4 *= 2
            V5 *= 2
            P1.health -= V3 + V4 + V5
        elif V6 ==5:
            print('Triple Slash Hit!')
            P1.health -= V3 + V4 +V5
        print('')
        print(C.name, '         V.S.        ', P1.name)
        print(C.health,'hp', '                 ', P1.health, 'hp')
        print('')
#//////////////////////////////////////////////////////////////////////////
print('1 - 1 V.S. Computer           2 - 1 V.S. 1')
print('3 - 1 V.S. 1 V.S. 1           4 - 1 V.S. Computer - Hard')
print('5 - 1 V.S. 1 - Hard           6 - Story Mode')
Mode = int(input('What mode do you want to play: '))
if Mode == 1:
    P1_name = input('Player1, Type your name: ')
    Type = input('Do you want to be Fire, Electric, Grass (Make sure to type in all lowercase): ')
    P1 = Characters(150, Type, P1_name)
    C = Characters(150, 'Dark', 'Computer')
    print('')
    print('It seems you are lonely :(')
    print("But don't fear there is a computer! :) ")
    print("Without further ado, Let's begin!")
    print('')
    if Type == 'fire':
        while P1.health > 0 and C.health > 0:
            H1()
            C1()
        while P1.health < 0 or P1.health == 0:
            print(P1.name, 'You Lost!')
            exit()
        while C.health < 0 or C.health == 0:
            print('You Won!')
            exit()
        while C.health < 0 or C.health == 0 and P1.health < 0 or P1.health == 0:
            print('You Tied!')
            exit()
    if Type == 'electric':
        while P1.health > 0 and C.health > 0:
            T1()
            C1()
        while P1.health < 0 or P1.health == 0:
            print(P1.name, 'You Lost!')
            exit()
        while C.health < 0 or C.health == 0:
            print('You Won!')
            exit()
        while C.health < 0 or C.health == 0 and P1.health < 0 or P1.health == 0:
            print('You Tied!')
            exit()
    elif Type == 'grass':
        while P1.health > 0 and C.health > 0:
            G1()
            C1()
        while P1.health < 0 or P1.health == 0:
            print(P1.name, 'You Lost!')
            exit()
        while C.health < 0 or C.health == 0:
            print('You Won!')
            exit()
        while C.health < 0 or C.health == 0 and P1.health < 0 or P1.health == 0:
            print('You Tied!')
            exit()
elif Mode == 2:d
    P1_name = input('Player 1, Type your name: ')
    P1_type = input('Player 1, Pick a type (Fire, Electric, or Grass): ')
    P2_name = input('Player 2, Type your name: ')
    P2_type = input('Player 2, Pick a type (Fire, Electric, or Grass): ') 
    P1 = Characters(150, P1_type, P1_name)
    P2 = Characters(150, P2_type, P2_name)
    value = random.randint(0, 1)
    if value == 0:
        value = 'heads'
    if value == 1:
        value = 'tails'
    print(P2.name,'         V.S.      ', P1.name)
    print(P2.health,'hp', '                 ', P1.health, 'hp')
    print(P2.type, '               ',  P1.type)
    print('')
    print(P2.name,', do you want to choose Heads or Tails?')
    Coin = input("Type the side the side you want (Make sure to type all lowercase): ")
    if Coin == 'heads':
        print('Good Choice!')
    elif Coin == 'tails':
        print('Good Choice')
    print(P2.name, ' flips coin')
    print('The Coin lands', value, '!')
    if value == Coin:
        print(P2.name, ' Goes First!')
    elif value != Coin:
        print(P1.name, ' Goes First!')
    print("Let's start the battle")
    print('')
    if value == Coin:
        while P2.health > 0 and P1.health > 0:
            if P1.type == 'fire' and P2.type == 'electric':                                 
                T()
                H()
            elif P1.type == 'fire' and P2.type == 'grass':
                G2()
                H()
            elif P1.type == 'fire' and P2.type == 'fire':
                H()
                H2()
            elif P1.type == 'electric' and P2.type == 'fire':
                H2()
                T2()
            elif P1.type == 'electric' and P2.type == 'electric':
                T()
                T2()
            elif P1.type == 'electric' and P2.type == 'grass':
                T2()
                G2()
            elif P1.type == 'grass' and P2.type == 'fire':
                H2()
                G()
            elif P1.type == 'grass' and P2.type == 'electric':
                T()
                G()
            elif P1.type == 'grass' and P2.type == 'grass':
                G2()
                G()
        while P1.health == 0 or P1.health < 0:
            print(P2.name, ' Wins!')
            exit()
        while P2.health == 0 or P2.health < 0:
            print(P1.name, ' Wins!')
            exit()
        while P2.health < 0 or P2.health == 0 and P1.health < 0 or P1.health == 0:
            print('You tied!')
            exit()
    elif value != Coin:
        while P1.health > 0 and P2.health > 0:
            if P1.type == 'fire' and P2.type == 'electric':                                 
                H()
                T()
            elif P1.type == 'fire' and P2.type == 'grass':
                H()
                G2()
            elif P1.type == 'fire' and P2.type == 'fire':
                H2()
                H()
            elif P1.type == 'electric' and P2.type == 'fire':
                T2()
                H2()
            elif P1.type == 'electric' and P2.type == 'electric':
                T2()
                T()
            elif P1.type == 'electric' and P2.type == 'grass':
                G2()
                T2()
            elif P1.type == 'grass' and P2.type == 'fire':
                G()
                H2()
            elif P1.type == 'grass' and P2.type == 'electric':
                G()
                T()
            elif P1.type == 'grass' and P2.type == 'grass':
                G()
                G2()
        while P1.health == 0 or P1.health < 0:
            print(P2.name, ' Wins!')
            exit()
        while P2.health == 0 or P2.health < 0:
            print(P1.name,'Wins!')
            exit()
        while P2.health < 0 or P2.health == 0 and P1.health < 0 or P1.health == 0:
            print('You tied!')
            exit()
elif Mode == 3:
    print('You have lots of friends I see')
    print('May I know all of your names?')
    print('')
    P1_name = input('Player 1, Type your name: ')
    P1_type = input('Player 1, Type the type you want (fire, electric, or grass): ')
    print('')
    P2_name = input('Player 2, Type your name: ')
    P2_type = input('Player 2, Type the type you want (fire, electric, or grass): ')
    print('')
    P3_name = input('Player 3, Type your name: ')
    P3_type = input('Player 3, Type the type you want (fire, electric, or grass): ')
    P1 = Characters(150, P1_type, P1_name)
    P2 = Characters(150, P2_type, P2_name)
    P3 = Characters(150, P3_type, P3_name)
    trando = random.randint(1, 3)
    if trando == 1:
        print('')
        print('Player 1 goes first, Player 2 is second, and Player 3 is last!')
        if P1_type == 'fire' and P2_type == 'fire' and P3_type == 'fire':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    H()
                elif Attack == 3:
                    H3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    H2()
                elif Attack2 == 3:
                    H4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    H5()
                elif Attack3 == 2:
                    H6()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                H()
                H2()
            while P1.health > 0 and P3.health > 0:
                H3()
                H5()
            while P2.health > 0 and P3.health > 0:
                H4()
                H6()
        elif P1_type == 'fire' and P2_type == 'fire' and P3_type == 'electric':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    H()
                elif Attack == 3:
                    H3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    H2()
                elif Attack2 == 3:
                    H4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    T5()
                elif Attack3 == 2:
                    T6()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                H()
                H2()
            while P1.health > 0 and P3.health > 0:
                H3()
                T5()
            while P2.health > 0 and P3.health > 0:
                H4()
                T6()
        elif P1_type == 'fire' and P2_type == 'fire' and P3_type == 'grass':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    H()
                elif Attack == 3:
                    H3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    H2()
                elif Attack2 == 3:
                    H4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    G5()
                elif Attack3 == 2:
                    G6()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                H()
                H2()
            while P1.health > 0 and P3.health > 0:
                H3()
                G5()
            while P2.health > 0 and P3.health > 0:
                H4()
                G6()
        elif P1_type == 'fire' and P2_type == 'electric' and P3_type == 'fire':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    H()
                elif Attack == 3:
                    H3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    T()
                elif Attack2 == 3:
                    T4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    H5()
                elif Attack3 == 2:
                    H6()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                H()
                T()
            while P1.health > 0 and P3.health > 0:
                H3()
                H5()
            while P2.health > 0 and P3.health > 0:
                T4()
                H6()
        elif P1_type == 'fire' and P2_type == 'electric' and P3_type == 'electric':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    H()
                elif Attack == 3:
                    H3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    T()
                elif Attack2 == 3:
                    T4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    T5()
                elif Attack3 == 2:
                    T6()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                H()
                T()
            while P1.health > 0 and P3.health > 0:
                H3()
                T5()
            while P2.health > 0 and P3.health > 0:
                T4()
                T6() 
        elif P1_type == 'fire' and P2_type == 'electric' and P3_type == 'grass':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    H()
                elif Attack == 3:
                    H3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    T()
                elif Attack2 == 3:
                    T4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    G5()
                elif Attack3 == 2:
                    G6()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
            while P1.health > 0 and P2.health > 0:
                H()
                T()
            while P1.health > 0 and P3.health > 0:
                H3()
                G5()
            while P2.health > 0 and P3.health > 0:
                T4()
                G6()
        elif P1_type == 'fire' and P2_type == 'grass' and P3_type == 'fire':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    H()
                elif Attack == 3:
                    H3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    G2()
                elif Attack2 == 3:
                    G4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    H5()
                elif Attack3 == 2:
                    H6()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                H()
                G2()
            while P1.health > 0 and P3.health > 0:
                H3()
                H5()
            while P2.health > 0 and P3.health > 0:
                G4()
                H6()
        elif P1_type == 'fire' and P2_type == 'grass' and P3_type == 'electric':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    H()
                elif Attack == 3:
                    H3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    G2()
                elif Attack2 == 3:
                    G4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    T5()
                elif Attack3 == 2:
                    T6()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                H()
                G2()
            while P1.health > 0 and P3.health > 0:
                H3()
                T5()
            while P2.health > 0 and P3.health > 0:
                G4()
                T6() 
        elif P1_type == 'fire' and P2_type == 'grass' and P3_type == 'grass':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    H()
                elif Attack == 3:
                    H3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    G2()
                elif Attack2 == 3:
                    G4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    G5()
                elif Attack3 == 2:
                    G6()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                H()
                G2()
            while P1.health > 0 and P3.health > 0:
                H3()
                G5()
            while P2.health > 0 and P3.health > 0:
                G4()
                G6() 
        elif P1_type == 'electric' and P2_type == 'fire' and P3_type == 'fire':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    T()
                elif Attack == 3:
                    T3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    H2()
                elif Attack2 == 3:
                    H4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    H5()
                elif Attack3 == 2:
                    H6()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                T2()
                H2()
            while P1.health > 0 and P3.health > 0:
                T3()
                H5()
            while P2.health > 0 and P3.health > 0:
                H4()
                H6()
        elif P1_type == 'electric' and P2_type == 'fire' and P3_type == 'electric':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    T()
                elif Attack == 3:
                    T3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    H2()
                elif Attack2 == 3:
                    H4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    T5()
                elif Attack3 == 2:
                    T6()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                T2()
                H2()
            while P1.health > 0 and P3.health > 0:
                T3()
                T5()
            while P2.health > 0 and P3.health > 0:
                H4()
                T6()
        elif P1_type == 'electric' and P2_type == 'fire' and P3_type == 'grass':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    T()
                elif Attack == 3:
                    T3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    H2()
                elif Attack2 == 3:
                    H4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    G5()
                elif Attack3 == 2:
                    G6()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                T2()
                H2()
            while P1.health > 0 and P3.health > 0:
                T3()
                G5()
            while P2.health > 0 and P3.health > 0:
                H4()
                G6()
        elif P1_type == 'electric' and P2_type == 'electric' and P3_type == 'fire':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    T()
                elif Attack == 3:
                    T3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    T()
                elif Attack2 == 3:
                    T4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    H5()
                elif Attack3 == 2:
                    H6()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                T2()
                T()
            while P1.health > 0 and P3.health > 0:
                T3()
                H5()
            while P2.health > 0 and P3.health > 0:
                T4()
                H6()
        elif P1_type == 'electric' and P2_type == 'electric' and P3_type == 'electric':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    T()
                elif Attack == 3:
                    T3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    T()
                elif Attack2 == 3:
                    T4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    T5()
                elif Attack3 == 2:
                    T6()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                T2()
                T()
            while P1.health > 0 and P3.health > 0:
                T3()
                T5()
            while P2.health > 0 and P3.health > 0:
                T4()
                T6()
        elif P1_type == 'electric' and P2_type == 'electric' and P3_type == 'grass':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    T()
                elif Attack == 3:
                    T3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    T()
                elif Attack2 == 3:
                    T4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    G5()
                elif Attack3 == 2:
                    G6()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                T2()
                T()
            while P1.health > 0 and P3.health > 0:
                T3()
                G5()
            while P2.health > 0 and P3.health > 0:
                T4()
                G6() 
        elif P1_type == 'electric' and P2_type == 'grass' and P3_type == 'fire':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    T()
                elif Attack == 3:
                    T3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    G2()
                elif Attack2 == 3:
                    G4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    H5()
                elif Attack3 == 2:
                    H6()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                T2()
                G2()
            while P1.health > 0 and P3.health > 0:
                T3()
                H5()
            while P2.health > 0 and P3.health > 0:
                G4()
                H6() 
        elif P1_type == 'electric' and P2_type == 'grass' and P3_type == 'electric':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    T()
                elif Attack == 3:
                    T3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    G2()
                elif Attack2 == 3:
                    G4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    T5()
                elif Attack3 == 2:
                    T6()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                G2()
                H2()
            while P1.health > 0 and P3.health > 0:
                T3()
                T5()
            while P2.health > 0 and P3.health > 0:
                G4()
                T6() 
        elif P1_type == 'electric' and P2_type == 'grass' and P3_type == 'grass':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    T()
                elif Attack == 3:
                    T3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    G2()
                elif Attack2 == 3:
                    G4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    G5()
                elif Attack3 == 2:
                    G6()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                G2()
                H2()
            while P1.health > 0 and P3.health > 0:
                T3()
                G5()
            while P2.health > 0 and P3.health > 0:
                G4()
                G6()
        elif P1_type == 'grass' and P2_type == 'fire' and P3_type == 'fire':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    G()
                elif Attack == 3:
                    G3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    H2()
                elif Attack2 == 3:
                    H4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    H5()
                elif Attack3 == 2:
                    H6()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                G()
                H2()
            while P1.health > 0 and P3.health > 0:
                G3()
                H5()
            while P2.health > 0 and P3.health > 0:
                H4()
                H6()
        elif P1_type == 'grass' and P2_type == 'fire' and P3_type == 'electric':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    G()
                elif Attack == 3:
                    G3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    H2()
                elif Attack2 == 3:
                    H4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    T5()
                elif Attack3 == 2:
                    T6()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                G()
                H2()
            while P1.health > 0 and P3.health > 0:
                G3()
                T5()
            while P2.health > 0 and P3.health > 0:
                H4()
                T6()
        elif P1_type == 'grass' and P2_type == 'fire' and P3_type == 'grass':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    G()
                elif Attack == 3:
                    G3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    H2()
                elif Attack2 == 3:
                    H4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    G5()
                elif Attack3 == 2:
                    G6()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                G()
                H2()
            while P1.health > 0 and P3.health > 0:
                G3()
                G5()
            while P2.health > 0 and P3.health > 0:
                H4()
                G6()
        elif P1_type == 'grass' and P2_type == 'electric' and P3_type == 'fire':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    G()
                elif Attack == 3:
                    G3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    T()
                elif Attack2 == 3:
                    T4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    H5()
                elif Attack3 == 2:
                    H6()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                G()
                T()
            while P1.health > 0 and P3.health > 0:
                G3()
                H5()
            while P2.health > 0 and P3.health > 0:
                T4()
                H6()
        elif P1_type == 'grass' and P2_type == 'electric' and P3_type == 'electric':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    G()
                elif Attack == 3:
                    G3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    T()
                elif Attack2 == 3:
                    T4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    T5()
                elif Attack3 == 2:
                    T6()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                G()
                T()
            while P1.health > 0 and P3.health > 0:
                G3()
                T5()
            while P2.health > 0 and P3.health > 0:
                T4()
                T6()
        elif P1_type == 'grass' and P2_type == 'electric' and P3_type == 'grass':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    G()
                elif Attack == 3:
                    G3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    T()
                elif Attack2 == 3:
                    T4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    G5()
                elif Attack3 == 2:
                    G6()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                G()
                T()
            while P1.health > 0 and P3.health > 0:
                G3()
                G5()
            while P2.health > 0 and P3.health > 0:
                T4()
                G6()
        elif P1_type == 'grass' and P2_type == 'grass' and P3_type == 'fire':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    G()
                elif Attack == 3:
                    G3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    G2()
                elif Attack2 == 3:
                    G4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    H5()
                elif Attack3 == 2:
                    H6()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                G()
                G2()
            while P1.health > 0 and P3.health > 0:
                G3()
                G5()
            while P2.health > 0 and P3.health > 0:
                G4()
                G6()
        elif P1_type == 'grass' and P2_type == 'grass' and P3_type == 'electric':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    G()
                elif Attack == 3:
                    G3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    G2()
                elif Attack2 == 3:
                    G4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    T5()
                elif Attack3 == 2:
                    T6()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                G()
                G2()
            while P1.health > 0 and P3.health > 0:
                G3()
                T5()
            while P2.health > 0 and P3.health > 0:
                G4()
                T6()
        elif P1_type == 'grass' and P2_type == 'grass' and P3_type == 'grass':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    G()
                elif Attack == 3:
                    G3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    G2()
                elif Attack2 == 3:
                    G4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    G5()
                elif Attack3 == 2:
                    G6()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                G()
                G2()
            while P1.health > 0 and P3.health > 0:
                G3()
                G5()
            while P2.health > 0 and P3.health > 0:
                G4()
                G6()
    elif trando == 2:
        print('')
        print('Player 2 goes first, Player 3 is second, and Player 1 is last!')
        if P1_type == 'fire' and P2_type == 'fire' and P3_type == 'fire':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    H()
                elif Attack == 3:
                    H3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    H2()
                elif Attack2 == 3:
                    H4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    H5()
                elif Attack3 == 2:
                    H6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    H()
                elif Attack == 3:
                    H3()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                H2()
                H()
            while P1.health > 0 and P3.health > 0:
                H5()
                H3()
            while P2.health > 0 and P3.health > 0:
                H4()
                H6()
        elif P1_type == 'fire' and P2_type == 'fire' and P3_type == 'electric':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    H()
                elif Attack == 3:
                    H3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    H2()
                elif Attack2 == 3:
                    H4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    T5()
                elif Attack3 == 2:
                    T6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    H()
                elif Attack == 3:
                    H3()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                H2()
                H()
            while P1.health > 0 and P3.health > 0:
                T5()
                H3()
            while P2.health > 0 and P3.health > 0:
                H4()
                T6()
        elif P1_type == 'fire' and P2_type == 'fire' and P3_type == 'grass':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    H2()
                elif Attack2 == 3:
                    H4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    G5()
                elif Attack3 == 2:
                    G6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    H()
                elif Attack == 3:
                    H3()
                else:
                    print('Lose a Turn!')    
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                H2()
                H()
            while P1.health > 0 and P3.health > 0:
                G5()
                H3()
            while P2.health > 0 and P3.health > 0:
                H4()
                G6()
        elif P1_type == 'fire' and P2_type == 'electric' and P3_type == 'fire':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    T()
                elif Attack2 == 3:
                    T4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    H5()
                elif Attack3 == 2:
                    H6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    H()
                elif Attack == 3:
                    H3()
                else:
                    print('Lose a Turn!')    
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                T()
                H()
            while P1.health > 0 and P3.health > 0:
                H5()
                H3()
            while P2.health > 0 and P3.health > 0:
                T4()
                H6()
        elif P1_type == 'fire' and P2_type == 'electric' and P3_type == 'electric':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    T()
                elif Attack2 == 3:
                    T4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    T5()
                elif Attack3 == 2:
                    T6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    H()
                elif Attack == 3:
                    H3()
                else:
                    print('Lose a Turn!')    
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                T()
                H()
            while P1.health > 0 and P3.health > 0:
                T5()
                H3()
            while P2.health > 0 and P3.health > 0:
                T4()
                T6() 
        elif P1_type == 'fire' and P2_type == 'electric' and P3_type == 'grass':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    T()
                elif Attack2 == 3:
                    T4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    G5()
                elif Attack3 == 2:
                    G6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    H()
                elif Attack == 3:
                    H3()
                else:
                    print('Lose a Turn!')    
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                T()
                H()
            while P1.health > 0 and P3.health > 0:
                G5()
                H3()
            while P2.health > 0 and P3.health > 0:
                T4()
                G6()
        elif P1_type == 'fire' and P2_type == 'grass' and P3_type == 'fire':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    G2()
                elif Attack2 == 3:
                    G4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    H5()
                elif Attack3 == 2:
                    H6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    H()
                elif Attack == 3:
                    H3()
                else:
                    print('Lose a Turn!')    
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                G2()
                H()
            while P1.health > 0 and P3.health > 0:
                H5()
                H3()
            while P2.health > 0 and P3.health > 0:
                G4()
                H6()
        elif P1_type == 'fire' and P2_type == 'grass' and P3_type == 'electric':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    G2()
                elif Attack2 == 3:
                    G4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    T5()
                elif Attack3 == 2:
                    T6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    H()
                elif Attack == 3:
                    H3()
                else:
                    print('Lose a Turn!')    
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                G2()
                H()
            while P1.health > 0 and P3.health > 0:
                T5()
                H3()
            while P2.health > 0 and P3.health > 0:
                G4()
                T6() 
        elif P1_type == 'fire' and P2_type == 'grass' and P3_type == 'grass':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    G2()
                elif Attack2 == 3:
                    G4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    G5()
                elif Attack3 == 2:
                    G6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    H()
                elif Attack == 3:
                    H3()
                else:
                    print('Lose a Turn!')    
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                G2()
                H()
            while P1.health > 0 and P3.health > 0:
                G5()
                H3()
            while P2.health > 0 and P3.health > 0:
                G4()
                G6() 
        elif P1_type == 'electric' and P2_type == 'fire' and P3_type == 'fire':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    H2()
                elif Attack2 == 3:
                    H4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    H5()
                elif Attack3 == 2:
                    H6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    T()
                elif Attack == 3:
                    T3()
                else:
                    print('Lose a Turn!')    
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                H2()
                T2()
            while P1.health > 0 and P3.health > 0:
                H5()
                T3()
            while P2.health > 0 and P3.health > 0:
                H4()
                H6()
        elif P1_type == 'electric' and P2_type == 'fire' and P3_type == 'electric':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    H2()
                elif Attack2 == 3:
                    H4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    T5()
                elif Attack3 == 2:
                    T6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    T()
                elif Attack == 3:
                    T3()
                else:
                    print('Lose a Turn!')    
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                H2()
                T2()
            while P1.health > 0 and P3.health > 0:
                T5()
                T3()
            while P2.health > 0 and P3.health > 0:
                H4()
                T6()
        elif P1_type == 'electric' and P2_type == 'fire' and P3_type == 'grass':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    H2()
                elif Attack2 == 3:
                    H4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    G5()
                elif Attack3 == 2:
                    G6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    T()
                elif Attack == 3:
                    T3()
                else:
                    print('Lose a Turn!')    
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                H2()
                T2()
            while P1.health > 0 and P3.health > 0:
                G5()
                T3()
            while P2.health > 0 and P3.health > 0:
                H4()
                G6()
        elif P1_type == 'electric' and P2_type == 'electric' and P3_type == 'fire':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    T()
                elif Attack2 == 3:
                    T4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    H5()
                elif Attack3 == 2:
                    H6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    T()
                elif Attack == 3:
                    T3()
                else:
                    print('Lose a Turn!')    
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                T()
                T2()
            while P1.health > 0 and P3.health > 0:
                H5()
                T3()
            while P2.health > 0 and P3.health > 0:
                T4()
                H6()
        elif P1_type == 'electric' and P2_type == 'electric' and P3_type == 'electric':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    T()
                elif Attack2 == 3:
                    T4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    T5()
                elif Attack3 == 2:
                    T6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    T()
                elif Attack == 3:
                    T3()
                else:
                    print('Lose a Turn!')    
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                T()
                T2()
            while P1.health > 0 and P3.health > 0:
                T5()
                T3()
            while P2.health > 0 and P3.health > 0:
                T4()
                T6()
        elif P1_type == 'electric' and P2_type == 'electric' and P3_type == 'grass':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    T()
                elif Attack2 == 3:
                    T4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    G5()
                elif Attack3 == 2:
                    G6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    T()
                elif Attack == 3:
                    T3()
                else:
                    print('Lose a Turn!')    
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                T()
                T2()
            while P1.health > 0 and P3.health > 0:
                G5()
                T3()
            while P2.health > 0 and P3.health > 0:
                T4()
                G6()
        elif P1_type == 'electric' and P2_type == 'grass' and P3_type == 'fire':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    G2()
                elif Attack2 == 3:
                    G4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    H5()
                elif Attack3 == 2:
                    H6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    T()
                elif Attack == 3:
                    T3()
                else:
                    print('Lose a Turn!')    
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                G2()
                T2()
            while P1.health > 0 and P3.health > 0:
                H5()
                T3()
            while P2.health > 0 and P3.health > 0:
                G4()
                H6() 
        elif P1_type == 'electric' and P2_type == 'grass' and P3_type == 'electric':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    G2()
                elif Attack2 == 3:
                    G4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    T5()
                elif Attack3 == 2:
                    T6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    T()
                elif Attack == 3:
                    T3()
                else:
                    print('Lose a Turn!')    
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                H2()
                G2()
            while P1.health > 0 and P3.health > 0:
                T5()
                T3()
            while P2.health > 0 and P3.health > 0:
                G4()
                T6() 
        elif P1_type == 'electric' and P2_type == 'grass' and P3_type == 'grass':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    G2()
                elif Attack2 == 3:
                    G4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    G5()
                elif Attack3 == 2:
                    G6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    T()
                elif Attack == 3:
                    T3()
                else:
                    print('Lose a Turn!')    
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                H2()
                G2()
            while P1.health > 0 and P3.health > 0:
                G5()
                T3()
            while P2.health > 0 and P3.health > 0:
                G4()
                G6()
        elif P1_type == 'grass' and P2_type == 'fire' and P3_type == 'fire':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    H2()
                elif Attack2 == 3:
                    H4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    H5()
                elif Attack3 == 2:
                    H6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    G()
                elif Attack == 3:
                    G3()
                else:
                    print('Lose a Turn!')    
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                H2()
                G()
            while P1.health > 0 and P3.health > 0:
                H5()
                G3()
            while P2.health > 0 and P3.health > 0:
                H4()
                H6()
        elif P1_type == 'grass' and P2_type == 'fire' and P3_type == 'electric':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    H2()
                elif Attack2 == 3:
                    H4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    T5()
                elif Attack3 == 2:
                    T6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    G()
                elif Attack == 3:
                    G3()
                else:
                    print('Lose a Turn!')    
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                H2()
                G()
            while P1.health > 0 and P3.health > 0:
                T5()
                G3()
            while P2.health > 0 and P3.health > 0:
                H4()
                T6()
        elif P1_type == 'grass' and P2_type == 'fire' and P3_type == 'grass':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    H2()
                elif Attack2 == 3:
                    H4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    G5()
                elif Attack3 == 2:
                    G6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    G()
                elif Attack == 3:
                    G3()
                else:
                    print('Lose a Turn!')    
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                H2()
                G()
            while P1.health > 0 and P3.health > 0:
                G5()
                G3()
            while P2.health > 0 and P3.health > 0:
                H4()
                G6()
        elif P1_type == 'grass' and P2_type == 'electric' and P3_type == 'fire':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    T()
                elif Attack2 == 3:
                    T4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    H5()
                elif Attack3 == 2:
                    H6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    G()
                elif Attack == 3:
                    G3()
                else:
                    print('Lose a Turn!')    
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                T()
                G()
            while P1.health > 0 and P3.health > 0:
                H5()
                G3()
            while P2.health > 0 and P3.health > 0:
                T4()
                H6()
        elif P1_type == 'grass' and P2_type == 'electric' and P3_type == 'electric':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    T()
                elif Attack2 == 3:
                    T4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    T5()
                elif Attack3 == 2:
                    T6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    G()
                elif Attack == 3:
                    G3()
                else:
                    print('Lose a Turn!')    
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                T()
                G()
            while P1.health > 0 and P3.health > 0:
                T5()
                G3()
            while P2.health > 0 and P3.health > 0:
                T4()
                T6()
        elif P1_type == 'grass' and P2_type == 'electric' and P3_type == 'grass':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    T()
                elif Attack2 == 3:
                    T4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    G5()
                elif Attack3 == 2:
                    G6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    G()
                elif Attack == 3:
                    G3()
                else:
                    print('Lose a Turn!')    
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                T()
                G()
            while P1.health > 0 and P3.health > 0:
                G5()
                G3()
            while P2.health > 0 and P3.health > 0:
                T4()
                G6()
        elif P1_type == 'grass' and P2_type == 'grass' and P3_type == 'fire':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    G2()
                elif Attack2 == 3:
                    G4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    H5()
                elif Attack3 == 2:
                    H6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    G()
                elif Attack == 3:
                    G3()
                else:
                    print('Lose a Turn!')    
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                G2()
                G()
            while P1.health > 0 and P3.health > 0:
                G5()
                G3()
            while P2.health > 0 and P3.health > 0:
                G4()
                G6()
        elif P1_type == 'grass' and P2_type == 'grass' and P3_type == 'electric':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    G2()
                elif Attack2 == 3:
                    G4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    T5()
                elif Attack3 == 2:
                    T6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    G()
                elif Attack == 3:
                    G3()
                else:
                    print('Lose a Turn!')    
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                G2()
                G()
            while P1.health > 0 and P3.health > 0:
                T5()
                G3()
            while P2.health > 0 and P3.health > 0:
                G4()
                T6()
        elif P1_type == 'grass' and P2_type == 'grass' and P3_type == 'grass':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    G2()
                elif Attack2 == 3:
                    G4()
                else:
                    print('Lose a Turn!')
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    G5()
                elif Attack3 == 2:
                    G6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    G()
                elif Attack == 3:
                    G3()
                else:
                    print('Lose a Turn!')    
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                G2()
                G()
            while P1.health > 0 and P3.health > 0:
                G5()
                G3()
            while P2.health > 0 and P3.health > 0:
                G4()
                G6()
    elif trando == 3:
        print('')
        print('Player 3 goes first, Player 1 is second, and Player 2 is last!')
        if P1_type == 'fire' and P2_type == 'fire' and P3_type == 'fire':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    H5()
                elif Attack3 == 2:
                    H6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    H()
                elif Attack == 3:
                    H3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    H2()
                elif Attack2 == 3:
                    H4()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                H()
                H2()
            while P1.health > 0 and P3.health > 0:
                H3()
                H5()
            while P2.health > 0 and P3.health > 0:
                H6()
                H4()
        elif P1_type == 'fire' and P2_type == 'fire' and P3_type == 'electric':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    T5()
                elif Attack3 == 2:
                    T6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    H()
                elif Attack == 3:
                    H3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    H2()
                elif Attack2 == 3:
                    H4()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                H()
                H2()
            while P1.health > 0 and P3.health > 0:
                T5()
                H3()
            while P2.health > 0 and P3.health > 0:
                T6()
                H4()
        elif P1_type == 'fire' and P2_type == 'fire' and P3_type == 'grass':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    G5()
                elif Attack3 == 2:
                    G6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    H()
                elif Attack == 3:
                    H3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    H2()
                elif Attack2 == 3:
                    H4()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                H()
                H2()
            while P1.health > 0 and P3.health > 0:
                H5()
                H3()
            while P2.health > 0 and P3.health > 0:
                G6()
                H4()
        elif P1_type == 'fire' and P2_type == 'electric' and P3_type == 'fire':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    H5()
                elif Attack3 == 2:
                    H6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    H()
                elif Attack == 3:
                    H3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    T()
                elif Attack2 == 3:
                    T4()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                H()
                T()
            while P1.health > 0 and P3.health > 0:
                H5()
                H3()
            while P2.health > 0 and P3.health > 0:
                H6()
                T4()
        elif P1_type == 'fire' and P2_type == 'electric' and P3_type == 'electric':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    T5()
                elif Attack3 == 2:
                    T6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    H()
                elif Attack == 3:
                    H3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    T()
                elif Attack2 == 3:
                    T4()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                H()
                T()
            while P1.health > 0 and P3.health > 0:
                T5()
                H3()
            while P2.health > 0 and P3.health > 0:
                T6()
                T4() 
        elif P1_type == 'fire' and P2_type == 'electric' and P3_type == 'grass':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    G5()
                elif Attack3 == 2:
                    G6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    H()
                elif Attack == 3:
                    H3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    T()
                elif Attack2 == 3:
                    T4()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                H()
                T()
            while P1.health > 0 and P3.health > 0:
                G5()
                H3()
            while P2.health > 0 and P3.health > 0:
                G6()
                T4()
        elif P1_type == 'fire' and P2_type == 'grass' and P3_type == 'fire':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    H5()
                elif Attack3 == 2:
                    H6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    H()
                elif Attack == 3:
                    H3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    G2()
                elif Attack2 == 3:
                    G4()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                H()
                G2()
            while P1.health > 0 and P3.health > 0:
                H5()
                H3()
            while P2.health > 0 and P3.health > 0:
                H6()
                G4()
        elif P1_type == 'fire' and P2_type == 'grass' and P3_type == 'electric':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    T5()
                elif Attack3 == 2:
                    T6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    H()
                elif Attack == 3:
                    H3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    G2()
                elif Attack2 == 3:
                    G4()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                H()
                G2()
            while P1.health > 0 and P3.health > 0:
                T5()
                H3()
            while P2.health > 0 and P3.health > 0:
                T6()
                G4() 
        elif P1_type == 'fire' and P2_type == 'grass' and P3_type == 'grass':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    G5()
                elif Attack3 == 2:
                    G6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    H()
                elif Attack == 3:
                    H3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    G2()
                elif Attack2 == 3:
                    G4()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                H()
                G2()
            while P1.health > 0 and P3.health > 0:
                G5()
                H3()
            while P2.health > 0 and P3.health > 0:
                G6()
                G4() 
        elif P1_type == 'electric' and P2_type == 'fire' and P3_type == 'fire':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    H5()
                elif Attack3 == 2:
                    H6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    T()
                elif Attack == 3:
                    T3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    H2()
                elif Attack2 == 3:
                    H4()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                T2()
                H2()
            while P1.health > 0 and P3.health > 0:
                H5()
                T3()
            while P2.health > 0 and P3.health > 0:
                H6()
                H4()
        elif P1_type == 'electric' and P2_type == 'fire' and P3_type == 'electric':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    T5()
                elif Attack3 == 2:
                    T6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    T()
                elif Attack == 3:
                    T3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    H2()
                elif Attack2 == 3:
                    H4()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                T2()
                H2()
            while P1.health > 0 and P3.health > 0:
                T5()
                T3()
            while P2.health > 0 and P3.health > 0:
                T6()
                H4()
        elif P1_type == 'electric' and P2_type == 'fire' and P3_type == 'grass':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    G5()
                elif Attack3 == 2:
                    G6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    T()
                elif Attack == 3:
                    T3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    H2()
                elif Attack2 == 3:
                    H4()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                T2()
                H2()
            while P1.health > 0 and P3.health > 0:
                G5()
                T3()
            while P2.health > 0 and P3.health > 0:
                G6()
                H4()
        elif P1_type == 'electric' and P2_type == 'electric' and P3_type == 'fire':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    H5()
                elif Attack3 == 2:
                    H6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    T()
                elif Attack == 3:
                    T3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    T()
                elif Attack2 == 3:
                    T4()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                T2()
                T()
            while P1.health > 0 and P3.health > 0:
                T3()
                H5()
            while P2.health > 0 and P3.health > 0:
                T4()
                H6()
        elif P1_type == 'electric' and P2_type == 'electric' and P3_type == 'electric':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    T5()
                elif Attack3 == 2:
                    T6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    T()
                elif Attack == 3:
                    T3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    T()
                elif Attack2 == 3:
                    T4()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                T2()
                T()
            while P1.health > 0 and P3.health > 0:
                T5()
                T3()
            while P2.health > 0 and P3.health > 0:
                T6()
                T4()
        elif P1_type == 'electric' and P2_type == 'electric' and P3_type == 'grass':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    G5()
                elif Attack3 == 2:
                    G6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    T()
                elif Attack == 3:
                    T3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    T()
                elif Attack2 == 3:
                    T4()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                T2()
                T()
            while P1.health > 0 and P3.health > 0:
                G5()
                T3()
            while P2.health > 0 and P3.health > 0:
                G6()
                T4()
        elif P1_type == 'electric' and P2_type == 'grass' and P3_type == 'fire':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    H5()
                elif Attack3 == 2:
                    H6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    T()
                elif Attack == 3:
                    T3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    G2()
                elif Attack2 == 3:
                    G4()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                T2()
                G2()
            while P1.health > 0 and P3.health > 0:
                T3()
                H5()
            while P2.health > 0 and P3.health > 0:
                G4()
                H6() 
        elif P1_type == 'electric' and P2_type == 'grass' and P3_type == 'electric':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    T5()
                elif Attack3 == 2:
                    T6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    T()
                elif Attack == 3:
                    T3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    G2()
                elif Attack2 == 3:
                    G4()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                G2()
                H2()
            while P1.health > 0 and P3.health > 0:
                T5()
                T3()
            while P2.health > 0 and P3.health > 0:
                T6()
                G4() 
        elif P1_type == 'electric' and P2_type == 'grass' and P3_type == 'grass':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    G5()
                elif Attack3 == 2:
                    G6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    T()
                elif Attack == 3:
                    T3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    G2()
                elif Attack2 == 3:
                    G4()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                G2()
                H2()
            while P1.health > 0 and P3.health > 0:
                G5()
                T3()
            while P2.health > 0 and P3.health > 0:
                G6()
                G4()
        elif P1_type == 'grass' and P2_type == 'fire' and P3_type == 'fire':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    H5()
                elif Attack3 == 2:
                    H6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    G()
                elif Attack == 3:
                    G3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    H2()
                elif Attack2 == 3:
                    H4()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                G()
                H2()
            while P1.health > 0 and P3.health > 0:
                H5()
                G3()
            while P2.health > 0 and P3.health > 0:
                H6()
                H4()
        elif P1_type == 'grass' and P2_type == 'fire' and P3_type == 'electric':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    T5()
                elif Attack3 == 2:
                    T6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    G()
                elif Attack == 3:
                    G3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    H2()
                elif Attack2 == 3:
                    H4()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                G()
                H2()
            while P1.health > 0 and P3.health > 0:
                T5()
                G3()
            while P2.health > 0 and P3.health > 0:
                T6()
                H4()
        elif P1_type == 'grass' and P2_type == 'fire' and P3_type == 'grass':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    G5()
                elif Attack3 == 2:
                    G6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    G()
                elif Attack == 3:
                    G3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    H2()
                elif Attack2 == 3:
                    H4()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                G()
                H2()
            while P1.health > 0 and P3.health > 0:
                G5()
                G3()
            while P2.health > 0 and P3.health > 0:
                G6()
                H4()
        elif P1_type == 'grass' and P2_type == 'electric' and P3_type == 'fire':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    H5()
                elif Attack3 == 2:
                    H6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    G()
                elif Attack == 3:
                    G3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    T()
                elif Attack2 == 3:
                    T4()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                T()
                G()
            while P1.health > 0 and P3.health > 0:
                H5()
                G3()
            while P2.health > 0 and P3.health > 0:
                H6()
                T4()
        elif P1_type == 'grass' and P2_type == 'electric' and P3_type == 'electric':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    T5()
                elif Attack3 == 2:
                    T6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    G()
                elif Attack == 3:
                    G3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    T()
                elif Attack2 == 3:
                    T4()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                G()
                T()
            while P1.health > 0 and P3.health > 0:
                T5()
                G3()
            while P2.health > 0 and P3.health > 0:
                T6()
                T4()
        elif P1_type == 'grass' and P2_type == 'electric' and P3_type == 'grass':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    G5()
                elif Attack3 == 2:
                    G6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    G()
                elif Attack == 3:
                    G3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    T()
                elif Attack2 == 3:
                    T4()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                G()
                T()
            while P1.health > 0 and P3.health > 0:
                G5()
                G3()
            while P2.health > 0 and P3.health > 0:
                G6()
                T4()
        elif P1_type == 'grass' and P2_type == 'grass' and P3_type == 'fire':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    H5()
                elif Attack3 == 2:
                    H6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    G()
                elif Attack == 3:
                    G3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    G2()
                elif Attack2 == 3:
                    G4()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                G()
                G2()
            while P1.health > 0 and P3.health > 0:
                G5()
                G3()
            while P2.health > 0 and P3.health > 0:
                G6()
                G4()
        elif P1_type == 'grass' and P2_type == 'grass' and P3_type == 'electric':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    T5()
                elif Attack3 == 2:
                    T6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    G()
                elif Attack == 3:
                    G3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    G2()
                elif Attack2 == 3:
                    G4()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                G()
                G2()
            while P1.health > 0 and P3.health > 0:
                T5()
                G3()
            while P2.health > 0 and P3.health > 0:
                T6()
                G4()
        elif P1_type == 'grass' and P2_type == 'grass' and P3_type == 'grass':
            while P1.health > 0 and P2.health > 0 and P3.health > 0:
                Attack3 = int(input('Player 3, Who do you want to attack? (Type 1 for Player 1 and 2 for Player 2): '))
                if Attack3 == 1:
                    G5()
                elif Attack3 == 2:
                    G6()
                else:
                    print('Lose a Turn!')
                Attack = int(input('Player 1, Who do you want to attack? (Type 2 for Player 2 and 3 for Player 3): '))
                if Attack == 2:
                    G()
                elif Attack == 3:
                    G3()
                else:
                    print('Lose a Turn!')
                Attack2 = int(input('Player 2, Who do you want to attack? (Type 1 for Player 1 and 3 for Player 3): ')) 
                if Attack2 == 1:
                    G2()
                elif Attack2 == 3:
                    G4()
                else:
                    print('Lose a Turn!')
            while P1.health < 0 or P1.health == 0:
                print(P1.name, 'You Died!')
                exit()
            while P2.health < 0 or P2.health == 0:
                print(P2.name, 'You Died!')
                exit()
            while P3.health < 0 or P3.health == 0:
                print(P3.name, 'You Died!')
                exit()
            while P1.health > 0 and P2.health > 0:
                G()
                G2()
            while P1.health > 0 and P3.health > 0:
                G5()
                G3()
            while P2.health > 0 and P3.health > 0:
                G6()
                G4()
elif Mode == 4:
    P1_name = input('Player1, Type your name: ')
    Type = input('Do you want to be Fire, Electric, Grass (Make sure to type in all lowercase): ')
    P1 = Characters(90, Type, P1_name)
    C = Characters(150, 'Dark', 'Computer')
    print('')
    print('It seems you are lonely :(')
    print("But don't fear there is a computer! :) ")
    print("Without further ado, Let's begin!")
    print('')
    if Type == 'fire':
        while P1.health > 0 and C.health > 0:
            H1()
            C1()
        while P1.health < 0 or P1.health == 0:
            print(P1.name, 'You Lost!')
            exit()
        while C.health < 0 or C.health == 0:
            print('You Won!')
            exit()
        while C.health < 0 or C.health == 0 and P1.health < 0 or P1.health == 0:
            print('You Tied!')
            exit()
    if Type == 'electric':
        while P1.health > 0 and C.health > 0:
            T1()
            C1()
        while P1.health < 0 or P1.health == 0:
            print(P1.name, 'You Lost!')
            exit()
        while C.health < 0 or C.health == 0:
            print('You Won!')
            exit()
        while C.health < 0 or C.health == 0 and P1.health < 0 or P1.health == 0:
            print('You Tied!')
            exit()
    elif Type == 'grass':
        while P1.health > 0 and C.health > 0:
            G1()
            C1()
        while P1.health < 0 or P1.health == 0:
            print(P1.name, 'You Lost!')
            exit()
        while C.health < 0 or C.health == 0:
            print('You Won!')
            exit()
        while C.health < 0 or C.health == 0 and P1.health < 0 or P1.health == 0:
            print('You Tied!')
            exit()
elif Mode == 5:
    P1_name = input('Player 1, Type your name: ')
    P1_type = input('Player 1, Pick a type (Fire, Electric, or Grass): ')
    P2_name = input('Player 2, Type your name: ')
    P2_type = input('Player 2, Pick a type (Fire, Electric, or Grass): ') 
    P1 = Characters(110, P1_type, P1_name)
    P2 = Characters(150, P2_type, P2_name)
    value = random.randint(0, 1)
    if value == 0:
        value = 'heads'
    if value == 1:
        value = 'tails'
    print(P2.name,'         V.S.      ', P1.name)
    print(P2.health,'hp', '                 ', P1.health, 'hp')
    print(P2.type, '               ',  P1.type)
    print('')
    print(P2.name,', do you want to choose Heads or Tails?')
    Coin = input("Type the side the side you want (Make sure to type all lowercase): ")
    if Coin == 'heads':
        print('Good Choice!')
    elif Coin == 'tails':
        print('Good Choice')
    print(P2.name, ' flips coin')
    print('The Coin lands', value, '!')
    if value == Coin:
        print(P2.name, ' Goes First!')
    elif value != Coin:
        print(P1.name, ' Goes First!')
    print("Let's start the battle")
    print('')
    if value == Coin:
        while P2.health > 0 and P1.health > 0:
            if P1.type == 'fire' and P2.type == 'electric':                                 
                T()
                H()
            elif P1.type == 'fire' and P2.type == 'grass':
                G2()
                H()
            elif P1.type == 'fire' and P2.type == 'fire':
                H()
                H2()
            elif P1.type == 'electric' and P2.type == 'fire':
                H2()
                T2()
            elif P1.type == 'electric' and P2.type == 'electric':
                T()
                T2()
            elif P1.type == 'electric' and P2.type == 'grass':
                T2()
                G2()
            elif P1.type == 'grass' and P2.type == 'fire':
                H2()
                G()
            elif P1.type == 'grass' and P2.type == 'electric':
                T()
                G()
            elif P1.type == 'grass' and P2.type == 'grass':
                G2()
                G()
        while P1.health == 0 or P1.health < 0:
            print(P2.name, ' Wins!')
            exit()
        while P2.health == 0 or P2.health < 0:
            print(P1.name, ' Wins!')
            exit()
        while P2.health < 0 or P2.health == 0 and P1.health < 0 or P1.health == 0:
            print('You tied!')
            exit()
    elif value != Coin:
        while P1.health > 0 and P2.health > 0:
            if P1.type == 'fire' and P2.type == 'electric':                                 
                H()
                T()
            elif P1.type == 'fire' and P2.type == 'grass':
                H()
                G2()
            elif P1.type == 'fire' and P2.type == 'fire':
                H2()
                H()
            elif P1.type == 'electric' and P2.type == 'fire':
                T2()
                H2()
            elif P1.type == 'electric' and P2.type == 'electric':
                T2()
                T()
            elif P1.type == 'electric' and P2.type == 'grass':
                G2()
                T2()
            elif P1.type == 'grass' and P2.type == 'fire':
                G()
                H2()
            elif P1.type == 'grass' and P2.type == 'electric':
                G()
                T()
            elif P1.type == 'grass' and P2.type == 'grass':
                G()
                G2()
        while P1.health == 0 or P1.health < 0:
            print(P2.name, ' Wins!')
            exit()
        while P2.health == 0 or P2.health < 0:
            print(P1.name,'Wins!')
            exit()
        while P2.health < 0 or P2.health == 0 and P1.health < 0 or P1.health == 0:
            print('You tied!')
            exit()
elif Mode == 'Work in Progress':
    P1_name = input('Player 1, what is your name: ')
    P1_type = input('Player 1, what is your type (fire, electric, or grass): ')
    P2_name = input('Player 2, what is your name: ')
    P2_type = input('Player 2, what is your type (fire, electric, or grass): ')
    print('You are team 1!')
    P3_name = input('Player 3, what is your name: ')
    P3_type = input('Player 3, what is your type (fire, electric, or grass): ')
    P4_name = input('Player 4, what is your name: ')
    P4_type = input('Player 4, what is your type (fire, electric, or grass): ')
    print('You are team 2!')
    print('We are going to flip a coin to see who goes first')
    Coin = random.randint(1, 2)
    if Coin == 1:
        Coin = 'heads'
        print('The Coin lands heads!')
        print('Team 1 Goes First!')
    elif Coin == 2:
        Coin = 'tails'
        print('The Coin lands tails!')
        print('Team 2 Goes First!')
elif Mode == 6:
    print('Welcome to Story Mode!')
    P1_name = input('What is your name: ')
    P1_type = input('What is your type? (fire, electric, or grass): ')
    P1 = Characters(150, P1_type, P1_name)
    print('')
    print('You get woken by your friends.') ; sleep(3.5)
    print("They tell you Lets go to the forest!") ; sleep(3.5)
    print('You ask why?') ; sleep(2)
    print('To catch mysterious monsters for our collection!, they say.') ; sleep(3.5)
    print('')
    D1 = input('Do you want to go?: ')
    if D1 == 'no':
        print('You refuse their advice, and go back to bed.') ; sleep(3.5)
        print("You go back to sleep and don't go on the adventure.") ; sleep(3.5)
        print('You unlocked the Boring Ending!') ; sleep(3.5)
        exit()
    elif D1 == 'yes':
        print('You decided to go with your friends into the forest!') ; sleep(3.5)dsa
        print('After walking for a hour, you see a cave.') ; sleep(3.5)
        print('Your friends start to walk in the cave.') ; sleep(3.5)
        D2 = input('Do you go in with them?: ')
        if D2 == 'yes':
            print('When you walk into the cave, you start to hear noises.') ; sleep(3.5)
            print("That's when a pack of orgs and they look hungry, Let's Battle!")
        elif D2 == 'no':
            print()
    else:
        print('Not a valid option')
else:
    print("You can't even type a number between 1 and 6.")
    exit()