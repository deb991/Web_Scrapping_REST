import os
import urllib
from urllib.request import urlopen
import json
from pprint import pprint

'''Basic HTTP Get request using urllib.request'''
def http_get():
    with urlopen("https://www.example.com") as response:
        body = response.read()
        print('Body:\t', body)
    return body

'''REST API to get JSON Data'''
def get_json():
    with urlopen("https://jsonplaceholder.typicode.com/todos/1") as response:
        body = response.read()
        #print('Response:\t', body)
    json_data = json.loads(body)
    print('JSOn_Data:\t', json_data)

'''HTTP Message is like text but transmitting in a stream of byte'''
'''Target server www.google.com has enough information to make a response'''
'''Understanding urllib.request represents an HTTP Message'''
def get_http_msg():
    with urlopen("https://www.example.com") as g_response:
        #pprint(dir(g_response))
        print('Header:\t{}, \nServer_Heder:\t{}'.format(g_response.headers, g_response.getheader("Server")))

'''Closing an HTTP response'''
def response_close():
    response = None
    try:
        response = urlopen("https://www.example.com")
    except Exception as ex:
        print(ex)
    else:
        body = response.read(50)
        '''First 50 bytes reading from response HTTPS message'''
        print('Body:\t', body)
        #print('Body First 50 bytes:\t', response.read(50))
    finally:
        if response is not None:
            response.close()
            print('response closed')

'''Exploring Text, Octets, Bits'''
def explore_response():
    '''Https message response are byte object
    so this need to be converted into strings to make it readable'''
    encode_response = ''
    with urlopen("https://example.com") as encode_response:
        src_data = encode_response.read()
        #print('Byte formatted response:\t', src_data)
        '''Getting Charset from header of the HTTPS message'''
        char_set = encode_response.headers.get_content_charset()
        print('Char_Set:\t', char_set)
        decode_response = src_data.decode(char_set)
        #print('\nDecoded response:\t', decode_response[:500])
        '''from Bytes to File'''
        with open("../res/http_message1.html", "wb") as msg_file:
            msg_file.write(src_data)


if __name__ == '__main__':
    #http_get()
    #get_json()
    #get_http_msg()
    #response_close()
    explore_response()