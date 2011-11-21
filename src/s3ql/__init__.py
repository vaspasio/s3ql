'''
__init__.py - this file is part of S3QL (http://s3ql.googlecode.com)

Copyright (C) 2008-2009 Nikolaus Rath <Nikolaus@rath.org>

This program can be distributed under the terms of the GNU GPLv3.
'''

from __future__ import division, print_function

__all__ = [ 'backends', 'cli', 'parse_args', 'block_cache', "common", 'daemonize', 
            'database', 'fs', 'fsck', 'ordered_dict',  'deltadump',
            'VERSION', 'CURRENT_FS_REV' ]

VERSION = '1.5'
CURRENT_FS_REV = 14

# Maps file system revisions to the last S3QL version that
# supported this revision.
REV_VER_MAP = { 13: '1.6',
                12: '1.3',
                11: '1.0.1' }
