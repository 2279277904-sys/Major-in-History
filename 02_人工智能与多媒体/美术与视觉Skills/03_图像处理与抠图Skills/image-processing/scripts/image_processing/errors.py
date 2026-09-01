"""Typed failures mapped to the public CLI exit-code contract."""


class ProcessingError(Exception):
    exit_code = 2
    error_code = "validation_error"


class ValidationFailure(ProcessingError):
    exit_code = 2
    error_code = "validation_error"


class DependencyFailure(ProcessingError):
    exit_code = 3
    error_code = "environment_error"


class InferenceFailure(ProcessingError):
    exit_code = 4
    error_code = "inference_error"


class FileFailure(ProcessingError):
    exit_code = 5
    error_code = "file_error"
