import sys
from builder.cli import render

try:
    render()

except KeyboardInterrupt:
    print('\n\nScript aborted by user.\n')
    sys.exit(1)
