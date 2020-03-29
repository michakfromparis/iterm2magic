#!/usr/bin/env python3
# Terminal Instant Manager
import sys
import os
import os.path
import getopt
import json
import iterm2

profile = 'Default'
command = ""
tabs = {}
config = {}

app_uri = 'net.michak.tim'
configuration_directory = os.path.join(
    os.path.expanduser("~"), 'Library', 'Containers', app_uri)
configuration_file = os.path.join(configuration_directory, 'tim.json')

def start(args):
  print('starting')
  for set in args:
    pair = set.split('@')
    tabs[pair[1]] = pair[0]
    print('create term tab named', pair[1], 'and run', pair[0])


def stop(args):
  print('stoping')


def usage(script_name):
  print()
  print()
  print('Usage: ', script_name,
        ' COMMAND command1@tabTitle1 [command2@tabTitle] ...')
  print()
  print('create iTerm windows & tabs with set title and start / stop command')
  print()
  print('Commands:')
  print('  start\t\tFor each title@command, creates a tab and runs command')
  print('  stop\t\tFor each title@command, runs command and closes tab')
  print()
  sys.exit(-42)


async def iTermStart(connection):
  app = await iterm2.async_get_app(connection)
  current_window = app.current_terminal_window
  new_window = await iterm2.Window.async_create(connection, profile)
  print('window id:\t', new_window.window_id)
  print('window number:\t', new_window.window_number)
  global config
  if config['windows'] is None:
    config['windows'] = {}
  config['windows'][new_window.window_id] = {'tabs':[new_window.current_tab.tab_id]}
  await new_window.async_set_title('tim')
  firstTab = True
  for tabTitle in tabs:
    command = tabs[tabTitle]
    if firstTab == True:
      await new_window.current_tab.async_set_title(tabTitle)
      await new_window.current_tab.current_session.async_send_text(command + '\n')
      firstTab = False
    else:
      new_tab = await new_window.async_create_tab(profile)
      config['windows'][new_window.window_id]['tabs'].append(new_tab.tab_id)
      await new_tab.async_set_title(tabTitle)
      await new_tab.current_session.async_send_text(command + '\n')
  global configuration_file
  with open(configuration_file, 'w') as out_file:
    json.dump(config, out_file)
  await current_window.current_tab.current_session.async_inject('created {} window with {} tabs\n'.format(1, len(tabs)).encode())


async def iTermStop(connection):
  print("stoping")
  app = await iterm2.async_get_app(connection)
  for window_id in config['windows']:
    window = app.get_window_by_id(window_id)
    if window is not None:
      await window.async_close()



async def iTerm(connection):
    if command == 'start':
      await iTermStart(connection)
    elif command == 'stop':
      await iTermStop(connection)


def init(args):
  scriptPath = os.path.basename(args[0])
  script_name = args[0].split('/')[-1]
  print('scriptPath:\t', scriptPath)
  print('script_name:\t', script_name)
  print('argsCount:\t', len(args))
  print('args:\t\t', str(args))
  if len(args) < 2:
    usage(script_name)
  if not os.path.exists(configuration_directory):
    print('creating configuration directory at', configuration_directory)
    os.makedirs(configuration_directory)
  if os.path.exists(configuration_file) and os.path.isfile(configuration_file):
    with open(configuration_file) as json_file:
      global config
      config = json.load(json_file)

  global command
  command = args[1]
  print('command:\t', command)
  if command == 'start':
    start(args[2:])
  elif command == 'stop':
    stop(args[2:])
  else:
    print('Unknown command ', command)


def main():
  init(sys.argv)
  iterm2.run_until_complete(iTerm)


if __name__ == "__main__":
    main()
