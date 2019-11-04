import sys
import math
from mHWtruDMG import *
from flask import Flask, request, render_template, redirect, url_for
import os
app = Flask(__name__)



@app.route('/mhw',methods = ['POST', 'GET'])
def calc():
    dmg_calc()
    if request.method == 'POST':
        return render_template('result.html',hWEAP = dmg_calc.WEAP,
                                            htruDmg = dmg_calc.truDmg,
                                            heleDmg = dmg_calc.eleDmg,
                                            htruEleShrpDmg = dmg_calc.truEleShrpDmg)


if __name__ == '__main__':
    app.debug = True
app.run(
    host=os.getenv('LISTEN', '0.0.0.0'),
    port=int(os.getenv('PORT', '8080')),
  
)

