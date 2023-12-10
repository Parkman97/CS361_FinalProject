from random import randint
import requests
import socket
from Sockets import api_socket

def randompokemon():
    HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
    PORT = 12346  # Port to listen on (non-privileged ports are > 1023)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        try:
            value = randint(0,1018)
            url = 'https://pokeapi.co/api/v2/pokemon/'
            url += str(value)
            try:
                # Send an HTTP GET request to the image URL
                response = requests.get(url)

                # Check if the request was successful (status code 200)
                if response.status_code == 200:
                    data = response.json()
                    name = data['forms'][0]['name']
                    api_socket.send((f"pokemon/{name}").encode('utf-8'))

                    return 3

                else:
                    print(f"Failed to download image. Status code: {response.status_code}")

            except Exception as e:
                print(f"An error occurred: {e}")

        except IndexError as error:
                print('\nSection: Function to Create Instances of WebDriver\nCulprit: random.choice(ua_strings)\nIndexError: {}\n'.format(error))

        except ConnectionResetError:
            print("Connection reset by peer")
            
        except Exception as e:
            print(f"Error: {e}")