# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: foxglove/Pose.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from foxglove import Quaternion_pb2 as foxglove_dot_Quaternion__pb2
from foxglove import Vector3_pb2 as foxglove_dot_Vector3__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x66oxglove/Pose.proto\x12\x08\x66oxglove\x1a\x19\x66oxglove/Quaternion.proto\x1a\x16\x66oxglove/Vector3.proto\"V\n\x04Pose\x12#\n\x08position\x18\x01 \x01(\x0b\x32\x11.foxglove.Vector3\x12)\n\x0borientation\x18\x02 \x01(\x0b\x32\x14.foxglove.Quaternionb\x06proto3')



_POSE = DESCRIPTOR.message_types_by_name['Pose']
Pose = _reflection.GeneratedProtocolMessageType('Pose', (_message.Message,), {
  'DESCRIPTOR' : _POSE,
  '__module__' : 'foxglove.Pose_pb2'
  # @@protoc_insertion_point(class_scope:foxglove.Pose)
  })
_sym_db.RegisterMessage(Pose)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _POSE._serialized_start=84
  _POSE._serialized_end=170
# @@protoc_insertion_point(module_scope)