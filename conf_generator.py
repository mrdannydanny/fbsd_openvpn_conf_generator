import subprocess


def run(cmd):
    try:
        ssh = 'ssh root@' + server_ip_addr
        return subprocess.check_output(ssh + cmd, stderr=subprocess.STDOUT, shell=True)
    except Exception:
        raise


def build_client(client_name, server_ip_addr):
    cmd = " 'cd /usr/local/etc/openvpn/easy-rsa/ &&" \
          " ./easyrsa.real build-client-full " + client_name + " nopass'"
    run(cmd)


def update_template(client_name):
    with open('client_template.conf', "r") as fin:
        buffer = fin.readlines()
    with open(client_name + '.conf', "w") as fout:
        for line in buffer:
            if '<ca>' in line:
                line = line + grab_file_content('/usr/local/etc/openvpn/easy-rsa/pki/ca.crt')
            elif '<cert>' in line:
                line = line + grab_file_content('/usr/local/etc/openvpn/easy-rsa/pki/issued/' +
                                                client_name + '.crt', key=True)
            elif '<key>' in line:
                line = line + grab_file_content('/usr/local/etc/openvpn/easy-rsa/pki/private/' +
                                                client_name + '.key')
            elif 'proto udp' in line:
                line = line + 'remote ' + server_ip_addr + ' 1194\n'
            fout.writelines(line)


def grab_file_content(file_path, key=False):
    output = run(' cat ' + file_path)
    if key:
        output_key = run(" tail -n 20 " + file_path)
        return output_key.decode('utf-8')
    return output.decode('utf-8')


def main():
    global server_ip_addr
    client_list = input('[*] Client Name: ')
    server_ip_addr = input('[*] Server IP Address: ')

    for client_name in client_list.split():
        build_client(client_name, server_ip_addr)
        update_template(client_name)


if __name__ == '__main__':
    main()
