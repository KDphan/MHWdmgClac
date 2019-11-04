#Monster Hunter World True Damage calculations as of 1.06

import math
import sys
from flask import Flask, request, render_template, redirect, url_for
import os


def re_calc():
    print('Wanna calculate another weapon, Pard? (Y/N)')
    while True:
           
        choice = input("> ")
        if choice == 'b' :
            print ("You win")
            input("yay")
            break
                
        
            
def dmg_calc():
    
    dmg_calc.WEAP = request.form['weap']
    DMG  = request.form['dmg']
    ELEM = request.form['edmg']
    SHRP = request.form['sharp']
    # if DMG <= 0:
    #       print('Invalid damage values, Hunter-san')
    #       return dmg_calc()
  
    hammer  = float(DMG) // 5.2
    horn    = float(DMG) // 4.2
    SA      = float(DMG) // 3.5
    GS      = float(DMG) // 4.8
    CB      = float(DMG) // 3.6
    LS      = float(DMG) // 3.3
    IG      = float(DMG) // 3.1
    LanceGL = float(DMG) // 2.3
    HBG     = float(DMG) // 1.5
    SNS     = float(DMG) // 1.4
    DB      = float(DMG) // 1.4
    LBG     = float(DMG) // 1.3
    Bow     = float(DMG) // 1.2  
  
  #Sharpness Modifiers for raw damage
    gun     = 1.00
    green   = 1.05
    blue    = 1.20
    white   = 1.32
  
  #Sharpness Modifiers for element damage
    Egun     = 1.00
    Egreen   = 1.00
    Eblue    = 1.0625
    Ewhite   = 1.125
  
    weapons = {'hammer': hammer, 'horn': horn, 'SA': SA,'GS': GS,'CB': CB,'LS': LS,'IG': IG,'LanceGL': LanceGL,'HBG': HBG,'SNS': SNS ,'DB': DB, 'LBG': LBG, 'Bow': Bow}
          
    sharpness  = {'green': green, 'blue': blue, 'white': white, 'gun': gun}
    Esharpness = {'green': Egreen, 'blue': Eblue, 'white': Ewhite, 'gun':Egun}
    
    eleSHRP = SHRP
    dmg_calc.truDmg = weapons[dmg_calc.WEAP]
    dmg_calc.eleDmg = float(ELEM) // 10
    truEleDmg = dmg_calc.truDmg + dmg_calc.eleDmg
    dmg_calc.truEleShrpDmg = (dmg_calc.truDmg*sharpness[SHRP]) + (dmg_calc.eleDmg*Esharpness[eleSHRP])
    
    
    # return WEAP, truDmg, eleDmg, truEleShrpDmg
    
    # damage_result = (" Weapon: " + str(WEAP) + 
    #                 " \nDamage: " + str(truDmg) + 
    #                 " \nElement: " + str(eleDmg) + 
    #                 " \nTrue Damage: " + str(truEleShrpDmg))
    
    # return damage_result
      
    # def weap_calc():
    #     WEAP = input('What is your weapon?').casefold()
    #     if WEAP not in weapons:
    #             print('invalid weapon, try inputting: hammer, horn, SA, GS, CB, LS, IG, LanceGL, HBG, SNS, DB, LBG, Bow')
    #             return weap_calc()
    #     else:
    #           ELEM    = int(input('What is your element damage?'))
    #           SHRP    = input('What is your sharpness color?')
    #           while SHRP not in sharpness:
    #             print('Invalid color, try green, blue, or white')
    #             SHRP    = input('What is your sharpness color?')
    #           else:
    #             eleSHRP = SHRP
    #             truDmg = weapons[WEAP]
    #             eleDmg = ELEM // 10
    #             truEleDmg = truDmg + eleDmg
    #             truEleShrpDmg = (truDmg*sharpness[SHRP]) + (eleDmg*Esharpness[eleSHRP])
                
    #           print('The true RAW damage for your', WEAP, 'is: ', truDmg)
    #           print('The true RAW+ELEM damage for your', WEAP, 'is: ', truEleDmg)    
    #           print('The true RAW+ELEM+SHARP damage for your', WEAP, 'is ', truEleShrpDmg)
        #re_calc()
    #weap_calc()
#dmg_calc()
    
 

