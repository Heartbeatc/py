import sys

import os

print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core  import src

if __name__ == '__main__':
    src.run()