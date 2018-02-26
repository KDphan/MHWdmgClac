#Monster Hunter World True Damage calculations as of 1.06

import math
import sys

  
def dmg_calc():   
  DMG  = int(input('Enter your weapon damage value:'))
  if DMG <= 0:
      print('Invalid damage values, Hunter-san')
      return dmg_calc()
  
  hammer  = DMG // 5.2
  horn    = DMG // 4.2
  SA      = DMG // 3.5
  GS      = DMG // 4.8
  CB      = DMG // 3.6
  LS      = DMG // 3.3
  IG      = DMG // 3.1
  LanceGL = DMG // 2.3
  HBG     = DMG // 1.5
  SNS     = DMG // 1.4
  DB      = DMG // 1.4
  LBG     = DMG // 1.3
  Bow     = DMG // 1.2  
  
  #Sharpness Modifiers for raw damage
  green   = 1.05
  blue    = 1.20
  white   = 1.32
  
  #Sharpness Modifiers for element damage
  Egreen   = 1.00
  Eblue    = 1.0625
  Ewhite   = 1.125
  
  weapons = {'hammer': hammer, 'horn': horn, 'SA': SA,'GS': GS,'CB': CB,'LS': LS,'IG': IG,'LanceGL': LanceGL,'HBG': HBG,'SNS': SNS ,'DB': DB, 'LBG': LBG, 'Bow': Bow}
  
  sharpness  = {'green': green, 'blue': blue, 'white': white}
  Esharpness = {'green': Egreen, 'blue': Eblue, 'white': Ewhite}
  
  def weap_calc():
    WEAP = input('What is your weapon?')
    if WEAP not in weapons:
        print('invalid weapon, try inputting: hammer, horn, SA, GS, CB, LS, IG, LanceGL, HBG, SNS, DB, LBG, Bow')
        return weap_calc()
    else:
      ELEM    = int(input('What is your element damage?'))
      SHRP    = input('What is your sharpness color?')
      while SHRP not in sharpness:
        print('Invalid color, try green, blue, or white')
        SHRP    = input('What is your sharpness color?')
      else:
        eleSHRP = SHRP
        truDmg = weapons[WEAP]
        eleDmg = ELEM // 10
        truEleDmg = truDmg + eleDmg
        truEleShrpDmg = (truDmg*sharpness[SHRP]) + (eleDmg*Esharpness[eleSHRP])
      
      print('The true RAW damage for your', WEAP, 'is:', truDmg)
      print('The true RAW+ELEM damage for your', WEAP, 'is:', truEleDmg)    
      print('The true RAW+ELEM+SHARP damage for your', WEAP, 'is', truEleShrpDmg)
    return dmg_calc()
    
  weap_calc()
  
dmg_calc()








