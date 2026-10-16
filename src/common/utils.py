from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bfp_rs import BaseStruct

def clone[T: BaseStruct](struct: T) -> T:
    return struct.from_bytes(struct.to_bytes(), ver = struct.ver, strict = True)
