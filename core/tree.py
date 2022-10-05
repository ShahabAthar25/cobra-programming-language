functions = {
    "printLn": {
        "type": "inline_func",
        "allowed_args": {
            "endsWith": {
                "default": "\n",
                "isBoolean": False,
            },
        }
    },
    "inputLn": {
        "type": "inline_func",
        "allowed_args": {
            "endsWith": {
                "default": "\n",
                "isBoolean": False,
            },
            "showInput": {
                "default": True,
                "isBoolean": True,
            }
        }
    }
}