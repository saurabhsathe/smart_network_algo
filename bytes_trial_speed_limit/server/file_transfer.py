

def file_transfer(bytes):
    encoding="utf-8"
    try:
        #print("in the server",bytes)
        f = open("sample.dat", "a")
        bytes_decoded=bytes.decode(encoding)
        f.write(bytes_decoded)
        f.close()
        return True
    except Exception as e:
        print(e)
        return False