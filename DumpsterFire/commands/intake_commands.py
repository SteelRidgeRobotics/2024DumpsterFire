import wpilib
import commands2
from subsystems.intake import IntakeAndPivot


class FeederTest(commands2.Command):

    def __init__(self, IntakeAndPivot : IntakeAndPivot):
        self.intake = IntakeAndPivot
        self.addRequirements(self.intake)

    def initialize(self):
        return super().initialize()

    def execute(self):
        self.intake.consume()

    def isFinished(self) -> bool:
        return False

class FeederTestDrop(commands2.Command):

    def __init__(self, IntakeAndPivot : IntakeAndPivot):
        self.intake = IntakeAndPivot
        self.addRequirements(self.intake)

    def initialize(self):
        return super().initialize()

    def execute(self):
        self.intake.disencumber()

    def isFinished(self) -> bool:
        return False
    
class FeederTestStop(commands2.Command):

    def __init__(self, IntakeAndPivot : IntakeAndPivot):
        self.intake = IntakeAndPivot
        self.addRequirements(self.intake)

    def initialize(self):
        return super().initialize()

    def execute(self):
        self.intake.hold()

    def isFinished(self) -> bool:
        return False