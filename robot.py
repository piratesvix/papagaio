import pyautogui

pyautogui.PAUSE = 1

# executar uma tarefa
pyautogui.hotkey('winleft','r')
# digitar nome da tarefa
pyautogui.write('cmd')
# executar tarefa
pyautogui.press('enter')