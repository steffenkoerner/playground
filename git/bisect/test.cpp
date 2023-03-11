#include <gtest/gtest.h>
#include "bisect.h"

TEST(sum, AdditionPositiveValues) {
  const int result = sum(3,4);
  EXPECT_EQ(result, 7);
}

TEST(sum, AdditionNegativeValues) {
  const int result = sum(-3,-6);
  EXPECT_EQ(result, -9);
}

TEST(sum, BugFinding) {
  const int result = sum(5,-6);
  EXPECT_EQ(result, -1);
}