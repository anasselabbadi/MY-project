import pyautogui
import sys
from time import sleep
o="No"
while o=="No":
    text = pyautogui.prompt(text='ENTER WHAT YOU WANT TEXT', title='SPAM ' , default='')
    nb = pyautogui.prompt(text='ENTER HOW MUCH TIME (1,2.......!)', title='SPAM ' , default='')
    o=pyautogui.confirm('Have you clicked inside text box where you want to write ?' ,buttons=['yes','no'])
    if o =='yes':
        sleep(5)
        for i in range (0,int(nb)):
                            pyautogui.write(text,interval=0.0005)
                            pyautogui.press('enter')
                            
    else:
        sys.exit()
