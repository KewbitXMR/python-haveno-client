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
OUT_DIR="./haveno_client"

# Generate Python code from grpc.proto
python3 -m grpc_tools.protoc -I$PROTO_DIR --python_out=$OUT_DIR --grpc_python_out=$OUT_DIR $PROTO_DIR/grpc.proto

# Generate Python code from pb.proto
python3 -m grpc_tools.protoc -I$PROTO_DIR --python_out=$OUT_DIR --grpc_python_out=$OUT_DIR $PROTO_DIR/pb.proto

echo "gRPC code generation completed."