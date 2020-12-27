import random
import sys


# Checking validity of IP address
def ip_valid():
    while True:
        ip_address = input("Enter an IP address: ")

        # Checking octets
        ip_octets = ip_address.split('.')

        if (len(ip_octets) == 4) and (1 <= int(ip_octets[0]) <= 223) and (int(ip_octets[0]) != 127) and (
                int(ip_octets[0]) != 169 or int(ip_octets[1]) != 254) and (
                0 <= int(ip_octets[1]) <= 255 and 0 <= int(ip_octets[2]) <= 255 and 0 <= int(ip_octets[3]) <= 255):
            return ip_octets
        else:
            print("\nInvalid IP address, please try a different IP address")
            continue


# Checking validity subnet mask
def subnet_mask_valid():
    masks = [255, 254, 252, 248, 240, 224, 192, 128, 0]
    while True:
        subnet_mask = input("Enter a subnet mask: ")

        # Checking octets
        mask_octets = subnet_mask.split('.')

        if (len(mask_octets) == 4) and (int(mask_octets[0]) == 255) and (int(mask_octets[1]) in masks) and (
                int(mask_octets[2]) in masks) and (int(mask_octets[3]) in masks) and (
                int(mask_octets[0]) >= int(mask_octets[1]) >= int(mask_octets[2]) >= int(mask_octets[3])):
            return mask_octets
        else:
            print("\nInvalid subnet mask, please try a different subnet mask")
            continue


# Generate random IP address
def generate_ip(bst_ip_address, net_ip_address):
    while True:
        answer = input("Generate random IP address? [Y/N] ").lower()

        if answer == "y":
            generated_ip = []

            # Obtain available IP addr in range, based on difference between octets in broadcast addr & network addr
            for indexb, oct_bst in enumerate(bst_ip_address):
                for indexn, oct_net in enumerate(net_ip_address):
                    if indexb == indexn:
                        if oct_bst == oct_net:
                            # Add identical octets to the generated_ip list
                            generated_ip.append(oct_bst)
                        else:
                            generated_ip.append(str(random.randint(int(oct_net), int(oct_bst))))

            random_ip = ".".join(generated_ip)
            print("Random IP address is: %s" % random_ip)
            continue
        else:
            return


# Convert mask to binary string
def mask_to_bin_string(mask_octets):
    mask_octets_binary = []

    for octet in mask_octets:
        binary_octet = bin(int(octet)).lstrip('0b')
        mask_octets_binary.append(binary_octet.zfill(8))  # padding to fill up all bin octet length that are <8 bit

    binary_mask = "".join(mask_octets_binary)
    return binary_mask


# Convert IP to binary string
def ip_to_bon_string(ip_octets):
    ip_octets_binary = []

    for octet in ip_octets:
        binary_octet = bin(int(octet)).lstrip('0b')
        ip_octets_binary.append(binary_octet.zfill(8))

    binary_ip = "".join(ip_octets_binary)
    return binary_ip


# Getting wildcard masks
def generate_wildcard_mask(mask_octets):
    wildcard_octets = []

    for octet in mask_octets:
        wild_octet = 255 - int(octet)
        wildcard_octets.append(str(wild_octet))

    wildcard_mask = ".".join(wildcard_octets)
    return wildcard_mask


def subnet_calculator():
    try:  # handle keyboard interrupting commands
        print()

        ip_octets = ip_valid()
        mask_octets = subnet_mask_valid()
        binary_mask = mask_to_bin_string(mask_octets)

        # Counting host bits in the mask and calculating number of hosts/subnet
        no_of_zeros = binary_mask.count("0")
        no_of_ones = 32 - no_of_zeros
        no_of_hosts = abs(2 ** no_of_zeros - 2)  # taking into account of /32 subnet

        wildcard_mask = generate_wildcard_mask(mask_octets)
        binary_ip = ip_to_bon_string(ip_octets)

        # Get network address and broadcast address
        network_address_binary = binary_ip[:no_of_ones] + "0" * no_of_zeros
        broadcast_address_binary = binary_ip[:no_of_ones] + "1" * no_of_zeros

        # Convert back to decimal
        net_ip_octets = []

        # 1st octet - index 0-7, 2nd octet - index 8-15, 3rd octet - index 16-23, 4th octet - index 24-31
        for bit in range(0, 32, 8):
            net_ip_octet = network_address_binary[bit: bit + 8]
            net_ip_octets.append(net_ip_octet)

        net_ip_address = []

        for octet in net_ip_octets:
            net_ip_address.append(str(int(octet, 2)))

        network_address = ".".join(net_ip_address)

        bst_ip_octets = []

        for bit in range(0, 32, 8):
            bst_ip_octet = broadcast_address_binary[bit: bit + 8]
            bst_ip_octets.append(bst_ip_octet)

        bst_ip_address = []

        for octet in bst_ip_octets:
            bst_ip_address.append(str(int(octet, 2)))

        broadcast_address = ".".join(bst_ip_address)

        print("\n")
        print("Network address: %s" % network_address)
        print("Broadcast address: %s" % broadcast_address)
        print("Number of valid hosts per subnet: %s" % no_of_hosts)
        print("Wildcard mask: %s" % wildcard_mask)
        print("Mask bits: %s" % no_of_ones)
        print("\n")

        generate_ip(bst_ip_address, net_ip_address)

    except KeyboardInterrupt:
        print("bla")
        sys.exit()


subnet_calculator()
