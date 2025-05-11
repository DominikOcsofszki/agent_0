from agents.logger_config import setup_logger

import inspect


class FakeDB:
    logger = setup_logger("FAKE_DB")

    def _log_fake_db(self, log):
        self.logger.info(log)
        return log

    def log_fake_db_args(self, frame):
        args, a, b, values = inspect.getargvalues(frame)
        function_name = inspect.getframeinfo(frame).function
        args_info = {arg: values[arg] for arg in args}
        return f"fun: {function_name}| args: {args_info}"
        # return __log_fake_db(
        #     f"Function '{function_name}' called with arguments {args_info}"
        # )
        return self._log_fake_db(f"{function_name}({args_info})")
        # return f"Function '{function_name}' called with arguments {args_info}"
