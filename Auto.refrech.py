import pyautogui
pyautogui.FAILSAFE = False
pyautogui.KEYBOARD_KEYS
ok=pyautogui.confirm('HI!!!!!!!!!!!!!!!!!MAKE SURE YOU EMPTY THE PLEAC')
'OK'
if ok=="OK":
    for i in range(1,50):
        pyautogui.rightClick(x=950, y=350)
        pyautogui.rightClick(x=960, y=400)
        pyautogui.hotkey("entre",presses=1)
else:
    ok=pyautogui.confirm('HAVE NICE DAY')
'OK'
            
            
