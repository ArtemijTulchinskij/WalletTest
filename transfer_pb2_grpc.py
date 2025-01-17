# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import common_pb2 as common__pb2
import transfer_pb2 as transfer__pb2

GRPC_GENERATED_VERSION = '1.68.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in transfer_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class TransferServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTransfers = channel.unary_unary(
                '/transfer.TransferService/GetTransfers',
                request_serializer=transfer__pb2.GetTransfersRequest.SerializeToString,
                response_deserializer=transfer__pb2.GetTransfersReply.FromString,
                _registered_method=True)
        self.GetTransfersStream = channel.unary_stream(
                '/transfer.TransferService/GetTransfersStream',
                request_serializer=transfer__pb2.GetTransfersRequest.SerializeToString,
                response_deserializer=transfer__pb2.GetTransfersReply.FromString,
                _registered_method=True)
        self.ExportTransfers = channel.unary_unary(
                '/transfer.TransferService/ExportTransfers',
                request_serializer=transfer__pb2.ExportTransfersRequest.SerializeToString,
                response_deserializer=transfer__pb2.ExportTransfersReply.FromString,
                _registered_method=True)
        self.HideTransfers = channel.unary_unary(
                '/transfer.TransferService/HideTransfers',
                request_serializer=transfer__pb2.HideTransfersRequest.SerializeToString,
                response_deserializer=common__pb2.EmptyReply.FromString,
                _registered_method=True)
        self.Transfer = channel.unary_unary(
                '/transfer.TransferService/Transfer',
                request_serializer=transfer__pb2.TransferRequest.SerializeToString,
                response_deserializer=transfer__pb2.TransferReply.FromString,
                _registered_method=True)


class TransferServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetTransfers(self, request, context):
        """Получить историю вводов, выводов, переводов пользователя
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTransfersStream(self, request, context):
        """Подписка на обновление истории транзакций пользователя
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExportTransfers(self, request, context):
        """Экспорт истории транзакций пользователя
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HideTransfers(self, request, context):
        """Скрытие транзакции пользователя
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Transfer(self, request, context):
        """Запрос на перевод средств
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TransferServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTransfers': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTransfers,
                    request_deserializer=transfer__pb2.GetTransfersRequest.FromString,
                    response_serializer=transfer__pb2.GetTransfersReply.SerializeToString,
            ),
            'GetTransfersStream': grpc.unary_stream_rpc_method_handler(
                    servicer.GetTransfersStream,
                    request_deserializer=transfer__pb2.GetTransfersRequest.FromString,
                    response_serializer=transfer__pb2.GetTransfersReply.SerializeToString,
            ),
            'ExportTransfers': grpc.unary_unary_rpc_method_handler(
                    servicer.ExportTransfers,
                    request_deserializer=transfer__pb2.ExportTransfersRequest.FromString,
                    response_serializer=transfer__pb2.ExportTransfersReply.SerializeToString,
            ),
            'HideTransfers': grpc.unary_unary_rpc_method_handler(
                    servicer.HideTransfers,
                    request_deserializer=transfer__pb2.HideTransfersRequest.FromString,
                    response_serializer=common__pb2.EmptyReply.SerializeToString,
            ),
            'Transfer': grpc.unary_unary_rpc_method_handler(
                    servicer.Transfer,
                    request_deserializer=transfer__pb2.TransferRequest.FromString,
                    response_serializer=transfer__pb2.TransferReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'transfer.TransferService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('transfer.TransferService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class TransferService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetTransfers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/transfer.TransferService/GetTransfers',
            transfer__pb2.GetTransfersRequest.SerializeToString,
            transfer__pb2.GetTransfersReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetTransfersStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/transfer.TransferService/GetTransfersStream',
            transfer__pb2.GetTransfersRequest.SerializeToString,
            transfer__pb2.GetTransfersReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ExportTransfers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/transfer.TransferService/ExportTransfers',
            transfer__pb2.ExportTransfersRequest.SerializeToString,
            transfer__pb2.ExportTransfersReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def HideTransfers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/transfer.TransferService/HideTransfers',
            transfer__pb2.HideTransfersRequest.SerializeToString,
            common__pb2.EmptyReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Transfer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/transfer.TransferService/Transfer',
            transfer__pb2.TransferRequest.SerializeToString,
            transfer__pb2.TransferReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
