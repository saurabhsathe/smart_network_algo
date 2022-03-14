import grpc
import file_transfer_pb2
import file_transfer_pb2_grpc
import time
import psutil
def client(stub):
    with open("subject102.dat", mode='rb') as file:
        try:
            chunk_size=1000000
            curr=float("-inf")
            optimal_chunk_size=-1
            while True:
                data = file.read(chunk_size)
                req=file_transfer_pb2.Request()
                req.chukid=1
                req.content=data
                t1=time.time()
                resp=stub.file_transfer(req)
                t2=time.time()
                latency=(t2-t1)*1000000

                throughput=(chunk_size)/latency
                print("throughput observed is",throughput,chunk_size)
                if throughput>=curr:
                    curr=throughput
                    optimal_chunk_size=chunk_size
                elif throughput<curr:
                    break
                chunk_size+=8000
            print("optimal_chunk_size",optimal_chunk_size)
        except Exception as e:
            print("fails dude",e)

    return True
if __name__=="__main__":
    channel=grpc.insecure_channel('localhost:50051')
    stub=file_transfer_pb2_grpc.CalculatorStub(channel)
    response=client(stub)
    t1=time.time()
    print(psutil.net_if_stats()['Wi-Fi'].mtu)
    #print(psutil.net_if_stats().keys())
    print(response)