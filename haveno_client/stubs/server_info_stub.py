import grpc
import warnings

import grpc_pb2 as grpc__pb2

GRPC_GENERATED_VERSION = '1.66.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

class ServerInfoStub(object):
    """/////////////////////////////////////////////////////////////////////////////////////////
    Help
    /////////////////////////////////////////////////////////////////////////////////////////

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetMethodHelp = channel.unary_unary(
                '/io.haveno.protobuffer.Help/GetMethodHelp',
                request_serializer=grpc__pb2.GetMethodHelpRequest.SerializeToString,
                response_deserializer=grpc__pb2.GetMethodHelpReply.FromString,
                _registered_method=True)

