# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: image_set.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='image_set.proto',
  package='artifacts.proto',
  syntax='proto3',
  serialized_pb=_b('\n\x0fimage_set.proto\x12\x0f\x61rtifacts.proto\"\x1e\n\x0eImageSetRecord\x12\x0c\n\x04path\x18\x01 \x01(\tb\x06proto3')
)




_IMAGESETRECORD = _descriptor.Descriptor(
  name='ImageSetRecord',
  full_name='artifacts.proto.ImageSetRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='artifacts.proto.ImageSetRecord.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=66,
)

DESCRIPTOR.message_types_by_name['ImageSetRecord'] = _IMAGESETRECORD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImageSetRecord = _reflection.GeneratedProtocolMessageType('ImageSetRecord', (_message.Message,), dict(
  DESCRIPTOR = _IMAGESETRECORD,
  __module__ = 'image_set_pb2'
  # @@protoc_insertion_point(class_scope:artifacts.proto.ImageSetRecord)
  ))
_sym_db.RegisterMessage(ImageSetRecord)


# @@protoc_insertion_point(module_scope)