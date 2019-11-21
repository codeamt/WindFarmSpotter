import XCTest

import srcTests

var tests = [XCTestCaseEntry]()
tests += srcTests.allTests()
XCTMain(tests)
