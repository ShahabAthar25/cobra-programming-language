tree = {
    "printLn": {
        "type": "inline_func",
        "allowed_args": {
            "endsWith": {
                "default": "\n",
                "required": True,
            }
        }
    },
    "inputLn": {
        "type": "inline_func",
        "allowed_args": {
            "endsWith": {
                "default": "\n",
                "required": True,
            },
            "showInput": {
                "default": True,
                "required": True
            }
        }
    }
}