# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import database_pb2 as database__pb2


class DatabaseServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateRecord = channel.unary_unary(
                '/DatabaseService/CreateRecord',
                request_serializer=database__pb2.CreateRecordRequest.SerializeToString,
                response_deserializer=database__pb2.CreateRecordResponse.FromString,
                )
        self.ReadRecord = channel.unary_unary(
                '/DatabaseService/ReadRecord',
                request_serializer=database__pb2.ReadRecordRequest.SerializeToString,
                response_deserializer=database__pb2.ReadRecordResponse.FromString,
                )
        self.UpdateRecord = channel.unary_unary(
                '/DatabaseService/UpdateRecord',
                request_serializer=database__pb2.UpdateRecordRequest.SerializeToString,
                response_deserializer=database__pb2.UpdateRecordResponse.FromString,
                )
        self.DeleteRecord = channel.unary_unary(
                '/DatabaseService/DeleteRecord',
                request_serializer=database__pb2.DeleteRecordRequest.SerializeToString,
                response_deserializer=database__pb2.DeleteRecordResponse.FromString,
                )


class DatabaseServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateRecord(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadRecord(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateRecord(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteRecord(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DatabaseServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateRecord': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateRecord,
                    request_deserializer=database__pb2.CreateRecordRequest.FromString,
                    response_serializer=database__pb2.CreateRecordResponse.SerializeToString,
            ),
            'ReadRecord': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadRecord,
                    request_deserializer=database__pb2.ReadRecordRequest.FromString,
                    response_serializer=database__pb2.ReadRecordResponse.SerializeToString,
            ),
            'UpdateRecord': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateRecord,
                    request_deserializer=database__pb2.UpdateRecordRequest.FromString,
                    response_serializer=database__pb2.UpdateRecordResponse.SerializeToString,
            ),
            'DeleteRecord': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteRecord,
                    request_deserializer=database__pb2.DeleteRecordRequest.FromString,
                    response_serializer=database__pb2.DeleteRecordResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DatabaseService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DatabaseService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateRecord(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DatabaseService/CreateRecord',
            database__pb2.CreateRecordRequest.SerializeToString,
            database__pb2.CreateRecordResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadRecord(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DatabaseService/ReadRecord',
            database__pb2.ReadRecordRequest.SerializeToString,
            database__pb2.ReadRecordResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateRecord(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DatabaseService/UpdateRecord',
            database__pb2.UpdateRecordRequest.SerializeToString,
            database__pb2.UpdateRecordResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteRecord(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DatabaseService/DeleteRecord',
            database__pb2.DeleteRecordRequest.SerializeToString,
            database__pb2.DeleteRecordResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
