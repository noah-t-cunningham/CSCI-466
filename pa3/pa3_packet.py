class Packet:

    def __init__(self, src_ip_address: str, dst_ip_address: str, src_tl_port: int, dst_tl_port: int, protocol: str):
        self.src_ip_address = src_ip_address
        self.dst_ip_address = dst_ip_address
        self.src_tl_port = src_tl_port
        self.dst_tl_port = dst_tl_port
        self.protocol = protocol

    def get_src_ip_address(self):
        return self.src_ip_address

    def get_dst_ip_address(self):
        return self.dst_ip_address

    def get_src_tl_port(self):
        return self.src_tl_port

    def get_dst_tl_port(self):
        return self.dst_tl_port

    def get_protocol(self):
        return self.protocol

    def set_src_ip_address(self, new_src_ip_address):
        self.src_ip_address = new_src_ip_address

    def set_dst_ip_address(self, new_dst_ip_address):
        self.dst_ip_address = new_dst_ip_address

    def set_src_tl_port(self, new_src_tl_port):
        self.src_tl_port = new_src_tl_port

    def set_dst_tl_port(self, new_dst_tl_port):
        self.dst_tl_port = new_dst_tl_port

    def set_protocol(self, new_protocol):
        self.protocol = new_protocol

