#include <gtest/gtest.h>
#include "application.h"

TEST(sum, AdditionPositiveValues) {
  const int result = sum(3,4);
  EXPECT_EQ(result, 7);
}

TEST(sum, AdditionNegativeValues) {
  const int result = sum(-3,-6);
  EXPECT_EQ(result, -9);
}

// You found out that there is a problem with the application and thus you added this
// Test that shows the bug.
TEST(sum, BugFinding) {
  const int result = sum(5,-6);
  EXPECT_EQ(result, -1);
}