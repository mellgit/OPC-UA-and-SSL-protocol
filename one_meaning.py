
import ssl # option 1
from cryptography import x509
from cryptography.hazmat.backends import default_backend
import subprocess # option 2


def get_endpoint_url(client):
    print(f"\n\nEndpointUrl")
    print(client.get_endpoints()[0].EndpointUrl)
    

def get_server_certificate_x509():
    print(f"\n\nServerCertificate_x509")
    
    # файл в котором находится сертификат
    file_name = r"C:\path_to_file"

    # получение сертификата
    cert_decode = ssl.get_server_certificate(('ip_address_device', 443,))

    # запись сертификата в файл
    with open(file_name, "wb") as cert_file1:
        cert_decode = bytes([ord(char) for char in cert_decode])
        data = cert_file1.write(cert_decode)
    
    # чтение из файла в байтовой строке
    with open(file_name, "rb") as cert_file:
        pem_data = [line.strip() for line in cert_file.readlines()]
        begin = pem_data[0]
        end = pem_data[-1]

        data = b""
        for line in pem_data[1:-1]:
            data += line

        pem_data = begin + b"\n" + data + b"\n" + end

    cert = x509.load_pem_x509_certificate(
            pem_data,
            default_backend()
        )
    
    keys = [
        "Страна",
        "Город",
        "Название компании",
        "Отдел компании",
        "Веб-сайт",
    ]

    i=0
    for attr in cert.subject:
        print(f"{keys[i]}: {attr.value}")
        i+=1
        
    print(f"Серийный номер: {cert.serial_number}")
    print(f"Срок действия: {cert.not_valid_before} - {cert.not_valid_after}")
    

def get_server_certificate_subprocess():
    print(f"\n\nServerCertificate_subprocess")
    cmd = "keytool -printcert -sslserver 'ip_address':443"
    cert = subprocess.getoutput(cmd)
    print(cert)


def get_security_mode(client):
    print(f"\n\nSecurityMode")
    print(client.get_endpoints()[0].SecurityMode)


def get_security_policy_uri(client):
    print(f"\n\nSecurityPolicyUri")
    print(client.get_endpoints()[0].SecurityPolicyUri)


def get_transport_profile_uri(client):
    print(f"\n\nTransportProfileUri")
    print(client.get_endpoints()[0].TransportProfileUri)


def get_security_level(client):
    print(f"\n\nSecurityLevel")
    print(client.get_endpoints()[0].SecurityLevel)
