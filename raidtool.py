# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: raidtool.py
# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import threading
import requests
import discord
import fade
import os
from colorama import Fore, init

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_ascii_logo():
    logo_text = '                                                                     \n         ▄▄▄   ▄▄▄· ▪  ·▄▄▄▄      ▄▄▄▄▄            ▄▄▌      \n         ▀▄ █·▐█ ▀█ ██ ██▪ ██     •██  ▪     ▪     ██•                                \n         ▐▀▀▄ ▄█▀▀█ ▐█·▐█· ▐█▌     ▐█.▪ ▄█▀▄  ▄█▀▄ ██▪           \n         ▐█•█▌▐█ ▪▐▌▐█▌██. ██      ▐█▌·▐█▌.▐▌▐█▌.▐▌▐█▌▐▌          \n         .▀  ▀ ▀  ▀ ▀▀▀▀▀▀▀▀•      ▀▀▀  ▀█▄▀▪ ▀█▄▀▪.▀▀▀ \n                                                                                              \n    '
    faded_text = fade.pinkred(logo_text)
    print(faded_text)
display_ascii_logo()

def option1():
    token = input('Enter Token: ')
    channel_id = input('Enter Channel ID: ')
    message_content = input('Enter Message: ')
    repeat_count = int(input('Enter Repeat count (How many times): '))

    def spammer():
        url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
        headers = {'Authorization': token}
        payload = {'content': message_content}
        for _ in range(repeat_count):
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 204:
                print('Sending', token[:-5] + '*****', response)
            elif response.status_code == 401:
                print('error', token[:-5] + '*****', response)
            elif response.status_code == 429:
                print('error', token[:-5] + '*****', response)
            elif response.status_code == 403:
                print('Invalid', token[:-5] + '*****', response)
            else:
                print('Error', token[:-5] + '*****', response)
    thread = threading.Thread(target=spammer)
    thread.start()
    thread.join()
    input('Press Enter to return to the main menu...')

def option2():
    webhook_url = input(fade.pinkred('Enter Webhook URL: '))
    message_content = input(fade.pinkred('Enter Message: '))
    repeat_count = int(input(fade.pinkred('Enter how many times to spam: ')))

    def send_to_webhook():
        payload = {'content': message_content}
        for _ in range(repeat_count):
            response = requests.post(webhook_url, json=payload)
            if response.status_code == 204:
                print(fade.brazil('Success'), response)
            else:
                print(fade.fire('Error'), response)
    thread = threading.Thread(target=send_to_webhook)
    thread.start()
    thread.join()
    input('Press Enter to return to the main menu...')

def option3():
    clear_screen()
    token = input(fade.pinkred('Enter Your Token: '))
    user_id = input(fade.pinkred('Enter Discord User ID: '))
    message_content = input(fade.pinkred('Enter Message to Send: '))
    repeat_count = int(input(fade.pinkred('Enter How Many Times to Send the Message: ')))
    url = 'https://discord.com/api/v9/users/@me/channels'
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    payload = {'recipient_id': user_id}
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        dm_channel_id = response.json().get('id', '')
        if dm_channel_id:
            url = f'https://discord.com/api/v9/channels/{dm_channel_id}/messages'
            payload = {'content': message_content}
            for _ in range(repeat_count):
                response = requests.post(url, json=payload, headers=headers)
                if response.status_code == 200:
                    print(fade.pinkred('Message Sent Successfully'))
                else:
                    print(fade.pinkred('Error Sending Message'), response)
            input(fade.pinkred('Press Enter to Continue...'))
            clear_screen()
        else:
            print(fade.pinkred('Error Creating DM Channel'), response)
    else:
        print(fade.pinkred('Error Fetching User DM Channel'), response)
    input('Press Enter to return to the main menu...')

def option4():
    webhook = input(' Eneter webhook : ')
    delete(webhook)

def delete(webhook):
    requests.delete(webhook)
    check = requests.get(webhook)
    if check.status_code == 404:
        print('\n Webhook removed')
        os.system('pause >nul')
    elif check.status_code == 200:
        print('\n Error')
        os.system('pause >nul')
    test = requests.get(webhook)
    if test.status_code == 404:
        print('\n Invalid')
        os.system('pause >nul')
    elif test.status_code == 200:
        print('\n Valid')
        delete(webhook)

def option5():
    token = input('Enter Your Token: ')
    user_id = input('Enter User ID to Remove as Friend: ')
    url = f'https://discord.com/api/v9/users/@me/relationships/{user_id}'
    headers = {'Authorization': token}
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f'Successfully removed user {user_id} as a friend.')
    else:
        print(f'Error removing user as a friend: {response.status_code}')

def option6():
    token = input('Enter Your Token: ')
    gc_id = input('Enter GC ID: ')
    message_content = input('Enter Message to Send: ')
    repeat_count = int(input('Enter How Many Times to Send the Message: '))
    url = f'https://discord.com/api/v9/channels/{gc_id}/messages'
    headers = {'Authorization': token}
    payload = {'content': message_content}
    for _ in range(repeat_count):
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            print('Success', token[:-5] + '*****', response)
        elif response.status_code == 401:
            print('Invalid', token[:-5] + '*****', response)
        elif response.status_code == 429:
            print('Rate Limit', token[:-5] + '*****', response)
        elif response.status_code == 403:
            print('Invalid / Banned', token[:-5] + '*****', response)
        else:
            print('Unknown Error', token[:-5] + '*****', response)
    input('Press Enter to return to the main menu...')

def option9():
    while True:
        clear_screen()
        display_ascii_logo()
        print(f"{fade.pinkred('                           Page 2                      ')}")
        print(f"{fade.pinkred('         ╔═══                                    ═══╗')}")
        print(f"{fade.pinkred('         ║                                          ║  ')}")
        print(f"{fade.pinkred('           [0] Back to main          [2]   ')}")
        print(f"{fade.pinkred('           [3]                       [4] ')}")
        print(f"{fade.pinkred('           [5]                       [6]     ')}")
        print(f"{fade.pinkred('        ║                                           ║ ')}")
        print(f"{fade.pinkred('        ╚═══                                     ═══╝')}")
        choice = input('[<>] ')
        if choice == '0':
            return
        print('Invalid')

def main():
    while True:
        clear_screen()
        display_ascii_logo()
        print(f"{fade.pinkred('            Tool made by wock on discord   ')}")
        print(f"{fade.pinkred('         ╔═══                                    ═══╗')}")
        print(f"{fade.pinkred('                                                     ')}")
        print(f"{fade.pinkred('            [1] Server raid     [2] Webhook spammer')}")
        print(f"{fade.pinkred('            [3] Dm spammer      [4] Webhook remove ')}")
        print(f"{fade.pinkred('            [5] Remove friend   [6] Gc spammer      ')}")
        print(f"{fade.pinkred('                        [9]Next page                 ')}")
        print(f"{fade.pinkred('         ╚═══                                    ═══╝')}")
        choice = input('[<>] ')
        if choice == '1':
            option1()
        elif choice == '2':
            option2()
        elif choice == '3':
            option3()
        elif choice == '4':
            option4()
        elif choice == '5':
            option5()
        elif choice == '6':
            option6()
        elif choice == '7':
            option7()
        elif choice == '9':
            option9()
        else:
            print('Invalid')
if __name__ == '__main__':
    main()