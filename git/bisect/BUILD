cc_library(
    name = "bisect",
    hdrs = ["bisect.h"],
)

cc_test(
  name = "bisect_test",
  srcs = ["test.cpp"],
  deps = ["@gtest//:gtest",
        "@gtest//:gtest_main",
        ":bisect",
        ],
)