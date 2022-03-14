import grpc
from concurrent import futures
import time

import file_transfer_pb2_grpc
import file_transfer_pb2

import file_transfer

class FileTransferService(file_transfer_pb2_grpc.FileTransferServicer):
    def __init__(self,server_configs=4000000):
        self.server_configs=server_configs

    def file_transfer(self, request, context):
        response=file_transfer_pb2.Response()

        if file_transfer.file_transfer(request.content):
            response.error=False
            return response
        else:
            response.error=True
            return response

    def ServerResponse(self, request, context):
        response=file_transfer_pb2.ServerSpeedResponse()
        response.server_mtu=self.server_configs
        return response



def serve(mx_srv_len=4000000):
    max_server_message_length=mx_srv_len
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10),options=[('grpc. max_receive_message_length', max_server_message_length),('grpc. max_send_message_length', max_server_message_length)])
    #print(dir(grpc.server.__defaults__))
    #print(grpc.server.__defaults__)
    file_transfer_pb2_grpc.add_FileTransferServicer_to_server(FileTransferService(),server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


serve()
"""
['AuthMetadataContext', 'AuthMetadataPlugin', 'AuthMetadataPluginCallback', 'Call', 'CallCredentials', 'Channel', 'ChannelConnectivity', 'ChannelCredentials', 'ClientCallDetails', 'Compression', 'Future', 'FutureCancelledError', 'FutureTimeoutError', 'GenericRpcHandler', 'HandlerCallDetails', 'LocalConnectionType', 'RpcContext', 'RpcError', 'RpcMethodHandler', 'Server', 'ServerCertificateConfiguration', 'ServerCredentials', 'ServerInterceptor', 'ServiceRpcHandler', 'ServicerContext', 'Status', 'StatusCode', 'StreamStreamClientInterceptor', 'StreamStreamMultiCallable', 'StreamUnaryClientInterceptor', 'StreamUnaryMultiCallable', 'UnaryStreamClientInterceptor', 'UnaryStreamMultiCallable', 'UnaryUnaryClientInterceptor', 'UnaryUnaryMultiCallable', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_common', '_compression', '_create_servicer_context', '_cygrpc', '_cython', '_grpcio_metadata', '_interceptor', '_runtime_protos', '_server', 'abc', 'access_token_call_credentials', 'aio', 'alts_channel_credentials', 'alts_server_credentials', 'channel_ready_future', 'composite_call_credentials', 'composite_channel_credentials', 'compute_engine_channel_credentials', 'contextlib', 'dynamic_ssl_server_credentials', 'enum', 'grpc_tools', 'insecure_channel', 'insecure_server_credentials', 'intercept_channel', 'local_channel_credentials', 'local_server_credentials', 'logging', 'metadata_call_credentials', 'method_handlers_generic_handler', 'protos', 'protos_and_services', 'secure_channel', 'server', 'services', 'six', 'ssl_channel_credentials', 'ssl_server_certificate_configuration', 'ssl_server_credentials', 'stream_stream_rpc_method_handler', 'stream_unary_rpc_method_handler', 'sys', 'unary_stream_rpc_method_handler', 'unary_unary_rpc_method_handler', 'xds_channel_credentials', 'xds_server_credentials']
"""