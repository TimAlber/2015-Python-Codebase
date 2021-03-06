import asyncio
import wpilib
import yeti

from yeti.interfaces import gamemode
from yeti.wpilib_extensions import Referee


class ServoMover(yeti.Module):
    """
    A bare-bones example of an arcade drive module.
    """

    def module_init(self):
        #Initialize the Referee for the module.
        self.referee = Referee(self)

        #Setup a joystick
        self.joystick = wpilib.Joystick(0)
        self.referee.watch(self.joystick)

        #Setup the robotdrive
        self.servo = wpilib.Servo(5)
        self.referee.watch(self.servo)

        #Set the teleop_loop to run.
        self.start_coroutine(self.teleop_loop())

    @asyncio.coroutine
    def teleop_loop(self):

        #Loop forever
        while True:
            #Wait until we are in teleop mode.
            yield from gamemode.wait_for_teleop()

            self.servo.set(self.joystick.getZ()+1)

            #Pause for a moment to let the rest of the code run.
            yield from asyncio.sleep(.05)