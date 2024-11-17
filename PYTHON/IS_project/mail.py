import smtplib 

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

import qrcode
def test():
    #template to send mail
    server = smtplib.SMTP('smtp.gmail.com' , 587)

    server.starttls()
    print("starting server")
    #enable 2fa in senders account create a new apppassword
    #here is the receivers mail
    #password for senders requires you to create a apppassword
    #https://www.youtube.com/watch?v=weA4yBSUMXs
    #link to create app password
    server.login('isprojectmit2024@gmail.com' , 'cbyn eoro gief jtof')
    print("login")
    #here is the senders mail
    server.sendmail('isprojectmit2024@gmail.com' , 'dummy@gmail.com' , 'Hi there')

    print("Mail sent")

def generate_keys():

    # Generate RSA keys
    key = RSA.generate(2048)
    private_key = key
    public_key = key.publickey()
    # Export keys to PEM format
    private_key_pem = private_key.export_key('DER')
    public_key_pem = public_key.export_key('DER')

    return private_key_pem.hex() , public_key_pem.hex()
     
def send_key(user, private_key):
    server = smtplib.SMTP('smtp.gmail.com' , 587)

    server.starttls()
    print("starting server")
    #enable 2fa in senders account create a new apppassword
    #here is the receivers mail
    #password for senders requires you to create a apppassword
    #https://www.youtube.com/watch?v=weA4yBSUMXs
    #link to create app password
    server.login('isprojectmit2024@gmail.com' , 'cbyn eoro gief jtof')
    print("login")
    #here is the senders mail
    server.sendmail('isprojectmit2024@gmail.com' , user , private_key)

    print("Mail sent")


def store_in_database(user , public_key):
    #TODO 
    #USer id and public key in hex form is stored
    #Complete the storing function and make sure to check the data base to see if user email is present
    return 0


def get_string_from_db():
    #TODO
    #Get the string for speech recognition

    return 0
def encrypt(string , public_key_hex):
    public_key_bytes = bytes.fromhex(public_key_hex)
    public_key = RSA.import_key(public_key_bytes)

    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(string)

    return ciphertext

def decrypt(private_key_hex):
    private_key_bytes = bytes.fromhex(private_key_hex)
    private_key = RSA.import_key(private_key_bytes)
    cipher  = PKCS1_OAEP.new(private_key)
    data= cipher.decrypt(cipher)
     
    # Create a QR Code instance
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction used for the QR Code
        box_size=10,  # controls how many pixels each “box” of the QR code is
        border=4,  # controls how many boxes thick the border should be
    )

    # Add data to the QR Code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    img.save("qrcode.png")

    print("QR Code generated and saved as 'qrcode.png'")
 


    
    
def main():
    print("getting key for the user");
    private_key , public_key = generate_keys();
    #add the users email here
    user = "dummyemail@gmail.com"

