from datetime import datetime, timedelta, timezone
from opentelemetry import trace
tracer = trace.get_tracer('MESSAGES API')

class Messages:
  def run(user_sender_handle, user_receiver_handle):
    with tracer.start_as_current_span('messages-mock-data'):

      model = {
        'errors': None,
        'data': None
      }

      now = datetime.now(timezone.utc).astimezone()

      results = [
        {
          'uuid': '4e81c06a-db0f-4281-b4cc-98208537772a' ,
          'display_name': 'Andrew Brown',
          'handle':  'andrewbrown',
          'message': 'Cloud is fun!',
          'created_at': now.isoformat()
        },
        {
          'uuid': '66e12864-8c26-4c3a-9658-95a10f8fea67',
          'display_name': 'Andrew Brown',
          'handle':  'andrewbrown',
          'message': 'This platform is great!',
          'created_at': now.isoformat()
      }]
      model['data'] = results
      return model