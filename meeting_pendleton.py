# Set the scene at the garden.
import sys
import time
seeing_mr_pendleton = ('...the ringing in your ears is getting louder.\n' 
        "When had it even started? A moment ago they were fine.\n" 
        "But there wasn't a moment ago. There was only this man's face\n" 
        "staring at you with grey eyes and moving his wormy lips as if speaking.\n" 
        "Did he not hear the ringing?\n")
for letter in seeing_mr_pendleton:
    sys.stdout.write(letter)
    time.sleep(0.06)

prompt = input("\nMr. Pendleton: Son I need you to wake the fuck up and focus! "
               "Do you even want to be here?\n")
if prompt.lower() == 'yes':
    print("Mr. Pendleton: Good. Now pay attention because we need "
        "this to work properly each time every time.")
else:
    print("Mr. Pendleton: Well that's too bad. Your family signed a waiver.")
import introduction