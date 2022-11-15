import json
from dataclasses import dataclass
from main import msg

def Data():
    if msg != "next":
        dict = json.loads(msg)

        @dataclass
        class Config:
            mode: str = dict['mode']
            time_limit: int = dict['time_limit']
            players: list = dict['players']
            dob: list = dict['dob']

if __name__ == "__main__":
    Data()