python_library(
  name='app',
  sources = globs("*.py"),
  dependencies=[
    '3rdparty/python:urllib3',
  ],
)

python_binary(
  name='app-bin',
  source='app.py',
  dependencies=[
    'src/python/app/model:model',
    'src/python/app/view:view',
  ],
  compatibility='CPython>=3.6'
)
