"""Windows compatibility shim for the missing pwd module."""

class _PwdEntry(tuple):
    def __new__(cls, pw_name="", pw_passwd="", pw_uid=0, pw_gid=0, pw_gecos="", pw_dir="", pw_shell=""):
        return super().__new__(cls, (pw_name, pw_passwd, pw_uid, pw_gid, pw_gecos, pw_dir, pw_shell))

    @property
    def pw_name(self):
        return self[0]

    @property
    def pw_passwd(self):
        return self[1]

    @property
    def pw_uid(self):
        return self[2]

    @property
    def pw_gid(self):
        return self[3]

    @property
    def pw_gecos(self):
        return self[4]

    @property
    def pw_dir(self):
        return self[5]

    @property
    def pw_shell(self):
        return self[6]


def getpwnam(name):
    return _PwdEntry(name, "x", 0, 0, "", "", "")


def getpwuid(uid):
    return _PwdEntry("nobody", "x", uid, 0, "", "", "")
