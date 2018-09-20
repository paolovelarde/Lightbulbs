class LightSwitch():

    def __init__(self, state):
        self._state = state

    def __str__(self):
        return 'I am ' + str(self._state)

    def turn_on(self):
        self._state = 'on'

    def turn_off(self):
        self._state = 'off'

    def flip(self):
        if self._state == 'on':
            self._state = 'off'
        else:
            self._state = 'on'


class SwitchBoard():

    def __init__(self, num_switches):
        self._num_switches = num_switches
        self._switchboard = []
        for i in range(0, num_switches):
            self._switchboard.append(i)
            for i in self._switchboard:
                self._switchboard[i] = False

    def __str__(self):
        self._on_switches = ''
        for switches in range(0, len(self._switchboard)):
            if self._switchboard[switches] is True:
                self._on_switches = self._on_switches + str(switches) + ' '
        return 'The following switches are on: ' + str(self._on_switches)

    def which_switch(self):
        self._on_switches = []
        for switches in range(0, len(self._switchboard)):
            if self._switchboard[switches] is True:
                self._on_switches.append(switches)
        return self._on_switches

    def flip(self, n):
        if n in range(0, len(self._switchboard)):
            if self._switchboard[n] is True:
                self._switchboard[n] = False
            else:
                self._switchboard[n] = True
        else:
            None

    def flip_every(self, s):
        for s in range(0, len(self._switchboard), s):
            if self._switchboard[s] is True:
                self._switchboard[s] = False
            else:
                self._switchboard[s] = True

    def reset(self):
        for i in range(0, len(self._switchboard)):
            self._switchboard[i] = False
