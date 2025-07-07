import re

def parse_time_input(time_input):
    time_input = time_input.lower()
    time_input = time_input.replace("p.m.", "").replace("a.m.", "")
    time_input = time_input.replace("pm", "").replace("am", "").replace(".", "")
    time_input = time_input.strip()

    match = re.search(r'(\d{1,2})[:\s]?(\d{2})', time_input)
    if match:
        hours = int(match.group(1))
        minutes = int(match.group(2))
        if 0 <= hours < 24 and 0 <= minutes < 60:
            return f"{hours:02d}:{minutes:02d}"
    return None
