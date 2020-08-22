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

Magic should happen.  If you're logged into 1Password, you might even see your passwords appearing in your vault.

# Dedication

This software is dedicated to everyone affected by the derecho that hit eastern Iowa on August 10, 2020.  Particularly those in Cedar Rapids.

If this software is helpful and you want to show your appreciation, here are a few places that helped people in Iowa that needed it:
* [World Central Kitchen](https://wck.org/) was on the ground quickly, [helping people that really needed it](https://wck.org/).
* [Hawkeye Area Community Action Program](https://www.hacap.org/) is a local nonprofit that has been helping with food and other needs.
* [United Way of East Central Iowa](https://www.uweci.org/) jumped in to help pretty fast, too.

Many thanks to the helpers, especially those that helped while also working on their own recovery needs!