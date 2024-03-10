"""The Bowling Game Scorer."""


class BowlingFrame:
    """Keeping the record of each bowling frame."""

    def __init__(self, max_roll=2):
        """Construct a frame"""
        self.pins = [0] * max_roll
        self.max_roll = max_roll
        self.next_roll = 0
        self.is_scored = False  # Flag to track if frame is scored

    def roll(self, pins: int):
        """Roll the ball swipe pins"""
        if self.next_roll < self.max_roll and not self.is_scored:
            self.pins[self.next_roll] = pins
            self.next_roll += 1
            self.is_scored = self.is_spare() or self.is_strike()

    def score(self):
        """Score of each frame"""
        if not self.is_scored:
            self.is_scored = True  # Mark frame as scored even if open frame (0 pins)
        total = 0
        for index in range(self.max_roll):
            total += self.pins[index]
        return total

    def is_spare(self):
        """Check if spare"""
        return self.max_roll == 1 and sum(self.pins) == 10

    def is_strike(self):
        """Check if strike"""
        return self.pins[0] == 10


class BowlingFrame10(BowlingFrame):
    """Keeping the record of each bowling frame (10th frame)."""

    def __init__(self):
        """Construct a frame"""
        super().__init__(3)
        self.bonus = 0  # Track bonus points for this frame

    def score(self):
        """Score of each frame"""
        if not self.is_scored:
            self.is_scored = True  # Mark frame as scored even if open frame (0 pins)
        total = 0
        for index in range(self.max_roll):
            total += self.pins[index]
        total += self.bonus

        return total


class BowlingGame:
    """The Bowling Game."""

    GAME_COMPLETED = -1

    def __init__(self):
        """The Bowling Game"""

        self.frames = []
        for _ in range(9):
            self.frames.append(BowlingFrame())

        self.frames.append(BowlingFrame10())
        self.cur_frame = 0
        self.cur_roll = 1
        self.bonus = 0  # Track bonus points for spares and strikes

    def roll(self, num_of_pin: int):
        """Roll a bowling ball.

        Args:
            num_of_pin: The number of knocked-down pins

        Returns:
            None

        """
        self.frames[self.cur_frame].roll(num_of_pin)

        # Update frame and roll based on current state
        if self.cur_roll == 1:
            self.cur_roll = 2
        elif self.cur_frame < 9 and self.cur_roll == 2:
            self.cur_frame += 1
            self.cur_roll = 1
        elif self.cur_frame == 9:
            if self.frames[9].is_strike() and self.cur_roll < 3:
                self.cur_roll += 1
            elif (self.frames[9].is_spare() or self.frames[9].is_strike()) and self.cur_roll == 2:
                self.cur_roll = 3
            else:
                self.cur_frame = self.GAME_COMPLETED

    def score(self):
        """Get the current score.

        Returns:
                The current score.

        """
        total = 0
        for frame in self.frames:
            total += frame.score()

        # Add bonus points for spares and strikes (considering next rolls)
        total += self.bonus
        for i in range(self.cur_frame + 1):
            if self.frames[i].is_strike():
                if self.cur_frame >= i + 2:
                    total += self.frames[i + 1].pins[0] + self.frames[i + 2].pins[0]
                elif self.cur_frame == i + 1:
                    total += self.frames[i + 1].score()
            elif self.frames[i].is_spare():
                if self.cur_frame >= i + 1:
                    total += self.frames[i + 1].pins[0]

        return total


