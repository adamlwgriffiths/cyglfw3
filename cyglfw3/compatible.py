from __future__ import absolute_import

import cyglfw3

# add glfw to functions and GLFW_ to constants
for name in dir(cyglfw3):
    # ignore normal module values
    if name.startswith('_'):
        continue

    attr = getattr(cyglfw3, name)
    if isinstance(attr, (int, float,)):
        # add GLFW_ prefix for constants
        globals()['GLFW_{}'.format(name)] = attr
    else:
        # add glfw prefix for functions
        globals()['glfw{}'.format(name)] = attr
