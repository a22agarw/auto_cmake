import os
import json
import unittest

from auto_cmake.auto_cmake import AutoCMake
from auto_cmake.auto_cmake_lib_shared_win import AutoCMakeLibSharedWin

# Source paths
proj_dir = os.path.abspath(os.path.join(os.getcwd(), "resources", "sample_c_proj"))
build_dir = os.path.abspath(os.path.join(proj_dir, "build"))

# Configuration
cmake_config = dict()
cmake_config['proj_name'] = 'sample_c_proj'
cmake_config['proj_dir'] = proj_dir
cmake_config['version'] = "2024.03.08"
cmake_config['cmake_version'] = '3.15'
cmake_config['include_dirs'] = [proj_dir]
cmake_config['libs'] = []
cmake_config['flags'] = []
cmake_config['exclude_dirs'] = []
cmake_config['exclude_paths'] = []
cmake_config['build_dir'] = build_dir

# WIN Configuration
cmake_config['jni_dir'] = "C:/Program Files/Java/jdk1.8.0_202"

class TestAutoCMakeLibSharedWin(unittest.TestCase):

    def test_build_lib_shared_win(self):
        ac = AutoCMakeLibSharedWin(**cmake_config)
        ac.run()

if __name__ == '__main__':
    unittest.main()
