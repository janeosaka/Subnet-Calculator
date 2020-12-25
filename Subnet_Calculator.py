import random
import sys


def subnet_calculator():
    try:  # handle keyboard interrupting commands
        print()

        # Checking validity of IP address
        while True:
            ip_address = input("Enter an IP address")

            # Checking octets
            ip_octets = ip_address.split(' ')

            if (len(ip_octets) == 4) and (1 <= int(ip_octets[0]) <= 233) and (int(ip_octets[0]) != 127) and (
                    int(ip_octets[0]) != 169 or int(ip_octets[1]) != 254) and (
                    0 <= int(ip_octets[1]) <= 255 and 0 <= int(ip_octets[2]) <= 255 and 0 <= int(ip_octets[3]) <= 255):
                break
            else:
                print("\nInvalid IP address, please try a different IP address")
                continue

        masks = [255, 254, 252, 248, 240, 224, 192, 128, 0]

        # Checking validity subnet mask
        while True:
            subnet_mask = input("Enter a subnet mask: ")

            # Checking octets
            mask_octets = subnet_mask.split('.')

            if (len(mask_octets) == 4) and (int(mask_octets[0]) == 255) and (int(mask_octets[1]) in masks) and (
                    int(mask_octets[2]) in masks) and (int(mask_octets[3]) in masks) and (
                    int(mask_octets[0]) >= int(mask_octets[1]) >= int(mask_octets[2]) >= int(mask_octets[3])):
                break
            else:
                print("\nInvalid subnet mask, please try a different subnet mask")
                continue

        # Convert mask to binary string
        mask_octets_binary = []

        for octet in mask_octets:
            binary_octet = bin(int(octet)).lstrip('0b')
            mask_octets_binary.append(binary_octet.zfill(8))  # padding to fill up all bin octet length that are <8 bit

        binary_mask = "".join(mask_octets_binary)

        # Counting host bits in the mask and calculating number of hosts/subnet
        no_of_zeros = binary_mask.count("0")
        no_of_ones = 32 - no_of_zeros
        no_of_hosts = abs(2 ** no_of_zeros - 2) # taking into account of /32 subnet


    except KeyboardInterrupt:
        print("bla")
