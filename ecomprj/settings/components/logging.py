from ecomprj.settings.components import BASE_DIR


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "debug_file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": f"{BASE_DIR}/logs/debug.log",
        },
        "error_file": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": f"{BASE_DIR}/logs/error.log",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["debug_file"],
            "level": "INFO",
            "propagate": True,
        },
        "": {
            "handlers": ["error_file"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}
