ENDPOINT_IN_DEVELOPING = 'This endpoint realisation is not ready yet. But you can see its interface and errors'


def temporary_description(role: str) -> str:
    extra_message = f'<h1>Role: {role}</h1>' if role != '' else ''
    return f'<h2>{ENDPOINT_IN_DEVELOPING}<h2><br>' \
           f'{extra_message}'
