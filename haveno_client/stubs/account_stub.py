import grpc
from haveno_client import grpc_pb2 # Import the necessary message classes
from ..grpc_pb2_grpc import AccountStub, Account
from haveno_client import grpc_pb2_grpc # Import the gRPC stub

class AccountClient:
    def __init__(self, channel):
        self.stub = AccountStub(channel)

    def account_exists(self) -> bool:
        try:
            response = self.stub.AccountExists()
            return response
        except grpc.RpcError as e:
            print(f"gRPC error: {e}")
            return None
        
