from pykeepass import PyKeePass
import argparse
import getpass
import subprocess


def open_keepass(kdb_path):
    password = getpass.getpass(prompt="Password for " + kdb_path + ": ")
    kp = PyKeePass(kdb_path, password)
    return kp


def create_onepass_entry(kp_entry, vault_name):
    args = 'op create item Login'.split()
    args += ['--title', kp_entry.title]
    args += ['--vault', vault_name]

    if kp_entry.username:
        args.append('username=' + kp_entry.username)
    if kp_entry.password:
        args.append('password=' + kp_entry.password)
    if has_notes(kp_entry):
        args.append('notes=' + get_notes(kp_entry) + '')
    if not kp_entry.group.is_root_group:
        args.append('tags=' + kp_entry.group.name)
    # print(args)

    subprocess.run(args)


def has_notes(kp_entry):
    return kp_entry.custom_properties or kp_entry.notes


def get_notes(kp_entry):
    return "{}\nCUSTOM:\n{}".format(kp_entry.notes, kp_entry.custom_properties) if kp_entry.custom_properties else kp_entry.notes


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("kdb", help="keepass database")
    parser.add_argument("vault", help="1Password vault name")

    args = parser.parse_args()

    kp = open_keepass(args.kdb)

    for entry in kp.entries:
        # notes = get_notes(entry)
        # print("Title: {} U:{} P:{} N:{}    GRP:{}".format(entry.title, entry.username, entry.password, notes, entry.group)) #If you're sure nobody's shoulder-surfing
        # If you prefer the entire title to be visible
        print("Creating entry for {}".format(entry.title))
        # print("Creating entry for {}".format(entry.title[0:3] + ('*' * (len(entry.title) - 2)))) # If you prefer to mask the title entries

        create_onepass_entry(entry, args.vault)

# Format for adding items to a vault using the op CLI tool
# ./op create item "Login" --title "MooCow3" username="Moo" password="cow" notes="This is a moo cow" --vault "Test Vault" tags="barn,chickens,does not type"
