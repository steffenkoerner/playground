proto_library(
   name = "thing_proto",
   srcs = ["thing.proto"],
   deps = ["@com_google_protobuf//:any_proto"],
)

load("@rules_proto_grpc//cpp:defs.bzl", "cpp_proto_compile")

cpp_proto_compile(
    name = "cpp_thing_proto",
    protos = [":thing_proto"],
)