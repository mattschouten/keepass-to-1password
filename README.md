# keepass-to-1password

This program is a thin wrapper around the 1Password command-line tool and KeePass databases to allow a one-time migration from KeePass to 1Password.

This is not super-secure.  From a bit of quick research, Python does not make it easy to securely destroy strings in memory.  Also, using the `op` tool potentially puts passwords and other secrets into command line arguments that may be visible from outside your login shell.  

But it's way less failure-prone than trying to re-type usernames, passwords, and notes.

## Prerequisites

Install the 1Password `op` tool according to its instructions.  Make sure it is available on your path. 

You'll need `PyKeePass`.  `pip install pykeepass` will work.  If you want to use a virtual environment:
```sh
python3 -m venv env
source env/bin/activate
pip install pykeepass
```

Any vault you want to create passwords in should exist prior to running this program.  If you want to import your KeePass database to "My Super Cool Vault", create "My Super Cool Vault".

## Running

Sign in to the 1Password `op` tool.  This is probably `op signin https://my.1password.com my_email@example.com -` but it may be different.  You will need your secret key and your password most likely.  After you sign in, `op` will give you a session token.  If you don't export the session token as it tells you, the rest of it will probably not work.

Then run `python3 keepass-to-1password.py <path to keepass file> <1Password Vault>`

Magic should happen.