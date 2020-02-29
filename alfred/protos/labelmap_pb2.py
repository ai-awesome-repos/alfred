# -*- coding: utf-8 -*-
#
# Copyright (c) 2020 JinTian.
#
# This file is part of alfred
# (see http://jinfagang.github.io).
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: labelmap.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='labelmap.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x0elabelmap.proto\"M\n\x0cLabelMapItem\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\x05\x12\n\n\x02id\x18\x04 \x01(\x05\x12\x14\n\x0c\x64isplay_name\x18\x03 \x01(\t\"\'\n\x08LabelMap\x12\x1b\n\x04item\x18\x01 \x03(\x0b\x32\r.LabelMapItem')
)




_LABELMAPITEM = _descriptor.Descriptor(
  name='LabelMapItem',
  full_name='LabelMapItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='LabelMapItem.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='label', full_name='LabelMapItem.label', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='LabelMapItem.id', index=2,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='LabelMapItem.display_name', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=95,
)


_LABELMAP = _descriptor.Descriptor(
  name='LabelMap',
  full_name='LabelMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='LabelMap.item', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=97,
  serialized_end=136,
)

_LABELMAP.fields_by_name['item'].message_type = _LABELMAPITEM
DESCRIPTOR.message_types_by_name['LabelMapItem'] = _LABELMAPITEM
DESCRIPTOR.message_types_by_name['LabelMap'] = _LABELMAP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LabelMapItem = _reflection.GeneratedProtocolMessageType('LabelMapItem', (_message.Message,), {
  'DESCRIPTOR' : _LABELMAPITEM,
  '__module__' : 'labelmap_pb2'
  # @@protoc_insertion_point(class_scope:LabelMapItem)
  })
_sym_db.RegisterMessage(LabelMapItem)

LabelMap = _reflection.GeneratedProtocolMessageType('LabelMap', (_message.Message,), {
  'DESCRIPTOR' : _LABELMAP,
  '__module__' : 'labelmap_pb2'
  # @@protoc_insertion_point(class_scope:LabelMap)
  })
_sym_db.RegisterMessage(LabelMap)


# @@protoc_insertion_point(module_scope)
