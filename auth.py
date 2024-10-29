from os import path, popen, remove
from time import sleep
from requests import post, head, Session, ConnectionError
from getpass import getpass
import re

regex_data = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"

def _GetchWindows():
    # This reads only one character.
    from msvcrt import getch
    return getch()


def login(uname, passw):
    url_1 = 'http://www.google.co.in'

    headers = \
        {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}

    session = Session()

    res = session.get(url_1, headers=headers)
    login_url = re.findall(regex_data,res.text)[0]
    pattern = r'https://gateway\.iitj\.ac\.in'
    print(login_url)
    if re.search(pattern, login_url):
        res = session.get(login_url, headers=headers)
        magic = res.url.split('?')[1]
    else:
        print("URL does not start with 'https://gateway.iitj.ac.in'")

    
    
    # magic = login_url.split('?')[1]

    payload = {
        '4Tredir': login_url,
        'magic': str(magic),
        'username': uname,
        'password': passw,
        }

    url_2 = login_url
    pattern = r'https://gateway\.iitj\.ac\.in'
    print(login_url)
    if re.search(pattern, login_url):
         res = post(url_2, headers=headers, data=payload)
    else:
        print("URL does not start with 'https://gateway.iitj.ac.in'")

   

    if 'Failed' in res.text:
        return False
    else:
        print('Successfully authenticated, now closing this window. Bye.. :)')
        sleep(.777)
        return True


def main():
    while(True):
        try:
            print("Checking connectivity..")
            try:
                res = head('http://www.google.co.in')
                print('Already connected. :)')
            except ConnectionError:
                username = "##################"
                password = "##################"

                if login(username, password):
                    pass
                else:
                    print('Wrong credentials. Try again.\n')
                    username = input('Enter your username : ').strip()
                    password = getpass()
                    login(username, password)
        except Exception:
            sleep(5)
        sleep(5)


if __name__ == '__main__':
    main()