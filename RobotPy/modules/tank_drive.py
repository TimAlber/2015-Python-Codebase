import asyncio
import wpilib
import yeti

from yeti.interfaces import gamemode
from yeti.wpilib_extensions import Referee


class TankDrive(yeti.Module):
    """
    A 2-Joystick Mecanum drivetrain module, using Tank drive.
    UNFINISHED!!!!!
    """

    USE_CAN = False

    def module_init(self):
        #Initialize the Referee for the module.
        self.referee = Referee(self)

        #Setup a joystick
        self.joystick = wpilib.Joystick(0)
        self.referee.watch(self.joystick)

        if self.USE_CAN:
            motor_controller_class = wpilib.CANJaguar
        else:
            motor_controller_class = wpilib.Jaguar

        #Setup CAN Jaguars
        self.right_front_cim = motor_controller_class(0)
        self.referee.watch(self.right_front_cim)

        self.left_front_cim = motor_controller_class(1)
        self.referee.watch(self.left_front_cim)

        self.right_rear_cim = motor_controller_class(2)
        self.referee.watch(self.right_rear_cim)

        self.left_rear_cim = motor_controller_class(3)
        self.referee.watch(self.left_rear_cim)

        #Setup the robotdrive
        self.robotdrive = wpilib.RobotDrive(self.left_front_cim, self.left_rear_cim, self.right_front_cim, self.right_rear_cim)
        self.referee.watch(self.robotdrive)


    @gamemode.teleop_task
    @asyncio.coroutine
    def teleop_loop(self):

        #Loop until end of teleop mode.
        while gamemode.is_teleop():

            strafemode = self.joystick.getRawButton(9)

            if strafemode:
                self.robotdrive.mecanumDrive_Cartesian(-self.joystick.getX(), -self.joystick.getY(), 0, 0)
            else:
                self.robotdrive.mecanumDrive_Cartesian(0, -self.joystick.getY(), -self.joystick.getX(), 0)

            #Pause for a moment to let the rest of the code run.
            yield from asyncio.sleep(.05)
