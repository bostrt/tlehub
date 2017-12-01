#!/usr/bin/env python
from tinydb import TinyDB, Query
import os
import click

DB_FILE = os.getenv('DB_FILE', 'tlehub.json')

def load(db, inputfile):
    header = None
    line1 = None
    satnum = None
    line2 = None
    flush = False
    for line in inputfile:
        if line.startswith('1'):
            line1 = line
            satnum = int(line1[2:7])
        elif line.startswith('2'):
            line2 = line
            flush = True
        else:
            header = line
            flush = False
        if flush:
            db.insert({'header': header.strip(), 'line1': line1.strip(), 'line2': line2.strip(), 'satnum': satnum})
    
@click.command()
@click.argument('inputfile', type=click.Path(file_okay=True, dir_okay=False, exists=True))
@click.option('--dump', is_flag=True)
def main(inputfile, dump):
    db = TinyDB(DB_FILE)
    load(db, open(inputfile, 'r'))
    if dump:
        print(db.all())

if __name__=='__main__':
    main()
