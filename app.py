"""
Main application file
"""

import os

for i in range(10000):
    print('second pt6', i)
    print('What is the variables:', os.environ['ENVIRONMENT'])
    print('nothing else huh', os.environ.get('ANOTHER_VARIABLE'))