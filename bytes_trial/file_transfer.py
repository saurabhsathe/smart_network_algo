

def file_transfer(bytes):
    try:
        f = open("sample.txt", "wb")
        f.write(bytes)
        f.close()
        return True
    except Exception as e:
        return False