def parse_script(script_text: str):
    """
    Break script into visual blocks.
    Each block should have { 'line': str, 'clip': str } for matching assets.
    """
    lines = script_text.strip().split('\n')
    blocks = []
    for i, line in enumerate(lines):
        clip = f"clip_{i+1}.mp4"
        blocks.append({"line": line, "clip": clip})
    return blocks
