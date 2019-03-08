python_tests(
  name = 'test_app',
  sources = globs("*.py"),
  dependencies = [
    '3rdparty/python:urllib3',
    'src/python/app/model',
    'src/python/app/view',
    'src/python/api',
    'test/python/app/model:test_model',
    'test/python/app/view:test_view'
  ],
)
