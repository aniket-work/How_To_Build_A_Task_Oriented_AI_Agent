"""functions or objects shared by agents"""

import re
import json

from agentlite.actions.BaseAction import BaseAction


def name_checking(name: str):
    """ensure no white space in name"""
    white_space = [" ", "\n", "\t"]
    for w in white_space:
        if w in name:
            return False
    return True


def act_match(input_act_name: str, act: BaseAction):
    if input_act_name == act.action_name:  # exact match
        return True
    ## To-Do More fuzzy match
    return False


import re
import json

import re
import json


def parse_action(string: str) -> tuple[str, dict, bool]:
    """
    Parse an action string into an action type and an argument.
    """
    # Define the pattern we're looking for
    pattern = r"Action:(\w+)\[(.+)\]"

    # Search for the pattern in the entire string
    match = re.search(pattern, string)

    if match:
        action_type = match.group(1).strip()
        arguments = match.group(2).strip()
        try:
            arguments = json.loads(arguments)
            return action_type, arguments, True
        except json.JSONDecodeError:
            return f"{action_type}[{arguments}]", {}, False
    else:
        return "", {}, False


AGENT_CALL_ARG_KEY = "Task"
NO_TEAM_MEMEBER_MESS = (
    """No team member for manager agent. Please check your manager agent team."""
)
ACION_NOT_FOUND_MESS = (
    """"This is the wrong action to call. Please check your available action list."""
)
