
import ssl
import socket
import OpenSSL
from pprint import pprint
from datetime import datetime

class SSLCertificate(object):

    def __init__(self):
        self._common_name = None
        self._country = None
        self._issuer = None
        self._issuer_country = None
        self._organization_name = None
        self._serialnumber = None
        self._valid_from = None
        self._valid_to = None

    def resolve_certificate(self, domain_or_ip: str):
        # Load certificate
        certificate = self.get_certificate(domain_or_ip)
        x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, certificate)
        # General Assignment
        self._valid_from = x509.get_notBefore()
        self._valid_to = x509.get_notAfter()
        # Subject Assignment
        self._common_name = x509.get_subject().CN
        self._country = x509.get_subject().C
        self._organization_name = x509.get_subject().O
        self._serialnumber = x509.get_serial_number()
        # Issuer Assignment
        self._issuer = x509.get_issuer().CN
        self._issuer_country = x509.get_issuer().C

    def get_certificate(self, host, port=443, timeout=10):
        # Create empty context to ignore cert validation
        context = ssl.SSLContext()
        conn = socket.create_connection((host, port))
        sock = context.wrap_socket(conn, server_hostname=host)
        sock.settimeout(timeout)
        try:
            der_cert = sock.getpeercert(True)
        finally:
            sock.close()
        return ssl.DER_cert_to_PEM_cert(der_cert)
    
    def __str__(self):
        return f"CN {self._common_name}, C {self._country}, OU {self._organization_name}"
