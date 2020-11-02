from opcua import Client  # module for working with a client
import time
import os
import one_meaning as om
import keeping_the_list as keep_l

# точка запуска
def main():
    ip_port = input('enter "ip:port">')
    try:
        url = str("opc.tcp://"+ip_port) # server address "opc.tcp://ip:port"
        client = Client(url)  # customer creation
        client.connect_socket()
        client.send_hello()
        client.open_secure_channel()
        client.create_session()

        # list values
        print("\n<===List values===>")
        keep_l.get_server(client)
        keep_l.get_user_identity_tokens(client)

        # one meaning
        print("\n<===One meaning===>")
        om.get_endpoint_url(client)
        om.get_security_level(client)
        om.get_security_mode(client)
        om.get_security_policy_uri(client)
        om.get_transport_profile_uri(client)
        om.get_server_certificate_x509()
        om.get_server_certificate_subprocess()
            

        client.close_secure_channel()
        client.disconnect_socket()

        os._exit(1)
        
    except Exception as exp:
        print(exp)
        os._exit(1)

if __name__ == "__main__":
    main()