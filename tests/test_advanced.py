# -*- coding: utf-8 -*-

from .context import sblibs

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(sblibs.main())


if __name__ == '__main__':
    unittest.main()
