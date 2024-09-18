import grpc
import socks
from . import grpc_pb2, grpc_pb2_grpc
from .stubs import AccountClient, TradesClient, OffersClient  # Import your modular stubs

class HavenoClient:
    def __init__(self, host, port, password, use_socks5=False, socks5_host='127.0.0.1', socks5_port=9050):
        self._host = host
        self._port = port
        self._password = password
        self.channel = None
        self.account_client = None
        self.trades_client = None
        self.offers_client = None
        self.disputes_client = None
        self.dispute_agents_client = None
        self.version_client = None
        self.help_client = None
        self.trade_statistics_client = None
        self.xmr_node_client = None
        self.xmr_connections_client = None
        self.notifications_client = None
        self.price_client = None
        self.wallet_client = None

        # Connect to the server using either a direct or SOCKS5 channel
        if use_socks5:
            print(f"Connecting to {host}:{port} through SOCKS5 proxy at {socks5_host}:{socks5_port}")
            self.channel = self._create_socks5_channel(host, port, socks5_host, socks5_port)
        else:
            print(f"Connecting to {host}:{port} directly")
            self.channel = grpc.insecure_channel(f'{host}:{port}')

        # Initialize gRPC clients (stubs)
        self._initialize_clients()

        # Check initial connection
        self._check_connection()

    def _create_socks5_channel(self, host, port, proxy_host, proxy_port):
        def socks5_socket_factory(address, timeout=None):
            sock = socks.socksocket()
            sock.set_proxy(socks.SOCKS5, proxy_host, proxy_port)
            sock.settimeout(timeout)
            sock.connect(address)
            return sock

        channel_options = [
            ('grpc.default_authority', f'{host}:{port}')
        ]
        return grpc.insecure_channel(f'{host}:{port}', options=channel_options, sock_factory=socks5_socket_factory)

    def _initialize_clients(self):
        call_options = grpc.CallOptions(metadata=(('password', self._password),))
        self.account_client = grpc_pb2_grpc.AccountStub(self.channel, call_options)
        self.trades_client = grpc_pb2_grpc.TradesStub(self.channel, call_options)
        self.offers_client = grpc_pb2_grpc.OffersStub(self.channel, call_options)
        self.disputes_client = grpc_pb2_grpc.DisputesStub(self.channel, call_options)
        self.dispute_agents_client = grpc_pb2_grpc.DisputeAgentsStub(self.channel, call_options)
        self.version_client = grpc_pb2_grpc.GetVersionStub(self.channel, call_options)
        self.help_client = grpc_pb2_grpc.HelpStub(self.channel, call_options)
        self.trade_statistics_client = grpc_pb2_grpc.GetTradeStatisticsStub(self.channel, call_options)
        self.xmr_node_client = grpc_pb2_grpc.XmrNodeStub(self.channel, call_options)
        self.xmr_connections_client = grpc_pb2_grpc.XmrConnectionsStub(self.channel, call_options)
        self.notifications_client = grpc_pb2_grpc.NotificationsStub(self.channel, call_options)
        self.price_client = grpc_pb2_grpc.PriceStub(self.channel, call_options)
        self.wallets_client = grpc_pb2_grpc.WalletsStub(self.channel, call_options)         
        print("Initialized gRPC clients.")

    def _check_connection(self):
        try:
            response = self.version_client.GetVersion # Replace with an appropriate call
            print(f"Successfully connected to the daemon: {response}")
        except grpc.RpcError as e:
            print(f"Failed to connect: {e}")
            self.disconnect()

    def disconnect(self):
        if self.channel:
            self.channel.close()
            self.channel = None
            self._reset_clients()
            print("Disconnected from the gRPC server.")

    def _reset_clients(self):
        self.account_client = None
        self.trades_client = None
        self.offers_client = None
        self.disputes_client = None
        self.dispute_agents_client = None
        self.version_client = None
        self.help_client = None
        self.trade_statistics_client = None
        self.xmr_node_client = None
        self.xmr_connections_client = None
        self.notifications_client = None
        self.price_client = None
        self.wallet_client = None