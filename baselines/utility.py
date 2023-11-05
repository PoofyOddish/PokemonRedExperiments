import json
def fetch_rom_ref():
    with open('reference_data/rom_values.json') as f:
        data = json.load(f)
        return(data)

def convert_hex_string_to_int(val:str) -> int:
    return(int(val,16))