#!/usr/bin/env python
# Copyright (C) 2011-2014 Swift Navigation Inc.
# Contact: Fergus Noble <fergus@swiftnav.com>
#
# This source is subject to the license found in the file 'LICENSE' which must
# be be distributed together with this source. All other rights reserved.
#
# THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
# EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.

from construct import *
import base64
import copy
import json
import struct

SBP_PREAMBLE = 0x55

# Default sender ID. Intended for messages sent from the host to the
# device.
SENDER_ID = 0x42

class SBP(object):
  """Swift Binary Protocol container.

  """

  _parser = Struct("SBP",
                   ULInt16('msg_id'),
                   Bytes("payload", lambda ctx: ctx.length),)

  __slots__ = ['msg_id',
               'payload'
              ]

  def __init__(self, msg_id=None, payload=None):
    self.msg_id = msg_id
    self.payload = payload

  def __eq__(self, other):
    try:
      if self is other:
        return True
      elif not isinstance(self, type(other)):
        return False
      elif self.__slots__ != other.__slots__:
        return False
      else:
        return all(getattr(self, s) == getattr(other, s) for s in self.__slots__)
    except AttributeError:
      return False

  def __update(self):
    raise NotImplementedError("Internal update used by children.")

  def _get_framed(self):
    """Returns the framed message and updates the CRC.

    """
    framed_msg = struct.pack('<H', self.msg_id)
    framed_msg += self.payload
    return framed_msg

  def pack(self):
    """Pack to framed binary message.

    """
    return self._get_framed()

  @staticmethod
  def unpack(d):
    """Unpack and return a framed binary message.

    """
    p = SBP._parser.parse(d)
    #assert p.preamble == SBP_PREAMBLE, "Invalid preamble 0x%x." % p.preamble
    return SBP(p.msg_id, p.payload)

  def copy(self):
    return copy.deepcopy(self)

  def __repr__(self):
    p = (self.msg_id, repr(self.payload))
    fmt = "<SBP (msg_id=0x%X, payload=%s)>"
    return fmt % p

  def to_binary(self):
    ret = struct.pack("<H", self.msg_id)
    if self.payload:
        ret += self.payload
    return ret

  def to_json(self):
    """Produce a JSON-encoded SBP message.

    """
    d = self.to_json_dict()
    return json.dumps(d)

  @staticmethod
  def from_json(s):
    """Given a JSON-encoded message, build an object.

    """
    d = json.loads(s)
    sbp = SBP.from_json_dict(d)
    return sbp

  @staticmethod
  def from_json_dict(d):
    sbp = SBP()
    sbp.msg_id = d.pop('msg_id')
    sbp.payload = base64.standard_b64decode(d.pop('payload'))
    return sbp

  def to_json_dict(self):
    payload = base64.standard_b64encode(self.payload) if self.payload else None
    return {
            'msg_id': self.msg_id,
            'payload': payload
           }
