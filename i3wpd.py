#!/usr/bin/env python
"""Custom wallpaper for all your i3 workspaces."""
import os
import sys
import time
import i3msg as i3

I3WPD_DEB = False
def dbg(msg):
    """Print to stdout"""
    if I3WPD_DEB:
        print(__name__ + ' : ' + msg)

class i3_Wpd:
    """Wallpaper setter daemon"""
    def __init__(self, bg_options, wp_dir, img_format):
        self.wp_cmd = 'feh ' + bg_options
        if not wp_dir.endswith('/'):
            wp_dir.append('/')
        self.wp_dir = wp_dir
        self.img_format = img_format
        dbg('Launch!')
        self.ws_reload()
        
        i3.subscribe(['workspace', 'shutdown', 'output'], self.focus_changed_handler)

    def set_wp(self):
        """Sets wallpaper, assuming i3-msg reports outputs in the same order as xinerama."""
        cmd = self.wp_cmd
        for ws in self.active_workspaces:
            cmd += ' ' + self.wp_dir + ws + self.img_format
        dbg(cmd)
        os.system(cmd)

    def ws_update(self):
        """Call on workspace focus change"""
        current_outputs = i3.send(i3.GET_OUTPUTS)
        n = 0
        for out in current_outputs:
            if out['active']:
                self.active_workspaces[n] = out['current_workspace']
                n += 1
        self.set_wp()

    def ws_reload(self):
        """Call on server output change"""
        dbg("Output change!")
        self.active_workspaces = []
        current_outputs = i3.send(i3.GET_OUTPUTS)
        for out in current_outputs:
            if out['active']:
                self.active_workspaces.append(out['current_workspace'])
        self.set_wp()

    def focus_changed_handler(self, event, data):
        """This daemon dies with i3"""
        if event == i3.workspace:
            if data['change'] == 'focus':
                self.ws_update()
        elif event == i3.output:
            self.ws_reload()
        elif event == i3.shutdown:
            dbg('i3 exit.')
            os._exit(0)



if __name__ == '__main__':
    if len(sys.argv) == 4:
        i3_Wpd(sys.argv[1], sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 3:
        i3_Wpd('--bg-center --bg black', sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 2:
        if sys.argv[1] == 'default':
            wp_dir = os.getcwd() + '/'
            if os.path.exists(wp_dir + 'backgrounds/') and os.path.isdir(wp_dir + 'backgrounds/'):
                 wp_dir += 'backgrounds/'
            i3_Wpd('--bg-center --bg black', wp_dir, '.png')
    else:
        print('i3wll.py - sets a custom wallpaper on every desktop')
        print('usage: i3wll.py [\"options\"] directory filetype')
        print('usage: i3wll.py default')
        print('options: \"--bg-center|--bg-fill|--bg-scale [--bg black]\".\nOther options may apply, see man feh(1).')
        exit()

    while True:
        time.sleep(1)
    