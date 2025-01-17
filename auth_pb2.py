# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: auth.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'auth.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import common_pb2 as common__pb2
import enum_pb2 as enum__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nauth.proto\x12\x04\x61uth\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x0c\x63ommon.proto\x1a\nenum.proto\"+\n\x12GetSentenceRequest\x12\x15\n\rwalletAddress\x18\x01 \x01(\t\"\x99\x01\n\x10GetSentenceReply\x12%\n\x06result\x18\x01 \x01(\x0b\x32\x15.common.RequestResult\x12\x15\n\x08sentence\x18\x02 \x01(\tH\x00\x88\x01\x01\x12/\n\x06\x65xpire\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x01\x88\x01\x01\x42\x0b\n\t_sentenceB\t\n\x07_expire\"\xef\x01\n\x17\x41uthByWalletSignRequest\x12\x15\n\rwalletAddress\x18\x01 \x01(\t\x12\x16\n\x0esignedSentence\x18\x02 \x01(\t\x12!\n\x05\x63hain\x18\x03 \x01(\x0e\x32\x12.enumeration.Chain\x12\x19\n\x0creferralCode\x18\x04 \x01(\tH\x00\x88\x01\x01\x12\x14\n\x07mfaCode\x18\x05 \x01(\tH\x01\x88\x01\x01\x12\x1e\n\x11\x61voidRegistration\x18\x06 \x01(\x08H\x02\x88\x01\x01\x42\x0f\n\r_referralCodeB\n\n\x08_mfaCodeB\x14\n\x12_avoidRegistration\"\xb0\x01\n\tAuthReply\x12%\n\x06result\x18\x01 \x01(\x0b\x32\x15.common.RequestResult\x12\x15\n\x08newTerms\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x17\n\nseedPhrase\x18\x03 \x01(\tH\x01\x88\x01\x01\x12&\n\x05token\x18\x04 \x01(\x0b\x32\x12.common.AuthTokensH\x02\x88\x01\x01\x42\x0b\n\t_newTermsB\r\n\x0b_seedPhraseB\x08\n\x06_token\"\xc7\x01\n\x15\x41uthByTelegramRequest\x12*\n\rtelegramReply\x18\x01 \x01(\x0b\x32\x13.auth.TelegramReply\x12\x19\n\x0creferralCode\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x14\n\x07mfaCode\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x1e\n\x11\x61voidRegistration\x18\x04 \x01(\x08H\x02\x88\x01\x01\x42\x0f\n\r_referralCodeB\n\n\x08_mfaCodeB\x14\n\x12_avoidRegistration\"\xee\x01\n\x11\x41uthBySeedRequest\x12\x12\n\nseedPhrase\x18\x01 \x01(\t\x12\x19\n\x0creferralCode\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x14\n\x07mfaCode\x18\x03 \x01(\tH\x01\x88\x01\x01\x12/\n\rtelegramReply\x18\x04 \x01(\x0b\x32\x13.auth.TelegramReplyH\x02\x88\x01\x01\x12\x1e\n\x11\x61voidRegistration\x18\x05 \x01(\x08H\x03\x88\x01\x01\x42\x0f\n\r_referralCodeB\n\n\x08_mfaCodeB\x10\n\x0e_telegramReplyB\x14\n\x12_avoidRegistration\":\n\x17NewTermsAcceptedRequest\x12\x1f\n\x17isUserAgreementAccepted\x18\x01 \x01(\x08\":\n\x19SeedPhraseAcceptedRequest\x12\x1d\n\x15isSeedPhraseWasStored\x18\x01 \x01(\x08\"\xa3\x01\n\x11\x41uthByCodeRequest\x12\x15\n\rshortLifeCode\x18\x01 \x01(\t\x12/\n\rtelegramReply\x18\x02 \x01(\x0b\x32\x13.auth.TelegramReplyH\x00\x88\x01\x01\x12\x1e\n\x11\x61voidRegistration\x18\x03 \x01(\x08H\x01\x88\x01\x01\x42\x10\n\x0e_telegramReplyB\x14\n\x12_avoidRegistration\"0\n\x18RefreshAuthTokensRequest\x12\x14\n\x0crefreshToken\x18\x01 \x01(\t\"l\n\x15GetShortLifeCodeReply\x12%\n\x06result\x18\x01 \x01(\x0b\x32\x15.common.RequestResult\x12\x1a\n\rshortLifeCode\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x10\n\x0e_shortLifeCode\"\x84\x01\n\rTelegramReply\x12=\n\rtelegramReply\x18\x01 \x03(\x0b\x32&.auth.TelegramReply.TelegramReplyEntry\x1a\x34\n\x12TelegramReplyEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32\xe3\x04\n\x0b\x41uthService\x12?\n\x0bGetSentence\x12\x18.auth.GetSentenceRequest\x1a\x16.auth.GetSentenceReply\x12\x42\n\x10\x41uthByWalletSign\x12\x1d.auth.AuthByWalletSignRequest\x1a\x0f.auth.AuthReply\x12>\n\x0e\x41uthByTelegram\x12\x1b.auth.AuthByTelegramRequest\x1a\x0f.auth.AuthReply\x12\x36\n\nAuthBySeed\x12\x17.auth.AuthBySeedRequest\x1a\x0f.auth.AuthReply\x12\x45\n\x10NewTermsAccepted\x12\x1d.auth.NewTermsAcceptedRequest\x1a\x12.common.EmptyReply\x12I\n\x12SeedPhraseAccepted\x12\x1f.auth.SeedPhraseAcceptedRequest\x1a\x12.common.EmptyReply\x12\x36\n\nAuthByCode\x12\x17.auth.AuthByCodeRequest\x1a\x0f.auth.AuthReply\x12\x44\n\x11RefreshAuthTokens\x12\x1e.auth.RefreshAuthTokensRequest\x1a\x0f.auth.AuthReply\x12G\n\x10GetShortLifeCode\x12\x16.google.protobuf.Empty\x1a\x1b.auth.GetShortLifeCodeReplyB\x1f\xaa\x02\x1cTT.Gateway.WebApi.Proto.Authb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'auth_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\034TT.Gateway.WebApi.Proto.Auth'
  _globals['_TELEGRAMREPLY_TELEGRAMREPLYENTRY']._loaded_options = None
  _globals['_TELEGRAMREPLY_TELEGRAMREPLYENTRY']._serialized_options = b'8\001'
  _globals['_GETSENTENCEREQUEST']._serialized_start=108
  _globals['_GETSENTENCEREQUEST']._serialized_end=151
  _globals['_GETSENTENCEREPLY']._serialized_start=154
  _globals['_GETSENTENCEREPLY']._serialized_end=307
  _globals['_AUTHBYWALLETSIGNREQUEST']._serialized_start=310
  _globals['_AUTHBYWALLETSIGNREQUEST']._serialized_end=549
  _globals['_AUTHREPLY']._serialized_start=552
  _globals['_AUTHREPLY']._serialized_end=728
  _globals['_AUTHBYTELEGRAMREQUEST']._serialized_start=731
  _globals['_AUTHBYTELEGRAMREQUEST']._serialized_end=930
  _globals['_AUTHBYSEEDREQUEST']._serialized_start=933
  _globals['_AUTHBYSEEDREQUEST']._serialized_end=1171
  _globals['_NEWTERMSACCEPTEDREQUEST']._serialized_start=1173
  _globals['_NEWTERMSACCEPTEDREQUEST']._serialized_end=1231
  _globals['_SEEDPHRASEACCEPTEDREQUEST']._serialized_start=1233
  _globals['_SEEDPHRASEACCEPTEDREQUEST']._serialized_end=1291
  _globals['_AUTHBYCODEREQUEST']._serialized_start=1294
  _globals['_AUTHBYCODEREQUEST']._serialized_end=1457
  _globals['_REFRESHAUTHTOKENSREQUEST']._serialized_start=1459
  _globals['_REFRESHAUTHTOKENSREQUEST']._serialized_end=1507
  _globals['_GETSHORTLIFECODEREPLY']._serialized_start=1509
  _globals['_GETSHORTLIFECODEREPLY']._serialized_end=1617
  _globals['_TELEGRAMREPLY']._serialized_start=1620
  _globals['_TELEGRAMREPLY']._serialized_end=1752
  _globals['_TELEGRAMREPLY_TELEGRAMREPLYENTRY']._serialized_start=1700
  _globals['_TELEGRAMREPLY_TELEGRAMREPLYENTRY']._serialized_end=1752
  _globals['_AUTHSERVICE']._serialized_start=1755
  _globals['_AUTHSERVICE']._serialized_end=2366
# @@protoc_insertion_point(module_scope)
