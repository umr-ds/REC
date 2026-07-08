from msgspec.msgpack import Decoder, Encoder

from rec.eid import EID


def _enc_hook(obj: object) -> object:
    # msgspec does not recognize subclasses of built-in types, so we need to handle EID explicitly.
    if isinstance(obj, EID):
        return str(obj)
    msg = f"Encoding objects of type {type(obj).__name__} is unsupported"
    raise NotImplementedError(msg)


# Reusing a single Encoder/Decoder.
_encoder = Encoder(enc_hook=_enc_hook)
_decoder = Decoder()

encode = _encoder.encode
decode = _decoder.decode
