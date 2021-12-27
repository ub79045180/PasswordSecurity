# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 12:08:21 2021

@author: Bundu1628235
"""

from flask import Flask, render_template, request
import model

app = Flask(__name__)

# Password Checker
@app.route('/', methods = ['GET','POST'])
def p_checker():
    try: 
        if request.method == 'GET':    
            return render_template('index.html')
        else:
            input_pwd = request.form['search']
            output_res = model.main(input_pwd.split())
            return render_template('index.html', data = output_res)
    except:
        return render_template('index.html', data = 'Connection problem. Please check your internet connection')

# Payment
@app.route('/payment', methods = ['GET','POST'])
def payment():
    try: 
        if request.method == 'GET':    
            return render_template('payment.html')
        else:
            return render_template('payment.html')
    except:
        return render_template('payment.html', data = 'Connection problem. Please check your internet connection')


# Password Generator
@app.route('/pwdgen', methods = ['GET','POST'])
def inputNum():
    if request.method == 'POST':
        try:
            password_len = request.form.getlist('l_pwd')
            str_password = [str(i) for i in password_len]
            str1_password = "".join(str_password)
            password_length = int(str1_password)
            output_res_num = model.numbers(password_length)
            output_res_letter = model.letters(password_length)
            output_res_sChar = model.sChar(password_length)
            output_res_num_letter = model.numLetters(password_length)
            output_res_num_sChar = model.numSchar(password_length)
            output_res_sChar_letter = model.letterSchar(password_length)
            output_res_all = model.generateAll(password_length)
            output = request.form.getlist('options')
            if output == ['letters']:
                return render_template('pwdgen.html', data = output_res_letter)
            elif output == ['numbers']:
                return render_template('pwdgen.html', data = output_res_num)
            elif output == ['s_char']:
                return render_template('pwdgen.html', data = output_res_sChar)
            elif output == ['numbers','letters']:
                return render_template('pwdgen.html', data = output_res_num_letter)
            elif output == ['numbers','s_char']:
                return render_template('pwdgen.html', data = output_res_num_sChar)
            elif output == ['letters','s_char']:
                return render_template('pwdgen.html', data = output_res_sChar_letter)
            elif output == ['numbers','letters','s_char']:
                return render_template('pwdgen.html', data = output_res_all)
            elif output == []:
                return render_template('pwdgen.html', data1 = 'Please select an option and the length of password')
        except:
            return render_template('pwdgen.html', data1 = 'Please enter a valid number for the length of password')
    elif request.method == 'GET':
        return render_template('pwdgen.html')
    
if __name__=='__main__':
    app.run(host='0.0.0.0', port = 7000, debug = True)