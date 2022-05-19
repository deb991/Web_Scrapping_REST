import os
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
import json
import ssl
import certifi

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
        with open("C:\\Users\\002CSC744\\Documents\\Web_Scrapping_REST\\res\\http_message1.html", "wb") as msg_file:
            msg_file.write(src_data)
            '''Going from Bytes to Dictionary'''
            #json_data = json.loads(decode_response)
            #print('Json data:\t', json_data)

'''Exception Handling'''
def make_request(url):
    try:
        with urlopen(url, timeout=10) as input_data:
            body = input_data.read()
            print('Request Status:\t', input_data.status)
    except HTTPError as error:
        print(error.status, error.reason)
    except URLError as error:
        print(error.reason)
    except TimeoutError as error:
        print('\nRequest Time Out')

'''SSL/ Certifiacte issue resolution'''
def ssl_error_handling():
    '''Simply create certificate based on unvarified sites, without checking any reputation.'''

    unverified_context = ssl._create_unverified_context()

    '''Now certi is being used as a certificate store, to match & 
    create certificate with respect to some good reputation sites'''
    #certifi_context = ssl.create_default_context(cafile=certifi.where())
    test = urlopen("https://sha384.badssl.com/", context=unverified_context)
    data = test.read()
    #print('data:\t', data)

def post_urllib_request(url, headers=None, data=None):
    request = Request(url, headers=headers or {}, data=data)
    try:
        with urlopen(request, timeout=10) as response:
            print(response.status)
            return response.read(), response
    except HTTPError as error:
        print(error.status, error.reason)
    except URLError as error:
        print(error.reason)
    except TimeoutError:
        print('Request time out')

def get_post_data():
    post_dict = {"Title": "Hello World!!!", "Name":"Test API to check \nURL Post request"}
    url_encode_data = urlencode(post_dict)
    print('url_encode_data:\t', url_encode_data)

    '''To post response in simple dictionary format. '''

    #post_data = url_encode_data.encode('utf-8')

    '''TO post simple dictionary response in json format. '''

    json_str = json.dumps(post_dict)
    post_data = json_str.encode('utf-8')
    return post_data

if __name__ == '__main__':
    #http_get()
    #get_json()
    #get_http_msg()
    #response_close()
    #explore_response()
    #make_request("https://httpstat.us/403")
    #ssl_error_handling()
    post_data = get_post_data()
    body, response = post_urllib_request("https://httpbin.org/anything", data=post_data, headers={"Content-Type": "application/json"},)
    print('Body - UFT-8 Encoding_output:\t', body.decode('utf-8'))