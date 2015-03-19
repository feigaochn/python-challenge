def solve_it():
    import xmlrpc.client

    phonebook = xmlrpc.client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
    print(phonebook.system.listMethods())
    print(phonebook.system.methodHelp('phone'))

    import urllib.request
    import urllib.parse

    url = 'http://www.pythonchallenge.com/pc/return/evil4.jpg'
    req = urllib.request.Request(url)
    try:
        urllib.request.urlopen(req)
    except Exception as e:
        print(e.headers)
        # WWW-Authenticate: Basic realm="inflate"
        # ...

    import base64

    unpw = '{}:{}'.format('huge', 'file')
    b64unpw = base64.encodebytes(unpw.encode()).decode().strip()

    req.add_header('Authorization', 'Basic {}'.format(b64unpw))
    print(req.headers)
    resp = urllib.request.urlopen(req)
    print(resp.read().decode())
    # Bert is evil! go back!

    print(phonebook.phone('Bert'))

    return 'italy'
