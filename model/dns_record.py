
import dns.resolver


SUPPORTED_RECORDS = ['A', 'MX', 'NS', 'CERT', 'TXT']


class DNSRecord(object):

    def __init__(self):
        # Model variables
        self._a = None
        self._mx = None
        self._ns = None
        self._cert = None
        self._txt = None
        self._registered_at = None

    def resolve_domain(self, target: str):
        for record in SUPPORTED_RECORDS:
            try:
                answer = dns.resolver.resolve(target, record)
                setattr(self, f"_{record.lower()}", [str(val) for val in answer])
            except Exception as Ex:
                print(f"Target {target}")
                print(Ex)

    def __str__(self):
        return f"DNSRecord for IP {self._a}"
