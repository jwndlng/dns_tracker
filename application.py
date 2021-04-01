

__title__ = 'DNS Explorer/Tracker'
__version__ = '1.0.0'
__author__ = "Jan Wendling <jan.wendling@gmail.com>"
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2021 - Jan Wendling'


import dns.reversename, dns.resolver
import model.host


def run_application(target: str):
    '''
    IP or Domain to start
    '''

    root = model.host.Host(ip=target)
    # root.lookup_dns()

    # print(root._dns_record._a)
    # print(root._dns_record._mx)
    # print(root._dns_record._ns)

    root.lookup_certificate()

    print(root._ssl_cert)

def ppline(msg):
    '''
    Print pointed line
    '''
    line_length = 80
    print("".join(["." for i in range(0, line_length-len(msg))]), end="")
    print(msg)


def main():
    ppline("Starting application")
    run_application('demo')
    ppline("End")


if "__main__" == __name__:
    main()
