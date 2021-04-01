
from .dns_record import DNSRecord
from .ssl_certificate import SSLCertificate

class Host(object):

    def __init__(self, domain=None, ip=None):
        # Model variables
        self._domain = domain
        self._dns_record = None
        self._ip_address = ip
        self._ssl_cert = None
        self._subdomains = None
        self._registered_at = None # IP

    def lookup_dns(self):
        dns = DNSRecord()
        dns.resolve_domain(self._domain)
        self._dns_record = dns

    def lookup_certificate(self):
        cert = SSLCertificate()
        target = self._domain if self._domain else self._ip_address
        cert.resolve_certificate(target)
        self._ssl_cert = cert

    def lookup_ip(self):
        pass
