import requests

def get_image(pokemonName):

    ##Show images 
    image_url = "https://img.pokemondb.net/artwork/large/"
    image_url += pokemonName
    image_url += '.jpg'

    try:
        # Send an HTTP GET request to the image URL
        response = requests.get(image_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Open the image using PIL (Pillow)
            data = response.content
            return data

        else:
            print(f"Failed to download image. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")
            
    return 10