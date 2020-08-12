# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: remote_env.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='remote_env.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x10remote_env.proto\x1a\x1bgoogle/protobuf/empty.proto\"9\n\x06Spaces\x12\x19\n\x11observation_space\x18\x01 \x01(\x0c\x12\x14\n\x0c\x61\x63tion_space\x18\x02 \x01(\x0c\"\\\n\x19ObservationRewardDoneInfo\x12\x13\n\x0bobservation\x18\x01 \x01(\x0c\x12\x0e\n\x06reward\x18\x02 \x01(\x02\x12\x0c\n\x04\x64one\x18\x03 \x01(\x08\x12\x0c\n\x04info\x18\x04 \x01(\x0c\"\"\n\x0bObservation\x12\x13\n\x0bobservation\x18\x01 \x01(\x0c\"\x18\n\x06\x41\x63tion\x12\x0e\n\x06\x61\x63tion\x18\x01 \x01(\x0c\"\x16\n\x05Image\x12\r\n\x05image\x18\x01 \x01(\x0c\"\x14\n\x04Seed\x12\x0c\n\x04seed\x18\x01 \x01(\x03\x32\xf0\x02\n\tRemoteEnv\x12=\n\tHeartBeat\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x00\x12.\n\tGetSpaces\x12\x16.google.protobuf.Empty\x1a\x07.Spaces\"\x00\x12*\n\x07SetSeed\x12\x05.Seed\x1a\x16.google.protobuf.Empty\"\x00\x12/\n\x05Reset\x12\x16.google.protobuf.Empty\x1a\x0c.Observation\"\x00\x12-\n\x04Step\x12\x07.Action\x1a\x1a.ObservationRewardDoneInfo\"\x00\x12*\n\x06Render\x12\x16.google.protobuf.Empty\x1a\x06.Image\"\x00\x12<\n\x08Shutdown\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_SPACES = _descriptor.Descriptor(
  name='Spaces',
  full_name='Spaces',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='observation_space', full_name='Spaces.observation_space', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action_space', full_name='Spaces.action_space', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=49,
  serialized_end=106,
)


_OBSERVATIONREWARDDONEINFO = _descriptor.Descriptor(
  name='ObservationRewardDoneInfo',
  full_name='ObservationRewardDoneInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='observation', full_name='ObservationRewardDoneInfo.observation', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reward', full_name='ObservationRewardDoneInfo.reward', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='done', full_name='ObservationRewardDoneInfo.done', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='info', full_name='ObservationRewardDoneInfo.info', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=108,
  serialized_end=200,
)


_OBSERVATION = _descriptor.Descriptor(
  name='Observation',
  full_name='Observation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='observation', full_name='Observation.observation', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=202,
  serialized_end=236,
)


_ACTION = _descriptor.Descriptor(
  name='Action',
  full_name='Action',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='Action.action', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=238,
  serialized_end=262,
)


_IMAGE = _descriptor.Descriptor(
  name='Image',
  full_name='Image',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='image', full_name='Image.image', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=264,
  serialized_end=286,
)


_SEED = _descriptor.Descriptor(
  name='Seed',
  full_name='Seed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seed', full_name='Seed.seed', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=288,
  serialized_end=308,
)

DESCRIPTOR.message_types_by_name['Spaces'] = _SPACES
DESCRIPTOR.message_types_by_name['ObservationRewardDoneInfo'] = _OBSERVATIONREWARDDONEINFO
DESCRIPTOR.message_types_by_name['Observation'] = _OBSERVATION
DESCRIPTOR.message_types_by_name['Action'] = _ACTION
DESCRIPTOR.message_types_by_name['Image'] = _IMAGE
DESCRIPTOR.message_types_by_name['Seed'] = _SEED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Spaces = _reflection.GeneratedProtocolMessageType('Spaces', (_message.Message,), {
  'DESCRIPTOR' : _SPACES,
  '__module__' : 'remote_env_pb2'
  # @@protoc_insertion_point(class_scope:Spaces)
  })
_sym_db.RegisterMessage(Spaces)

ObservationRewardDoneInfo = _reflection.GeneratedProtocolMessageType('ObservationRewardDoneInfo', (_message.Message,), {
  'DESCRIPTOR' : _OBSERVATIONREWARDDONEINFO,
  '__module__' : 'remote_env_pb2'
  # @@protoc_insertion_point(class_scope:ObservationRewardDoneInfo)
  })
_sym_db.RegisterMessage(ObservationRewardDoneInfo)

Observation = _reflection.GeneratedProtocolMessageType('Observation', (_message.Message,), {
  'DESCRIPTOR' : _OBSERVATION,
  '__module__' : 'remote_env_pb2'
  # @@protoc_insertion_point(class_scope:Observation)
  })
_sym_db.RegisterMessage(Observation)

Action = _reflection.GeneratedProtocolMessageType('Action', (_message.Message,), {
  'DESCRIPTOR' : _ACTION,
  '__module__' : 'remote_env_pb2'
  # @@protoc_insertion_point(class_scope:Action)
  })
_sym_db.RegisterMessage(Action)

Image = _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), {
  'DESCRIPTOR' : _IMAGE,
  '__module__' : 'remote_env_pb2'
  # @@protoc_insertion_point(class_scope:Image)
  })
_sym_db.RegisterMessage(Image)

Seed = _reflection.GeneratedProtocolMessageType('Seed', (_message.Message,), {
  'DESCRIPTOR' : _SEED,
  '__module__' : 'remote_env_pb2'
  # @@protoc_insertion_point(class_scope:Seed)
  })
_sym_db.RegisterMessage(Seed)



_REMOTEENV = _descriptor.ServiceDescriptor(
  name='RemoteEnv',
  full_name='RemoteEnv',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=311,
  serialized_end=679,
  methods=[
  _descriptor.MethodDescriptor(
    name='HeartBeat',
    full_name='RemoteEnv.HeartBeat',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetSpaces',
    full_name='RemoteEnv.GetSpaces',
    index=1,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_SPACES,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetSeed',
    full_name='RemoteEnv.SetSeed',
    index=2,
    containing_service=None,
    input_type=_SEED,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Reset',
    full_name='RemoteEnv.Reset',
    index=3,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_OBSERVATION,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Step',
    full_name='RemoteEnv.Step',
    index=4,
    containing_service=None,
    input_type=_ACTION,
    output_type=_OBSERVATIONREWARDDONEINFO,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Render',
    full_name='RemoteEnv.Render',
    index=5,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_IMAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Shutdown',
    full_name='RemoteEnv.Shutdown',
    index=6,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_REMOTEENV)

DESCRIPTOR.services_by_name['RemoteEnv'] = _REMOTEENV

# @@protoc_insertion_point(module_scope)