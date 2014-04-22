#!/usr/bin/env python
"""
Create a simple python script with a shebang line that points to python_shebang
and execute it via os.system.  If things work properly we will see the output
of the script.
"""

#Copyright (c) 2014 Yahoo! Inc. All rights reserved.
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License. See accompanying LICENSE file.

__author__ = 'dhubbard'

import unittest
import tempfile
import os


test_script = """#!/usr/bin/env {}
import sys
print('Python ok')
print(sys.version)
"""


class UnitTest(unittest.TestCase):
    script_file = None

    def setUp(self):
        # Create a tempfile with a script that uses our shebang handler
        python_shebang_location = os.path.abspath(
            os.path.join(os.getcwd(), '../python_shebang/bin/python_shebang')
        )
        if os.path.exists(
                os.path.join(os.getcwd(), 'python_shebang/bin/python_shebang')
        ):
            python_shebang_location = os.path.join(
                os.getcwd(),
                'python_shebang/bin/python_shebang'
            )
        self.script_file = tempfile.NamedTemporaryFile(mode='w+b')
        os.fchmod(self.script_file.fileno(), 0o700)
        full_script = test_script.format(
            python_shebang_location).encode('utf-8')
        self.script_file.write(full_script)
        self.script_file.flush()

    def test_run_from_shell(self):
        result = os.popen(self.script_file.name, 'r').read()
        self.assertIn('Python ok', result)


if __name__ == "__main__":
    unittest.main()