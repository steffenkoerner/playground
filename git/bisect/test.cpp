#include <gtest/gtest.h>
#include "bisect.h"

TEST(SkipTest, DoesSkip) {

  const int result = sum(3,4);
  EXPECT_EQ(result, 7);
}