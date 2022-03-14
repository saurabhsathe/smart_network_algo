# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import file_transfer_pb2 as file__transfer__pb2


class FileTransferStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.file_transfer = channel.unary_unary(
                '/FileTransfer/file_transfer',
                request_serializer=file__transfer__pb2.Request.SerializeToString,
                response_deserializer=file__transfer__pb2.Response.FromString,
                )
        self.ServerResponse = channel.unary_unary(
                '/FileTransfer/ServerResponse',
                request_serializer=file__transfer__pb2.ServerSpeedRequest.SerializeToString,
                response_deserializer=file__transfer__pb2.ServerSpeedResponse.FromString,
                )


class FileTransferServicer(object):
    """Missing associated documentation comment in .proto file."""

    def file_transfer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ServerResponse(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FileTransferServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'file_transfer': grpc.unary_unary_rpc_method_handler(
                    servicer.file_transfer,
                    request_deserializer=file__transfer__pb2.Request.FromString,
                    response_serializer=file__transfer__pb2.Response.SerializeToString,
            ),
            'ServerResponse': grpc.unary_unary_rpc_method_handler(
                    servicer.ServerResponse,
                    request_deserializer=file__transfer__pb2.ServerSpeedRequest.FromString,
                    response_serializer=file__transfer__pb2.ServerSpeedResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'FileTransfer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FileTransfer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def file_transfer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FileTransfer/file_transfer',
            file__transfer__pb2.Request.SerializeToString,
            file__transfer__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ServerResponse(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FileTransfer/ServerResponse',
            file__transfer__pb2.ServerSpeedRequest.SerializeToString,
            file__transfer__pb2.ServerSpeedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)