import base64
import requests

def generate_obfuscated_url(legit_url, phishing_url):
    """
    Generates an obfuscated URL using a legitimate URL and a phishing URL.

    Args:
    legit_url (str): The legitimate URL that will be shown before the '@'.
    phishing_url (str): The phishing URL that will actually be visited.

    Returns:
    str: The obfuscated URL.
    """
    if not phishing_url.startswith("http://") and not phishing_url.startswith("https://"):
        phishing_url = "http://" + phishing_url
    obfuscated_url = f"{legit_url}@{phishing_url}"
    return obfuscated_url

def hex_encode_url(url):
    """
    Encodes a URL using hexadecimal encoding.

    Args:
    url (str): The URL to be encoded.

    Returns:
    str: The hex-encoded URL.
    """
    return ''.join('%{:02x}'.format(ord(c)) for c in url)

def base64_encode_url(url):
    """
    Encodes a URL using Base64 encoding.

    Args:
    url (str): The URL to be encoded.

    Returns:
    str: The Base64-encoded URL.
    """
    url_bytes = url.encode('utf-8')
    base64_bytes = base64.urlsafe_b64encode(url_bytes)
    return base64_bytes.decode('utf-8')

def url_shortener(url):
    """
    Shortens a URL using the is.gd URL shortening service.

    Args:
    url (str): The URL to be shortened.

    Returns:
    str: The shortened URL.
    """
    short_url = requests.get(f"https://is.gd/create.php?format=simple&url={url}").text.strip()
    return short_url

def main():
    # ASCII Art Title
    title = r"""
 ________ ___  ________  ___  ___  ________  ___  ___  ___  ________  ___  ___     
|\  _____\\  \|\   ____\|\  \|\  \|\   __  \|\  \|\  \|\  \|\   ____\|\  \|\  \    
\ \  \__/\ \  \ \  \___|\ \  \\\  \ \  \|\  \ \  \\\  \ \  \ \  \___|\ \  \\\  \   
 \ \   __\\ \  \ \_____  \ \   __  \ \   ____\ \   __  \ \  \ \_____  \ \   __  \  
  \ \  \_| \ \  \|____|\  \ \  \ \  \ \  \___|\ \  \ \  \ \  \|____|\  \ \  \ \  \ 
   \ \__\   \ \__\____\_\  \ \__\ \__\ \__\    \ \__\ \__\ \__\____\_\  \ \__\ \__\
    \|__|    \|__|\_________\|__|\|__|\|__|     \|__|\|__|\|__|\_________\|__|\|__|
                 \|_________|                                 \|_________|         
    """
    print(title)

    # Prompt the user for the URLs
    legit_url = input("Enter the legitimate URL (e.g., https://youtube.com): ")
    phishing_url = input("Enter the phishing URL (e.g., malicious.com): ")

    # Prompt the user for the obfuscation method
    print("\nChoose the action:")
    print("1. Generate obfuscated URL")
    print("2. Hex encode ")
    print("3. Base64 encode ")
    print("4. Shorten URL with is.gd")
    print("5. Shorten URL with is.gd and obfuscate")
    action = input("Enter the number of the desired action: ")

    if action == '1':
        obfuscated_url = generate_obfuscated_url(legit_url, phishing_url)
        print("\nGenerated obfuscated URL:", obfuscated_url)
    elif action == '2':
        obfuscated_url = f"{legit_url}@{hex_encode_url(phishing_url)}"
        print("\nGenerated obfuscated URL with hex encoding:", obfuscated_url)
    elif action == '3':
        obfuscated_url = f"{legit_url}@{base64_encode_url(phishing_url)}"
        print("\nGenerated obfuscated URL with Base64 encoding:", obfuscated_url)
    elif action == '4':
        shortened_url = url_shortener(phishing_url)
        print("\nGenerated shortened URL with is.gd:", shortened_url)
    elif action == '5':
        shortened_url = url_shortener(phishing_url)
        obfuscated_url = generate_obfuscated_url(legit_url, shortened_url)
        print("\nGenerated obfuscated URL after shortening with is.gd:", obfuscated_url)
    else:
        print("Invalid option. Please choose a valid action.")

if __name__ == "__main__":
    main()
