# DNS-opslag bygget fra bunden (Modul 2, opgave 1)
import struct

# --- Konstanter ---
TRANSACTION_ID = 0x1234   # Valgfrit ID. Svaret skal have samme ID
FLAGS = 0x0100               # Recursion Desired = 1
QDCOUNT = 1                  # Antal spørgsmål
ANCOUNT = 0                  # Antal svar (0 i en forespørgsel)
NSCOUNT = 0                  # Authority-records
ARCOUNT = 0                  # Additional-records


def build_header():
    # 6 felter à 2 bytes (H), network byte order (!) = 12 bytes
    return struct.pack("!HHHHHH", TRANSACTION_ID, FLAGS, QDCOUNT, ANCOUNT, NSCOUNT, ARCOUNT)


# --- Test ---
header = build_header()
print(len(header), header.hex())