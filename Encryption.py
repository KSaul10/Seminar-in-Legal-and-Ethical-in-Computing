# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/125rHnYmMlsgDPrIMzwilGzx5iPsLz5iz
"""

!pip install cryptography

from cryptography.fernet import Fernet

#Generate key
key = Fernet.generate_key()
Suite = Fernet(key)

#Message to encrypt
message = b"KWIHANGANA"

#Encrypt
encrypted_message = Suite.encrypt(message)
print("First_Name:",encrypted_message)

#Decrypt
decrypted_message = Suite.decrypt(encrypted_message)
print("First_Name:",decrypted_message.decode())