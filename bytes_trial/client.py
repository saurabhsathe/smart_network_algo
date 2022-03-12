import grpc
import file_transfer_pb2
import file_transfer_pb2_grpc

def client(stub):
    with open("bytes_transfer_main.txt", mode='rb') as file: # b is important -> binary
        chunk_size=100
        def get_data(file):
            while True:
                data = file.read(chunk_size)
                if not data:
                    break
                yield data
        count=1
        for piece in get_data(file):
            print(piece)
            req=file_transfer_pb2.Request()
            req.chukid=count
            req.content=piece
            resp=stub.file_transfer(req)
            count+=1
            print(resp)
    return True
if __name__=="__main__":
    channel=grpc.insecure_channel('localhost:50051')
    stub=file_transfer_pb2_grpc.CalculatorStub(channel)
    response=client(stub)
    print(response)