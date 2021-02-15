
from .dns_record import DNSRecord

class Host(object):

    def __init__(self, domain=None, ip=None):
        # Model variables
        self._domain = domain
        self._dns_record = None
        self._ip_address = ip
        self._ssl_cert = None
        self._subdomains = None
        self._registered_at = None # IP

    def crawl_dns(self):
        dns = DNSRecord()
        dns.resolve_domain(self._domain)
        self._dns_record = dns

    def crawl_ip(self):
        pass
