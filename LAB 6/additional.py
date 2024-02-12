import re

states = "Mississippi Alabama Texas Massachusetts Kansas"

statesList = []

match_xas = re.search(r'\bxas\b', states)
if match_xas:
    statesList.append(match_xas.group())

match_k_s = re.search(r'\b[kK].*s\b', states)
if match_k_s:
    statesList.append(match_k_s.group())

match_M_s = re.search(r'\b[Mm].*s\b', states)
if match_M_s:
    statesList.append(match_M_s.group())

match_a = re.search(r'\ba\b', states)
if match_a:
    statesList.append(match_a.group())

match_M_start = re.search(r'\b[Mm].*', states)
if match_M_start:
    statesList.append(match_M_start.group())

print("States List:", statesList)
