#!/home/reana/reana-venv/bin/python2
# -*- coding: utf-8 -*-
import re
import sys
from reana_cluster.cli import cli
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(cli())
