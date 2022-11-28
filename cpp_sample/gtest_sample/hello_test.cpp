#include <gtest/gtest.h>

#include "hello.h"

TEST(HelloTest, BasicAssertions) {
    EXPECT_EQ("hello", greeting());
}
