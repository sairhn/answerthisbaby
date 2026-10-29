import base64
import time

def reveal_secret():
    # Scrambled data string
    secret_data = b'Y29uZ3JhdHVsYXRpb25zISB5b3UgZGVjb2RlZCBpdCEganVzdCB3YW50ZWQgdG8gc2F5IHRoYXQgSSBhbSBzbyBsdWNreSB0byBoYXZlIHlvdSBpbiBteSBsaWZlLiBZb3UncmUgbXkgZmF2b3VyaXRlIHBlcnNvbiEgY3VkZGxlcyBsYXRlcj8gbyg9Xl9eKTo='
    
    print("⏳ Decrypting love_letter_payload.bin...")
    time.sleep(1.5)
    
    # Decoding process
    decoded_message = base64.b64decode(secret_data).decode('utf-8')
    
    print("\n🔒 [DECRYPTION COMPLETE] \n")
    print(f"💌 Message: {decoded_message}\n")

if __name__ == '__main__':
    reveal_secret()
