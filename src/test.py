from pathlib import Path

from backend.bible import Vulgate

fn = Path("/home/john/code/divinum-officium/web/www/horas/Help/vulgate.txt")
vulgate = Vulgate("vulgate")
vulgate.from_file(fn)

print(vulgate.content.keys())

print(vulgate.content.Gn["1"]["10"])

vulgate.get_range("Gn1:1", None)
