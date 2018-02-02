"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Matthew De Clerck.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # ------------------------------------------------------------------
    # Done: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # ------------------------------------------------------------------

    root = tkinter.Tk()

    # ------------------------------------------------------------------
    # Done: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # ------------------------------------------------------------------

    frame1 = ttk.Frame(root, padding=20)
    frame1.grid()

    # ------------------------------------------------------------------
    # Done: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # ------------------------------------------------------------------

    hello_button = ttk.Button(frame1, text='Say Hello')
    hello_button.grid()

    # ------------------------------------------------------------------
    # Done: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # ------------------------------------------------------------------

    hello_button['command'] = lambda: print_hello()

    # ------------------------------------------------------------------
    # Done: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # ------------------------------------------------------------------

    my_entry_box = ttk.Entry(frame1)
    my_entry_box.grid()

    hello_goodbye_button = ttk.Button(frame1, text='Check for ok')
    hello_goodbye_button['command'] = lambda: check_for_ok(my_entry_box)
    hello_goodbye_button.grid()

    # ------------------------------------------------------------------
    # TODO: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # ------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################

    my_entry_box = ttk.Entry(frame1)
    my_entry_box.grid()

    how_are_you_button = ttk.Button(frame1, text='How are you?')
    how_are_you_button['command'] = lambda: how_are_you(my_entry_box)
    how_are_you_button.grid()

    well_done_button = ttk.Button(frame1, text='Say well done!')
    well_done_button.grid()

    well_done_button['command'] = lambda: print_well_done()

    # ------------------------------------------------------------------
    # Done: 8. As time permits, do other interesting GUI things!
    # ------------------------------------------------------------------

    root.mainloop()


def print_hello():
    print("Hello")

def print_well_done():
    print("Well done!")


def check_for_ok(entry_box):
    contents = entry_box.get()
    if contents == 'ok':
        print('Hello')
    else:
        print('Goodbye')

def how_are_you(entry_box):
    contents = entry_box.get()
    if contents == 'How are you?':
        print('I am fine.')
    else:
        print('Can you repeat that?')


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
