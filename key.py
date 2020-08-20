import keyboard
import datetime
import time
import threading

import pyautogui
import pyperclip
import time

print('请确保输入文字后 按enter建是发送消息。\n如果不是，请修改成是\n\n 按S建stop或者start')




stop_time = input('请输入每次喷人得间隔时间')



with open('./sentence.txt', 'r', encoding= 'utf-8', errors='ignore') as f:
    lines = f.readlines()


flag = False



for i in range(5):
    print('剩余开喷时间：' + str(5-i) + " s")
    time.sleep(1)


def main():
    count = 0
    while True:

        if flag:
            time.sleep(2)
            continue

        time.sleep(float(stop_time))
        i = lines[count % len(lines)]
        i = i.replace('\n', '')
        pyperclip.copy(i)  # 先复制
        pyautogui.hotkey('ctrl', 'v')  # 再粘贴
        pyautogui.press('enter')

        count += 1


def abc(x):

    a = keyboard.KeyboardEvent('down', 28, 's')
    #按键事件a为按下enter键，第二个参数如果不知道每个按键的值就随便写，
    #如果想知道按键的值可以用hook绑定所有事件后，输出x.scan_code即可
    global  flag
    if x.event_type == 'down' and x.name == a.name:
        if flag:
            flag = False
            print('开启脚本')
        else:
            flag = True
            print('关闭脚本')

    #当监听的事件为enter键，且是按下的时候

def listen():

    keyboard.hook(abc)

    # keyboard.hook_key('enter', bcd)

    # recorded = keyboard.record(until='esc')
    keyboard.wait()


t1 = threading.Thread(target=listen)  # 创建多线程实例，Thread中target是需要子线程执行的函数
t2 = threading.Thread(target=main)
t1.start()
t2.start()


