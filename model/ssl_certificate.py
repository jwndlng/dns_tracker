
class SSLCertificate(object):

    def __init__(self):
        # Model variables
        self._type = None
        self._ca_cert = None
        self._root_cert = None
        self._valid_from = None
        self._valid_to = None

    def resolve_ssl_chain(self):
        pass
