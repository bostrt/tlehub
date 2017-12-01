from flask import Flask, render_template
from tinydb import TinyDB, Query
import os
import re

# DB formt: {'header': stuff, 'line1': stuff, 'line2': stuff, 'satnum': stuff}
DB_FILE = os.getenv('DB_FILE', 'tlehub.json') 

# Setup globals
app = Flask(__name__)
db = TinyDB(DB_FILE)

@app.route('/')
def index():
    scheme = os.getenv('SCHEME', 'http')
    hostname = os.getenv('HOST', 'localhost')
    return '''Usage:

$ curl %s://%s/search/SO-50
SAUDISAT 1C (SO-50)
1 27607U 02058C   17334.47967434  .00000085  00000-0  32838-4 0  9990
2 27607  64.5556 337.3751 0040801  21.1335 339.1441 14.75396663803514    
    
$ curl %s://%s/27607
SAUDISAT 1C (SO-50)
1 27607U 02058C   17334.47967434  .00000085  00000-0  32838-4 0  9990
2 27607  64.5556 337.3751 0040801  21.1335 339.1441 14.75396663803514    
''' % (scheme, hostname, scheme, hostname), {'Content-Type': 'text/plain'}

@app.route('/search/<term>')
def search(term):
    TLE = Query()
    results = db.search(TLE.header.matches(re.compile('.*' + re.escape(term) + '.*', re.IGNORECASE)))
    view = ''
    if len(results) > 0:
        for result in results:
            view = view + result['header'] + '\n'
            view = view + result['line1'] + '\n'
            view = view + result['line2'] + '\n'
    return view, {'Content-Type': 'text/plain'}

@app.route('/<int:satnum>')
def noradnum(satnum):
    TLE = Query()
    results = db.search(TLE.satnum == satnum)
    view = ''
    if len(results) > 0:
        for result in results:
            view = view + result['header'] + '\n'
            view = view + result['line1'] + '\n'
            view = view + result['line2'] + '\n'
    return view, {'Content-Type': 'text/plain'}
        
