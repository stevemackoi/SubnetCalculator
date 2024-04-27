import sys

def make_ip_num(ip_str):
    split_ip = ip_str.split(sep='.')
    int_ip = [int(num) for num in split_ip]
    hex_ip = [format(num, '02x') for num in int_ip]
    join_ip = ''.join(hex_ip)
    ip_num = int(join_ip, 16) 
    return(ip_num)

def calculate(ip_str, cidr_int):
    hosts = 32 - cidr_int
    mask = int((cidr_int * '1' + hosts * '0'), 2)
    host_mask = int(hosts * '1', 2)
    bin_ip = make_ip_num(ip_str)
    bin_mask = int(format(mask, '032b'), 2)

    network_id = bin_ip & bin_mask
    broadcast = bin_ip | host_mask
    first_host = network_id + 1
    last_host = broadcast - 1
    my_tuple = (bin_ip, network_id, first_host, last_host, broadcast)
    return (my_tuple)

def make_ip_str(ip_num):
    octets = [0,0,0,0]
    ip_binary = format(ip_num, '032b')
    for i in range(4):
        octets[i] = str(int(ip_binary[i*8:i*8+8], 2))
    ip_str = '.'.join(octets)
    return ip_str

def pretty_print(subnet_tuple):
    label_tuple = ("IP Address:	", "Network ID:	", "First Host:	", "Last Host:	", "Broadcast:	")    
    for i in range(len(subnet_tuple)):
        print(label_tuple[i], make_ip_str(subnet_tuple[i]))

if __name__ == '__main__': 
    if len(sys.argv) == 3:       
        ip_address=str(sys.argv[1])
        cidr=int(sys.argv[2])
        results = calculate(ip_address,cidr)
        pretty_print(results)
    else:
        print("Hey! You did that wrong!")
        print("Format is <ip address> <cidr>")
        print("Example: 192.168.1.1 24")
        
