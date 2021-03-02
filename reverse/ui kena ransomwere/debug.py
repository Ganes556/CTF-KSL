import base64

base64_message = 'RHVkHmFsZR5gYG9XallRHktPSx5KQVpZRB5SXU5XWUogax11GWPcGmkR3CTQ0tw6dQbcCRkZDN55EQveEhkYFaBjcWxgWWieUmJnnlFsVZ5GSl1HTnFdnqOitauvrba5k5J7irlnaZ+JhZ9luWyXn4qVgJGsjHWdn669qrWqqLlfQF1ndTVfXCRsVyNkX19hAOg='
base64_bytes = base64_message.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
# message = message_bytes.decode('ascii')

print(base64.decodebytes(message_bytes))