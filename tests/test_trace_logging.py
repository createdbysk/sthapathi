import trace_logging
import nose.tools


class TestTraceLogging(object):
    def test_trace_exists(self):
        trace_logger = trace_logging.getLogger(self.__module__)
        nose.tools.assert_is_not_none(trace_logger.trace)