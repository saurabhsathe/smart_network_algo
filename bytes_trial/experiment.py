

import file_transfer
def client():
    with open("subject102.dat", mode='rb') as file: # b is important -> binary
        chunk_size=100
        def get_data(file):
            while True:
                data = file.read(chunk_size)
                if not data:
                    break
                yield data
        count=1
        for piece in get_data(file):
            #print(piece,count)
            file_transfer.file_transfer(piece)
            count+=1

if __name__=="__main__":
    client()