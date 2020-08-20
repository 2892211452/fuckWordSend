import pyautogui
import pyperclip
import time

print('请确保输入文字后 按enter建是发送消息。\n如果不是，请修改成是')




with open('./sentence.txt', 'r', encoding= 'utf-8', errors='ignore') as f:
    lines = f.readlines()

time.sleep(3)
count = 0
while True:
    i = lines[count % len(lines)]
    i = i.replace('\n', '')
    pyperclip.copy(i)  # 先复制
    pyautogui.hotkey('ctrl', 'v')  # 再粘贴
    pyautogui.press('enter')



    count +=1


