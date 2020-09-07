# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fl_comm_libs/proto/dc_agent.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='fl_comm_libs/proto/dc_agent.proto',
  package='jdfl',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n!fl_comm_libs/proto/dc_agent.proto\x12\x04jdfl\"+\n\x15\x46\x65tchDataBlockRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\"\x92\x02\n\rDataBlockMeta\x12\x10\n\x08\x62lock_id\x18\x01 \x01(\t\x12\x14\n\x0cpartition_id\x18\x02 \x01(\x05\x12\x14\n\x0c\x66ile_version\x18\x03 \x01(\x05\x12\x12\n\nstart_time\x18\x04 \x01(\x03\x12\x10\n\x08\x65nd_time\x18\x05 \x01(\x03\x12\x13\n\x0b\x65xample_ids\x18\x06 \x03(\x0c\x12\x1a\n\x12leader_start_index\x18\x07 \x01(\x03\x12\x18\n\x10leader_end_index\x18\x08 \x01(\x03\x12\x1c\n\x14\x66ollower_start_index\x18\t \x01(\x03\x12\x1a\n\x12\x66ollower_end_index\x18\n \x01(\x03\x12\x18\n\x10\x64\x61ta_block_index\x18\x0b \x01(\x03\"^\n\rDataBlockInfo\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x11\n\tdata_path\x18\x02 \x01(\t\x12&\n\tmeta_info\x18\x03 \x01(\x0b\x32\x13.jdfl.DataBlockMeta\"\x83\x01\n\x16\x46\x65tchDataBlockResponse\x12%\n\x0bstatus_code\x18\x01 \x01(\x0e\x32\x10.jdfl.StatusCode\x12\x1c\n\x14status_error_message\x18\x02 \x01(\t\x12$\n\x07\x64\x62_info\x18\x03 \x01(\x0b\x32\x13.jdfl.DataBlockInfo*S\n\nStatusCode\x12\x06\n\x02OK\x10\x00\x12\r\n\tNOT_READY\x10\x01\x12\x0c\n\x08\x46INISHED\x10\x02\x12\r\n\tNOT_FOUND\x10\x03\x12\x11\n\rERROR_ABORTED\x10\x04\x32\x66\n\x15\x44\x61taBlockQueryService\x12M\n\x0eQueryDataBlock\x12\x1b.jdfl.FetchDataBlockRequest\x1a\x1c.jdfl.FetchDataBlockResponse\"\x00\x62\x06proto3')
)

_STATUSCODE = _descriptor.EnumDescriptor(
  name='StatusCode',
  full_name='jdfl.StatusCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_READY', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FINISHED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_FOUND', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_ABORTED', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=595,
  serialized_end=678,
)
_sym_db.RegisterEnumDescriptor(_STATUSCODE)

StatusCode = enum_type_wrapper.EnumTypeWrapper(_STATUSCODE)
OK = 0
NOT_READY = 1
FINISHED = 2
NOT_FOUND = 3
ERROR_ABORTED = 4



_FETCHDATABLOCKREQUEST = _descriptor.Descriptor(
  name='FetchDataBlockRequest',
  full_name='jdfl.FetchDataBlockRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='jdfl.FetchDataBlockRequest.request_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=86,
)


_DATABLOCKMETA = _descriptor.Descriptor(
  name='DataBlockMeta',
  full_name='jdfl.DataBlockMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='block_id', full_name='jdfl.DataBlockMeta.block_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partition_id', full_name='jdfl.DataBlockMeta.partition_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_version', full_name='jdfl.DataBlockMeta.file_version', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='jdfl.DataBlockMeta.start_time', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='jdfl.DataBlockMeta.end_time', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='example_ids', full_name='jdfl.DataBlockMeta.example_ids', index=5,
      number=6, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='leader_start_index', full_name='jdfl.DataBlockMeta.leader_start_index', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='leader_end_index', full_name='jdfl.DataBlockMeta.leader_end_index', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='follower_start_index', full_name='jdfl.DataBlockMeta.follower_start_index', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='follower_end_index', full_name='jdfl.DataBlockMeta.follower_end_index', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_block_index', full_name='jdfl.DataBlockMeta.data_block_index', index=10,
      number=11, type=3, cpp_type=2, label=1,
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
  serialized_start=89,
  serialized_end=363,
)


_DATABLOCKINFO = _descriptor.Descriptor(
  name='DataBlockInfo',
  full_name='jdfl.DataBlockInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='jdfl.DataBlockInfo.request_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_path', full_name='jdfl.DataBlockInfo.data_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='meta_info', full_name='jdfl.DataBlockInfo.meta_info', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=365,
  serialized_end=459,
)


_FETCHDATABLOCKRESPONSE = _descriptor.Descriptor(
  name='FetchDataBlockResponse',
  full_name='jdfl.FetchDataBlockResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status_code', full_name='jdfl.FetchDataBlockResponse.status_code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status_error_message', full_name='jdfl.FetchDataBlockResponse.status_error_message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='db_info', full_name='jdfl.FetchDataBlockResponse.db_info', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=462,
  serialized_end=593,
)

_DATABLOCKINFO.fields_by_name['meta_info'].message_type = _DATABLOCKMETA
_FETCHDATABLOCKRESPONSE.fields_by_name['status_code'].enum_type = _STATUSCODE
_FETCHDATABLOCKRESPONSE.fields_by_name['db_info'].message_type = _DATABLOCKINFO
DESCRIPTOR.message_types_by_name['FetchDataBlockRequest'] = _FETCHDATABLOCKREQUEST
DESCRIPTOR.message_types_by_name['DataBlockMeta'] = _DATABLOCKMETA
DESCRIPTOR.message_types_by_name['DataBlockInfo'] = _DATABLOCKINFO
DESCRIPTOR.message_types_by_name['FetchDataBlockResponse'] = _FETCHDATABLOCKRESPONSE
DESCRIPTOR.enum_types_by_name['StatusCode'] = _STATUSCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FetchDataBlockRequest = _reflection.GeneratedProtocolMessageType('FetchDataBlockRequest', (_message.Message,), {
  'DESCRIPTOR' : _FETCHDATABLOCKREQUEST,
  '__module__' : 'fl_comm_libs.proto.dc_agent_pb2'
  # @@protoc_insertion_point(class_scope:jdfl.FetchDataBlockRequest)
  })
_sym_db.RegisterMessage(FetchDataBlockRequest)

DataBlockMeta = _reflection.GeneratedProtocolMessageType('DataBlockMeta', (_message.Message,), {
  'DESCRIPTOR' : _DATABLOCKMETA,
  '__module__' : 'fl_comm_libs.proto.dc_agent_pb2'
  # @@protoc_insertion_point(class_scope:jdfl.DataBlockMeta)
  })
_sym_db.RegisterMessage(DataBlockMeta)

DataBlockInfo = _reflection.GeneratedProtocolMessageType('DataBlockInfo', (_message.Message,), {
  'DESCRIPTOR' : _DATABLOCKINFO,
  '__module__' : 'fl_comm_libs.proto.dc_agent_pb2'
  # @@protoc_insertion_point(class_scope:jdfl.DataBlockInfo)
  })
_sym_db.RegisterMessage(DataBlockInfo)

FetchDataBlockResponse = _reflection.GeneratedProtocolMessageType('FetchDataBlockResponse', (_message.Message,), {
  'DESCRIPTOR' : _FETCHDATABLOCKRESPONSE,
  '__module__' : 'fl_comm_libs.proto.dc_agent_pb2'
  # @@protoc_insertion_point(class_scope:jdfl.FetchDataBlockResponse)
  })
_sym_db.RegisterMessage(FetchDataBlockResponse)



_DATABLOCKQUERYSERVICE = _descriptor.ServiceDescriptor(
  name='DataBlockQueryService',
  full_name='jdfl.DataBlockQueryService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=680,
  serialized_end=782,
  methods=[
  _descriptor.MethodDescriptor(
    name='QueryDataBlock',
    full_name='jdfl.DataBlockQueryService.QueryDataBlock',
    index=0,
    containing_service=None,
    input_type=_FETCHDATABLOCKREQUEST,
    output_type=_FETCHDATABLOCKRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DATABLOCKQUERYSERVICE)

DESCRIPTOR.services_by_name['DataBlockQueryService'] = _DATABLOCKQUERYSERVICE

# @@protoc_insertion_point(module_scope)