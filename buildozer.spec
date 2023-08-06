[app]
# (str) Title of your application
title = Your Kivy App

# (str) Package name
package.name = your.kivy.app

# (str) Package domain (reverse domain style, e.g. org.example.yourapp)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv

# (list) List of source files to exclude (let empty to not exclude anything)
source.exclude_exts = spec

# (list) List of directories to exclude (let empty to not exclude anything)
source.exclude_dirs = tests, bin

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command line output))
log_level = 2
