python_library(
  name='app',
  dependencies=[
    '3rdparty/python:urllib3',
    'src/python/api'
  ]
)

python_binary(
  name='app-bin',
  source='app.py',
  dependencies=[
    'src/python/app',
    'src/python/api',
  ],
  compatibility='CPython>=3'
)
