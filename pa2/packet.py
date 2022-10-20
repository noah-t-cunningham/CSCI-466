class Packet:

    def __init__(self, sequence_number: int, checksum: int, ack_or_nak: int, length: int, message: str, last_packet: int):
        self.sequence_number = sequence_number
        self.checksum = checksum
        self.ack_or_nak = ack_or_nak
        self.length = length
        self.message = message
        self.last_packet = last_packet

    def get_message(self):
        return self.message

    def get_sequence(self):
        return self.sequence_number

    def get_last_packet(self):
        return self.last_packet

    def get_corruption(self):
        return self.checksum

    def get_ack_nak(self):
        return self.ack_or_nak

    def set_corruption(self, new_checksum):
        self.checksum = new_checksum

