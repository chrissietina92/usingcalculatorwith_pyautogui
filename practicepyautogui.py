import webbrowser, pyautogui, subprocess, os, re


regex = re.compile(r'(?<==)\d+')
#this regex gets the numbers from pyautogui.locateCenterOnScreen() by creating a lists of numbers that follow a = sign
select = 0

calcPics = {
    '1' : 'calculator/one.png',
    '2' : 'calculator/two.png',
    '3' : 'calculator/three.png',
    '4' : 'calculator/four.png',
    '5' : 'calculator/five.png',
    '6' : 'calculator/six.png',
    '7' : 'calculator/seven.png',
    '8' : 'calculator/eight.png',
    '9' : 'calculator/nine.png',
    '-' : 'calculator/minus.png',
    '+' : 'calculator/add.png',
    '/' : 'calculator/div.png',
    '*' : 'calculator/multiply.png',
    '=' : 'calculator/equals.png',
    '0' : 'calculator/zero.png'

    }
# a dictionary with numbers and operators with their image file paths


def click(button):
    z = pyautogui.locateCenterOnScreen(button)
    r = regex.findall(str(z))
    cord = []
    for i in r:
        numb = int(i)
        cord.append(numb)
    a = cord[0]
    b = cord[1]
    pyautogui.moveTo(a,b, 0.9)
    pyautogui.click()
    pyautogui.moveTo(580,820, 0.8)
    pyautogui.click()

calcProc = subprocess.Popen('/Applications/Calculator.app/Contents/MacOS/Calculator')
print('Welcome to using a the mac calculator without opening the app manually.')
print('This programme will keep going until you chose the =')

while select != '=':
    print('Select the calculator button you want to select next.')
    select = input()
    chosenButton = calcPics.get(select)
    click(chosenButton)
    
print('You have your answer!')


