# Haveno Client

The Haveno Client is a Python gRPC client that allows you to interact with Haveno, a decentralized cryptocurrency trading platform. This client enables you to connect to Haveno servers, access market data, manage accounts, and perform trades programmatically.

## Features

- Connect to multiple Haveno servers using gRPC.
- Manage accounts, access market data, and make trades.
- Supports SOCKS5 proxy for secure and private connections.
- Modular design for different gRPC services (e.g., Accounts, Trades, Offers).

## Requirements

- Python 3.7+
- `grpcio` and `grpcio-tools`
- `pysocks` for SOCKS5 proxy support (optional)
- Haveno server running and accessible

## Installation

1. **Clone the repository**:

```bash
   git clone https://github.com/yourusername/python-haveno-client.git
   cd python-haveno-client
```

2. **Create a virtual environment** (optional but recommended):

```bash
   python3 -m venv venv
   source venv/bin/activate
```

3. **Install dependencies**:

```bash
   pip install -r requirements.txt
```

## Usage

### 1. Initialize the Haveno Client

Here is an example of how to initialize the client and connect to a Haveno server:

```python
   from haveno_client import HavenoClient

   # Create a Haveno client instance and connect to the server
   client = HavenoClient(host='localhost', port=3201, password='your_password', use_socks5=True, socks5_host='127.0.0.1', socks5_port=9050)

   # Perform operations using the client
   account_info = client.account_client.get_account_info('account_id')
   print(account_info)

   # Disconnect from the server
   client.disconnect()
```

### 2. Connect to Multiple Servers

You can create multiple instances of `HavenoClient` to connect to different Haveno servers:

```python
   client1 = HavenoClient(host='localhost', port=50051, password='password1')
   client2 = HavenoClient(host='localhost', port=50052, password='password2', use_socks5=True)

   # Perform operations with each client...
   client1.disconnect()
   client2.disconnect()
```

### 3. Using Modular Service Stubs

The client provides modular stubs for each gRPC service, such as `AccountClient`, `TradesClient`, and `OffersClient`. Each stub can be accessed via the `HavenoClient` instance:

```python
   # Example: Get account information
   account_info = client.account_client.get_account_info('account_id')
```

## Development

### Building the Package

To compile the package for distribution:

```bash
   python -m build
```

This will create the distribution files in the `dist/` directory.

### Running Tests

To run the test suite, use:

```bash
   python -m unittest discover tests/
```

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b my-feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin my-feature-branch`.
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments

- The Haveno development team for building the Haveno decentralized exchange.
- Contributors to the `grpcio` and `pysocks` libraries.
- **THIS PROJECT IS A WORK IN PROGRESS, ITS IS NOT YET SUITABLE FOR PRODUCTION ENVIRONMENTS**