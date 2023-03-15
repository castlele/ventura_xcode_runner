#!/usr/local/bin/python3

import sys
import os


BLACK_LIST = ["Xcodes.app"]
CUR_MAJOR_V = "14"
DEFAULT_V = "13.2.1"
BASE_DIR = "/Applications/"
EXECUTABLE_PATH = "/Contents/MacOS/Xcode"
DEFAULT_XCODE_NAME = "Xcode.app"

OPEN_CMD = "open"
HELP_CMD = "help"
V_LIST_CMD = "versions"

XCODEPROJ = "xcodeproj"
XCWORKSPACE = "xcworkspace"

def configure_app_version(app: str) -> str:
    components = app.split("-")

    if len(components) == 1:
        return DEFAULT_V

    return ".".join(components[1].split(".")[:-1])


def get_available_xcodes() -> dict:
    return {configure_app_version(app): BASE_DIR + app
            for app in os.listdir(BASE_DIR)
            if "xcode" in app.lower() and app not in BLACK_LIST}


def xcode_version_parser(version: str) -> str:
    available_xcodes = get_available_xcodes()

    if version in available_xcodes:
        return available_xcodes[version]

    major = version.split(".")[0]

    for k, v in available_xcodes.items():
        if major in k:
            return v

    print(f"There is no available version: {version}")
    exit(1)


def get_workspace_path(path: str) -> str:
    files = os.listdir(path)
    workspace_filter = list(filter(lambda file: XCWORKSPACE in file, files))
    xproj_filter = list(filter(lambda file: XCODEPROJ in file, files))

    if (workspace_filter):
        return workspace_filter[0]

    if (xproj_filter):
        return xproj_filter[0]

    return ""


def print_help():
    print("""
    xrun                        : opens default xcode (usually with name Xcode.app).
    xrun <xcode_version>        : opens xcode with specified version, if there is no specified version, program will search by major version.
    xrun versions               : prints a full list of available versions.
    """)


def print_xcode_version():
    print([k for k in get_available_xcodes().keys()])


def execute_open_command(command: str, workspace: str = ""):
    open = OPEN_CMD + " " + command

    if CUR_MAJOR_V not in command:
        os.system(open + EXECUTABLE_PATH + " " + workspace)
        return

    os.system(open + " " + workspace)


def main():
    arguments = sys.argv

    if len(arguments) < 2:
        path = xcode_version_parser(DEFAULT_V)
        execute_open_command(path)
        exit(0)

    if arguments[1] == HELP_CMD:
        print_help()
        exit(0)

    if arguments[1] == V_LIST_CMD:
        print_xcode_version()
        exit(0)

    path = xcode_version_parser(arguments[1])
    workspace_path = ""

    if len(arguments) > 2:
        workspace_path = get_workspace_path(arguments[2])

    execute_open_command(path, workspace=workspace_path)


if __name__ == "__main__":
    main()
