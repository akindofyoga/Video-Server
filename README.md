Server for [this](https://github.com/rogerthat94/VideoClient) client.

The Protobuf code was compiled with the lines
`/path/to/protoc --python_out=. update.proto` and
`/path/to/protoc --java_out=. update.proto`. Note that Scarlet does not use
protobuf lite. I used version 3.0 of the protobuf compiler. You can find
instructions to download a binary of this version
[here](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md#manual-protobuf-compiler-installation-and-usage).
The compiler takes a while to build, so I do not recommend compiling it
yourself.