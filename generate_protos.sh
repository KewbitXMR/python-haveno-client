# This Python haveno client extends the features of Haveno, supporting mobile devices and more.
# Copyright (C) 2024 KewbitXMR (https://kewbit.org)
#
# Contact Email: kewbitxmr@protonmail.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#!/bin/bash

# Directory paths
PROTO_DIR="./protos"
OUT_DIR="./haveno_client/proto2"

# Generate Python code from both grpc.proto and pb.proto in one command
python3 -m grpc_tools.protoc \
    -I$PROTO_DIR \
    --python_out=$OUT_DIR \
    --grpc_python_out=$OUT_DIR \
    $PROTO_DIR/grpc.proto $PROTO_DIR/pb.proto

echo "gRPC and Protobuf code generation completed."