# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='distributions/schema.proto',
  package='distributions',
  serialized_pb='\n\x1a\x64istributions/schema.proto\x12\rdistributions\"H\n\x03Row\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08\x62ooleans\x18\x02 \x03(\x08\x12\x14\n\x0c\x63\x61tegoricals\x18\x03 \x03(\r\x12\r\n\x05reals\x18\x04 \x03(\x02')




_ROW = descriptor.Descriptor(
  name='Row',
  full_name='distributions.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='distributions.Row.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='booleans', full_name='distributions.Row.booleans', index=1,
      number=2, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='categoricals', full_name='distributions.Row.categoricals', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='reals', full_name='distributions.Row.reals', index=3,
      number=4, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
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
  extension_ranges=[],
  serialized_start=45,
  serialized_end=117,
)

DESCRIPTOR.message_types_by_name['Row'] = _ROW

class Row(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ROW
  
  # @@protoc_insertion_point(class_scope:distributions.Row)

# @@protoc_insertion_point(module_scope)
