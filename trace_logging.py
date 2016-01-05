"""
Adds a trace() function with level TRACE to logging.
"""
from logging import *

# Implement a TRACE log level and a trace() function that logs at that level.
TRACE = 9
addLevelName(TRACE, "TRACE")


def __trace(self, message, *args, **kws):
    # Yes, logger takes its '*args' as 'args'.
    if self.isEnabledFor(TRACE):
        self._log(TRACE, message, args, **kws)

# Add the trace method to the logger
Logger.trace = __trace
