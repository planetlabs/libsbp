#!/usr/bin/env python
# Copyright (C) 2015 Swift Navigation Inc.
# Contact: Fergus Noble <fergus@swiftnav.com>
#
# This source is subject to the license found in the file 'LICENSE' which must
# be be distributed together with this source. All other rights reserved.
#
# THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
# EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.


"""
Demonstrating SBP messages
"""

from construct import *
import json
from sbp.msg import SBP, SENDER_ID
from sbp.utils import fmt_repr, exclude_fields, walk_json_dict, containerize, greedy_string

# Automatically generated from sbp/sc/testapp.yaml with generate.py.
# Please do not hand edit!


class testapp_channel(object):
  """testapp_channel.
  
  Example structure
  
  Parameters
  ----------
  c1 : int
    first field.
  c2 : int
    second field.
  c3 : int
    third field.

  """
  _parser = Embedded(Struct("testapp_channel",
                     ULInt32('c1'),
                     SLInt16('c2'),
                     ULInt8('c3'),))
  __slots__ = [
               'c1',
               'c2',
               'c3',
              ]

  def __init__(self, payload=None, **kwargs):
    if payload:
      self.from_binary(payload)
    else:
      self.c1 = kwargs.pop('c1')
      self.c2 = kwargs.pop('c2')
      self.c3 = kwargs.pop('c3')

  def __repr__(self):
    return fmt_repr(self)
  
  def from_binary(self, d):
    p = testapp_channel._parser.parse(d)
    for n in self.__class__.__slots__:
      setattr(self, n, getattr(p, n))

  def to_binary(self):
    d = dict([(k, getattr(obj, k)) for k in self.__slots__])
    return testapp_channel.build(d)
    
SBP_TESTAPP_PING = 0x0068
class TestappPing(SBP):
  """SBP class for message TESTAPP_PING (0x0068).

  You can have TESTAPP_PING inherit its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  This message pings the test application to generate
a TESTAPP_PONG reply.


  """
  __slots__ = []

  def __init__(self, sbp=None, **kwargs):
    if sbp:
      super( TestappPing,
             self).__init__(sbp.msg_id)
      self.payload = sbp.payload
    else:
      super( TestappPing, self).__init__()
      self.msg_id = SBP_TESTAPP_PING

  def __repr__(self):
    return fmt_repr(self)

  @staticmethod
  def from_json(s):
    """Given a JSON-encoded string s, build a message object.

    """
    d = json.loads(s)
    return TestappPing.from_json_dict(d)

  @staticmethod
  def from_json_dict(d):
    sbp = SBP.from_json_dict(d)
    return TestappPing(sbp, **d)

 
    
SBP_TESTAPP_PONG = 0x0069
class TestappPong(SBP):
  """SBP class for message TESTAPP_PONG (0x0069).

  You can have TESTAPP_PONG inherit its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  This message is a reply to the TESTAPP_PING message.


  """
  __slots__ = []

  def __init__(self, sbp=None, **kwargs):
    if sbp:
      super( TestappPong,
             self).__init__(sbp.msg_id)
      self.payload = sbp.payload
    else:
      super( TestappPong, self).__init__()
      self.msg_id = SBP_TESTAPP_PONG

  def __repr__(self):
    return fmt_repr(self)

  @staticmethod
  def from_json(s):
    """Given a JSON-encoded string s, build a message object.

    """
    d = json.loads(s)
    return TestappPong.from_json_dict(d)

  @staticmethod
  def from_json_dict(d):
    sbp = SBP.from_json_dict(d)
    return TestappPong(sbp, **d)

 
    
SBP_TESTAPP_SET_COUNTER = 0x0070
class TestappSetCounter(SBP):
  """SBP class for message TESTAPP_SET_COUNTER (0x0070).

  You can have TESTAPP_SET_COUNTER inherit its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  This message allows updating the testapp internal counter.
The reply message type is TESTAPP_SET_COUNTER.


  Parameters
  ----------
  sbp : SBP
    SBP parent object to inherit from.
  counter_value : int
    Updated counter value.
  sender : int
    Optional sender ID, defaults to SENDER_ID (see sbp/msg.py).

  """
  _parser = Struct("TestappSetCounter",
                   ULInt16('counter_value'),)
  __slots__ = [
               'counter_value',
              ]

  def __init__(self, sbp=None, **kwargs):
    if sbp:
      super( TestappSetCounter,
             self).__init__(sbp.msg_id)
      self.from_binary(sbp.payload)
    else:
      super( TestappSetCounter, self).__init__()
      self.msg_id = SBP_TESTAPP_SET_COUNTER
      self.counter_value = kwargs.pop('counter_value')

  def __repr__(self):
    return fmt_repr(self)

  @staticmethod
  def from_json(s):
    """Given a JSON-encoded string s, build a message object.

    """
    d = json.loads(s)
    return TestappSetCounter.from_json_dict(d)

  @staticmethod
  def from_json_dict(d):
    sbp = SBP.from_json_dict(d)
    return TestappSetCounter(sbp, **d)

 
  def from_binary(self, d):
    """Given a binary payload d, update the appropriate payload fields of
    the message.

    """
    p = TestappSetCounter._parser.parse(d)
    for n in self.__class__.__slots__:
      setattr(self, n, getattr(p, n))

  def to_binary(self):
    """Produce a framed/packed SBP message.

    """
    c = containerize(exclude_fields(self))
    self.payload = TestappSetCounter._parser.build(c)
    return self.pack()

  def to_json_dict(self):
    self.to_binary()
    d = super( TestappSetCounter, self).to_json_dict()
    j = walk_json_dict(exclude_fields(self))
    d.update(j)
    return d
    
SBP_TESTAPP_GET_COUNTER = 0x0071
class TestappGetCounter(SBP):
  """SBP class for message TESTAPP_GET_COUNTER (0x0071).

  You can have TESTAPP_GET_COUNTER inherit its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  This message commands the testapp to reply with its
internal counter value. The reply message type is
TESTAPP_SET_COUNTER.


  """
  __slots__ = []

  def __init__(self, sbp=None, **kwargs):
    if sbp:
      super( TestappGetCounter,
             self).__init__(sbp.msg_id)
      self.payload = sbp.payload
    else:
      super( TestappGetCounter, self).__init__()
      self.msg_id = SBP_TESTAPP_GET_COUNTER

  def __repr__(self):
    return fmt_repr(self)

  @staticmethod
  def from_json(s):
    """Given a JSON-encoded string s, build a message object.

    """
    d = json.loads(s)
    return TestappGetCounter.from_json_dict(d)

  @staticmethod
  def from_json_dict(d):
    sbp = SBP.from_json_dict(d)
    return TestappGetCounter(sbp, **d)

 
    
SBP_TESTAPP_SET_MANY = 0x0072
class TestappSetMany(SBP):
  """SBP class for message TESTAPP_SET_MANY (0x0072).

  You can have TESTAPP_SET_MANY inherit its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  This message demonstrates many fields.


  Parameters
  ----------
  sbp : SBP
    SBP parent object to inherit from.
  a : int
    unsigned 8-bit value
  b : int
    unsigned 16-bit value.
  c : float
    floating point value
  d : double
    double precision floating point value
  e : int
    signed 32-bit value
  f : string
    a variable length string!!
  sender : int
    Optional sender ID, defaults to SENDER_ID (see sbp/msg.py).

  """
  _parser = Struct("TestappSetMany",
                   ULInt8('a'),
                   ULInt16('b'),
                   LFloat32('c'),
                   LFloat64('d'),
                   SLInt32('e'),
                   greedy_string('f'),)
  __slots__ = [
               'a',
               'b',
               'c',
               'd',
               'e',
               'f',
              ]

  def __init__(self, sbp=None, **kwargs):
    if sbp:
      super( TestappSetMany,
             self).__init__(sbp.msg_id)
      self.from_binary(sbp.payload)
    else:
      super( TestappSetMany, self).__init__()
      self.msg_id = SBP_TESTAPP_SET_MANY
      self.a = kwargs.pop('a')
      self.b = kwargs.pop('b')
      self.c = kwargs.pop('c')
      self.d = kwargs.pop('d')
      self.e = kwargs.pop('e')
      self.f = kwargs.pop('f')

  def __repr__(self):
    return fmt_repr(self)

  @staticmethod
  def from_json(s):
    """Given a JSON-encoded string s, build a message object.

    """
    d = json.loads(s)
    return TestappSetMany.from_json_dict(d)

  @staticmethod
  def from_json_dict(d):
    sbp = SBP.from_json_dict(d)
    return TestappSetMany(sbp, **d)

 
  def from_binary(self, d):
    """Given a binary payload d, update the appropriate payload fields of
    the message.

    """
    p = TestappSetMany._parser.parse(d)
    for n in self.__class__.__slots__:
      setattr(self, n, getattr(p, n))

  def to_binary(self):
    """Produce a framed/packed SBP message.

    """
    c = containerize(exclude_fields(self))
    self.payload = TestappSetMany._parser.build(c)
    return self.pack()

  def to_json_dict(self):
    self.to_binary()
    d = super( TestappSetMany, self).to_json_dict()
    j = walk_json_dict(exclude_fields(self))
    d.update(j)
    return d
    
SBP_TESTAPP_FIXED_ARRAY_MSG = 0x0073
class TestappFixedArrayMsg(SBP):
  """SBP class for message TESTAPP_FIXED_ARRAY_MSG (0x0073).

  You can have TESTAPP_FIXED_ARRAY_MSG inherit its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  This message demonstrates a fixed-length array field.


  Parameters
  ----------
  sbp : SBP
    SBP parent object to inherit from.
  vector : array
    A fixed length integer array
  sender : int
    Optional sender ID, defaults to SENDER_ID (see sbp/msg.py).

  """
  _parser = Struct("TestappFixedArrayMsg",
                   Struct('vector', Array(5, SLInt16('vector'))),)
  __slots__ = [
               'vector',
              ]

  def __init__(self, sbp=None, **kwargs):
    if sbp:
      super( TestappFixedArrayMsg,
             self).__init__(sbp.msg_id)
      self.from_binary(sbp.payload)
    else:
      super( TestappFixedArrayMsg, self).__init__()
      self.msg_id = SBP_TESTAPP_FIXED_ARRAY_MSG
      self.vector = kwargs.pop('vector')

  def __repr__(self):
    return fmt_repr(self)

  @staticmethod
  def from_json(s):
    """Given a JSON-encoded string s, build a message object.

    """
    d = json.loads(s)
    return TestappFixedArrayMsg.from_json_dict(d)

  @staticmethod
  def from_json_dict(d):
    sbp = SBP.from_json_dict(d)
    return TestappFixedArrayMsg(sbp, **d)

 
  def from_binary(self, d):
    """Given a binary payload d, update the appropriate payload fields of
    the message.

    """
    p = TestappFixedArrayMsg._parser.parse(d)
    for n in self.__class__.__slots__:
      setattr(self, n, getattr(p, n))

  def to_binary(self):
    """Produce a framed/packed SBP message.

    """
    c = containerize(exclude_fields(self))
    self.payload = TestappFixedArrayMsg._parser.build(c)
    return self.pack()

  def to_json_dict(self):
    self.to_binary()
    d = super( TestappFixedArrayMsg, self).to_json_dict()
    j = walk_json_dict(exclude_fields(self))
    d.update(j)
    return d
    
SBP_TESTAPP_VARIABLE_ARRAY_MSG = 0x0074
class TestappVariableArrayMsg(SBP):
  """SBP class for message TESTAPP_VARIABLE_ARRAY_MSG (0x0074).

  You can have TESTAPP_VARIABLE_ARRAY_MSG inherit its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  This message demonstrates a variable length array field.


  Parameters
  ----------
  sbp : SBP
    SBP parent object to inherit from.
  vector : array
    A variable length byte array
  sender : int
    Optional sender ID, defaults to SENDER_ID (see sbp/msg.py).

  """
  _parser = Struct("TestappVariableArrayMsg",
                   OptionalGreedyRange(ULInt8('vector')),)
  __slots__ = [
               'vector',
              ]

  def __init__(self, sbp=None, **kwargs):
    if sbp:
      super( TestappVariableArrayMsg,
             self).__init__(sbp.msg_id)
      self.from_binary(sbp.payload)
    else:
      super( TestappVariableArrayMsg, self).__init__()
      self.msg_id = SBP_TESTAPP_VARIABLE_ARRAY_MSG
      self.vector = kwargs.pop('vector')

  def __repr__(self):
    return fmt_repr(self)

  @staticmethod
  def from_json(s):
    """Given a JSON-encoded string s, build a message object.

    """
    d = json.loads(s)
    return TestappVariableArrayMsg.from_json_dict(d)

  @staticmethod
  def from_json_dict(d):
    sbp = SBP.from_json_dict(d)
    return TestappVariableArrayMsg(sbp, **d)

 
  def from_binary(self, d):
    """Given a binary payload d, update the appropriate payload fields of
    the message.

    """
    p = TestappVariableArrayMsg._parser.parse(d)
    for n in self.__class__.__slots__:
      setattr(self, n, getattr(p, n))

  def to_binary(self):
    """Produce a framed/packed SBP message.

    """
    c = containerize(exclude_fields(self))
    self.payload = TestappVariableArrayMsg._parser.build(c)
    return self.pack()

  def to_json_dict(self):
    self.to_binary()
    d = super( TestappVariableArrayMsg, self).to_json_dict()
    j = walk_json_dict(exclude_fields(self))
    d.update(j)
    return d
    
SBP_TESTAPP_STATE = 0x0075
class TestappState(SBP):
  """SBP class for message TESTAPP_STATE (0x0075).

  You can have TESTAPP_STATE inherit its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  Piksi message about the state of UART0.

  Parameters
  ----------
  sbp : SBP
    SBP parent object to inherit from.
  channels : testapp_channel
    Example channel data.
  info : string
    Info string of length 8 bytes.
  remaining_channel_array : array
    Array of testapp_channel structs
  sender : int
    Optional sender ID, defaults to SENDER_ID (see sbp/msg.py).

  """
  _parser = Struct("TestappState",
                   Struct('channels', testapp_channel._parser),
                   String('info', 8),
                   Struct('remaining_channel_array', Array(5, Struct('remaining_channel_array', testapp_channel._parser))),)
  __slots__ = [
               'channels',
               'info',
               'remaining_channel_array',
              ]

  def __init__(self, sbp=None, **kwargs):
    if sbp:
      super( TestappState,
             self).__init__(sbp.msg_id)
      self.from_binary(sbp.payload)
    else:
      super( TestappState, self).__init__()
      self.msg_id = SBP_TESTAPP_STATE
      self.channels = kwargs.pop('channels')
      self.info = kwargs.pop('info')
      self.remaining_channel_array = kwargs.pop('remaining_channel_array')

  def __repr__(self):
    return fmt_repr(self)

  @staticmethod
  def from_json(s):
    """Given a JSON-encoded string s, build a message object.

    """
    d = json.loads(s)
    return TestappState.from_json_dict(d)

  @staticmethod
  def from_json_dict(d):
    sbp = SBP.from_json_dict(d)
    return TestappState(sbp, **d)

 
  def from_binary(self, d):
    """Given a binary payload d, update the appropriate payload fields of
    the message.

    """
    p = TestappState._parser.parse(d)
    for n in self.__class__.__slots__:
      setattr(self, n, getattr(p, n))

  def to_binary(self):
    """Produce a framed/packed SBP message.

    """
    c = containerize(exclude_fields(self))
    self.payload = TestappState._parser.build(c)
    return self.pack()

  def to_json_dict(self):
    self.to_binary()
    d = super( TestappState, self).to_json_dict()
    j = walk_json_dict(exclude_fields(self))
    d.update(j)
    return d
    

msg_classes = {
  0x0068: TestappPing,
  0x0069: TestappPong,
  0x0070: TestappSetCounter,
  0x0071: TestappGetCounter,
  0x0072: TestappSetMany,
  0x0073: TestappFixedArrayMsg,
  0x0074: TestappVariableArrayMsg,
  0x0075: TestappState,
}