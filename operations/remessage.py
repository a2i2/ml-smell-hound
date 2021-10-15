# ...

overriden_symbols = {
    "too-many-arguments": "Too many arguments, consider moving hyperparameters to a config file."
}


def override_msg(obj):

    if obj["symbol"] in overriden_symbols:
        obj["message"] = overriden_symbols["symbol"]
