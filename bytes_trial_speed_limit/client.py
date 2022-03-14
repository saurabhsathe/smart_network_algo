import grpc
import file_transfer_pb2
import file_transfer_pb2_grpc
import time
import get_optimal_chunksize
def client(stub,chunksize):
    with open("subject102.dat", mode='rb') as file:
        chunk_size=1000000 if chunksize==None else chunksize
        def get_data(file):
            while True:
                data = file.read(chunk_size)
                if not data:
                    break
                yield data
        count=1
        for piece in get_data(file):
            #print(piece)
            req=file_transfer_pb2.Request()
            req.chukid=count
            req.content=piece
            resp=stub.file_transfer(req)
            count+=1
            #print(resp)
    return True
if __name__=="__main__":

    channel=grpc.insecure_channel('localhost:50051')
    stub=file_transfer_pb2_grpc.FileTransferStub(channel)
    chunksize=get_optimal_chunksize.get_optimal_chunk(stub)
    t1=time.time()
    response=client(stub,chunksize)
    t2=time.time()
    print("File transfer completed at ",(t2-t1))

#49845.58081626892 for 1500
#3057.1300983428955