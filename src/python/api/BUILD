python_library(
  name='api',
  sources = globs("*.py"),
  dependencies=[
    '3rdparty/python:urllib3'
  ]
)

python_binary(
  name='api-bin',
  source='router.py',
  dependencies=[
    '3rdparty/python_urllib3'
  ],
  compatibility='CPython>=3.6'
)
