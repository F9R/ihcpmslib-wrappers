from enum import IntFlag

class NetworkInterfaceTypesWrapper(IntFlag):
    WiredEthernet = 1
    WiFi = 2
    Vpn = 4
    VirtualEthernet = 8