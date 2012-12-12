#coding: utf-8

import os
import logging

#: base settings
project_codename = 'manplanet'

#: path settings
data_path = os.path.abspath('..')
base_path = os.path.join(data_path, 'manpage')
project_path = os.path.abspath('.')
project_db_path = os.path.join(project_path, 'data',
                               '%s.sqlite' % (project_codename))

#: db settings
database_url = 'sqlite:///%s' % (project_db_path)

#: logging settings
log_level = logging.DEBUG
log_path = os.path.join(project_path, '%s.log' % (project_codename))
log_format = '%(levelname)s - %(message)s'

#: PageRank settings
pr_iterate_times = 100

#: server settings
DEBUG = True
