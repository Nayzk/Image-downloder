#Import libraries
import requests #deal with HTTP requests
import shutil #deal with files


def download_image(url, filename):
    try:
        # Send a GET request to url
        response = requests.get(url, stream=True)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Open a local file in write-binary mode
            with open(filename, 'wb') as f:
                # Decode the response content and copy it to the local file
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, f)
            print("Image downloaded successfully as", filename)
        else:
            print("Failed to download image:", response.status_code)
    except Exception as e:
        print("Error:", e)

# Asking about URL and the file you want to save at..
url = input("Plz, enter your url: ")  # Put the URL of the image you want to download
filename = "path\image.jpg"  # File name to save the image in
download_image(url, filename)

