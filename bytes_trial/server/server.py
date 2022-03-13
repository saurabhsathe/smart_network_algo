import grpc
from concurrent import futures
import time

import file_transfer_pb2_grpc
import file_transfer_pb2

import file_transfer

class CalculatorService(file_transfer_pb2_grpc.CalculatorServicer):
    def file_transfer(self, request, context):
        response=file_transfer_pb2.Response()

        if file_transfer.file_transfer(request.content):
            response.error=False
            return response
        else:
            response.error=True
            return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    file_transfer_pb2_grpc.add_CalculatorServicer_to_server(CalculatorService(),server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


serve()
