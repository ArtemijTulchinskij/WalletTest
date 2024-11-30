# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: common.proto
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
    'common.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
import enum_pb2 as enum__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x63ommon.proto\x12\x06\x63ommon\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19google/protobuf/any.proto\x1a\nenum.proto\"\x98\x01\n\x0eGeneralRequest\x12\x11\n\trequestId\x18\x01 \x01(\t\x12%\n\x07message\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x13\n\x06method\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x1a\n\rauthorization\x18\x04 \x01(\tH\x01\x88\x01\x01\x42\t\n\x07_methodB\x10\n\x0e_authorization\"H\n\x0cGeneralReply\x12\x11\n\trequestId\x18\x01 \x01(\t\x12%\n\x07message\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\")\n\x12UnsubscribeRequest\x12\x13\n\x0bunsubscribe\x18\x01 \x01(\x08\"t\n\rRequestResult\x12\x11\n\tisSuccess\x18\x01 \x01(\x08\x12(\n\x06\x65rrors\x18\x02 \x03(\x0b\x32\x18.common.ErrorDescription\x12\x17\n\nerrorTrace\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\r\n\x0b_errorTrace\"3\n\nEmptyReply\x12%\n\x06result\x18\x01 \x01(\x0b\x32\x15.common.RequestResult\"p\n\x10\x45rrorDescription\x12\x0c\n\x04\x63ode\x18\x01 \x01(\r\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0f\n\x07\x64\x65tails\x18\x03 \x01(\t\x12,\n\rlocalizedText\x18\x04 \x03(\x0b\x32\x15.common.LocalizedText\"w\n\rPagingRequest\x12\x13\n\x06offset\x18\x01 \x01(\rH\x00\x88\x01\x01\x12\x12\n\x05limit\x18\x02 \x01(\rH\x01\x88\x01\x01\x12\x18\n\x0blastKnownId\x18\x03 \x01(\tH\x02\x88\x01\x01\x42\t\n\x07_offsetB\x08\n\x06_limitB\x0e\n\x0c_lastKnownId\"f\n\x10KeyPagingRequest\x12\x12\n\x05limit\x18\x01 \x01(\rH\x00\x88\x01\x01\x12\x1e\n\x11\x63ontinuationToken\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x08\n\x06_limitB\x14\n\x12_continuationToken\"-\n\rLocalizedText\x12\x0e\n\x06locale\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\"Q\n\x0cTimeInterval\x12\x12\n\x05value\x18\x01 \x01(\x03H\x00\x88\x01\x01\x12#\n\x04unit\x18\x02 \x01(\x0e\x32\x15.enumeration.TimeUnitB\x08\n\x06_value\"7\n\nAuthTokens\x12\x13\n\x0b\x61\x63\x63\x65ssToken\x18\x01 \x01(\t\x12\x14\n\x0crefreshToken\x18\x02 \x01(\t\"\xa8\x04\n\x13TransactionSettings\x12\x14\n\x07\x61ntiMev\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12\x17\n\npreApprove\x18\x02 \x01(\x08H\x01\x88\x01\x01\x12\x18\n\x0b\x61utoApprove\x18\x03 \x01(\x08H\x02\x88\x01\x01\x12\x14\n\x07\x61ntiRug\x18\x04 \x01(\x08H\x03\x88\x01\x01\x12\'\n\x08gasLimit\x18\x05 \x01(\x0b\x32\x10.common.DecimalsH\x04\x88\x01\x01\x12-\n\x0bpriorityFee\x18\x06 \x01(\x0b\x32\x13.common.PriorityFeeH\x05\x88\x01\x01\x12,\n\rbriberyAmount\x18\x07 \x01(\x0b\x32\x10.common.DecimalsH\x06\x88\x01\x01\x12\'\n\x08slippage\x18\x08 \x01(\x0b\x32\x10.common.DecimalsH\x07\x88\x01\x01\x12-\n\nexpiration\x18\t \x01(\x0b\x32\x14.common.TimeIntervalH\x08\x88\x01\x01\x12 \n\x13transferOnBlacklist\x18\n \x01(\x08H\t\x88\x01\x01\x12\x10\n\x03\x66of\x18\x0b \x01(\x08H\n\x88\x01\x01\x42\n\n\x08_antiMevB\r\n\x0b_preApproveB\x0e\n\x0c_autoApproveB\n\n\x08_antiRugB\x0b\n\t_gasLimitB\x0e\n\x0c_priorityFeeB\x10\n\x0e_briberyAmountB\x0b\n\t_slippageB\r\n\x0b_expirationB\x16\n\x14_transferOnBlacklistB\x06\n\x04_fof\"y\n\x0bPriorityFee\x12!\n\x05\x66ixed\x18\x01 \x01(\x0b\x32\x10.common.DecimalsH\x00\x12\x38\n\nmultiplier\x18\x02 \x01(\x0e\x32\".enumeration.PriorityFeeMultiplierH\x00\x42\r\n\x0bpriorityFee\"y\n\x0e\x41nalyticsReply\x12,\n\x0c\x61nalyticsSol\x18\x01 \x01(\x0b\x32\x14.common.AnalyticsSolH\x00\x12,\n\x0c\x61nalyticsEth\x18\x02 \x01(\x0b\x32\x14.common.AnalyticsEthH\x00\x42\x0b\n\tanalytics\"\xe7\x08\n\x0c\x41nalyticsEth\x12%\n\x06\x62uyTax\x18\x01 \x01(\x0b\x32\x10.common.DecimalsH\x00\x88\x01\x01\x12&\n\x07sellTax\x18\x02 \x01(\x0b\x32\x10.common.DecimalsH\x01\x88\x01\x01\x12*\n\x0btransferTax\x18\x03 \x01(\x0b\x32\x10.common.DecimalsH\x02\x88\x01\x01\x12#\n\x04\x63log\x18\x04 \x01(\x0b\x32\x10.common.DecimalsH\x03\x88\x01\x01\x12\x15\n\x08honeypot\x18\x05 \x01(\x08H\x04\x88\x01\x01\x12)\n\x0flockedLiquidity\x18\x06 \x01(\x0b\x32\x10.common.Decimals\x12.\n\x0f\x62urnedLiquidity\x18\x07 \x01(\x0b\x32\x10.common.DecimalsH\x05\x88\x01\x01\x12\x14\n\x07holders\x18\x08 \x01(\x03H\x06\x88\x01\x01\x12%\n\x06maxBuy\x18\t \x01(\x0b\x32\x10.common.DecimalsH\x07\x88\x01\x01\x12&\n\x07maxSell\x18\n \x01(\x0b\x32\x10.common.DecimalsH\x08\x88\x01\x01\x12\x15\n\x08\x63\x61ntSell\x18\x0b \x01(\x03H\t\x88\x01\x01\x12\x16\n\tsellLimit\x18\x0c \x01(\x08H\n\x88\x01\x01\x12\x1b\n\x0e\x64\x65ployerWallet\x18\r \x01(\tH\x0b\x88\x01\x01\x12/\n\x10\x64\x65ployerHoldings\x18\x0e \x01(\x0b\x32\x10.common.DecimalsH\x0c\x88\x01\x01\x12\x32\n\tcreatedAt\x18\x0f \x01(\x0b\x32\x1a.google.protobuf.TimestampH\r\x88\x01\x01\x12\x1d\n\x10verifiedContract\x18\x10 \x01(\x08H\x0e\x88\x01\x01\x12\x16\n\trenounced\x18\x11 \x01(\x08H\x0f\x88\x01\x01\x12\x1d\n\x10notProxyContract\x18\x12 \x01(\x08H\x10\x88\x01\x01\x12\x18\n\x0bownerWallet\x18\x13 \x01(\tH\x11\x88\x01\x01\x12\x1e\n\x11sellLimitPerBlock\x18\x14 \x01(\x08H\x12\x88\x01\x01\x12)\n\ntopHolders\x18\x15 \x01(\x0b\x32\x10.common.DecimalsH\x13\x88\x01\x01\x12.\n\x0f\x63reatorHoldings\x18\x16 \x01(\x0b\x32\x10.common.DecimalsH\x14\x88\x01\x01\x42\t\n\x07_buyTaxB\n\n\x08_sellTaxB\x0e\n\x0c_transferTaxB\x07\n\x05_clogB\x0b\n\t_honeypotB\x12\n\x10_burnedLiquidityB\n\n\x08_holdersB\t\n\x07_maxBuyB\n\n\x08_maxSellB\x0b\n\t_cantSellB\x0c\n\n_sellLimitB\x11\n\x0f_deployerWalletB\x13\n\x11_deployerHoldingsB\x0c\n\n_createdAtB\x13\n\x11_verifiedContractB\x0c\n\n_renouncedB\x13\n\x11_notProxyContractB\x0e\n\x0c_ownerWalletB\x14\n\x12_sellLimitPerBlockB\r\n\x0b_topHoldersB\x12\n\x10_creatorHoldings\"\xe8\x04\n\x0c\x41nalyticsSol\x12.\n\x0f\x62urnedLiquidity\x18\x01 \x01(\x0b\x32\x10.common.DecimalsH\x00\x88\x01\x01\x12+\n\x0cpooledCrypto\x18\x02 \x01(\x0b\x32\x10.common.DecimalsH\x01\x88\x01\x01\x12+\n\x0cpooledTokens\x18\x03 \x01(\x0b\x32\x10.common.DecimalsH\x02\x88\x01\x01\x12\x1a\n\rmintAuthority\x18\x04 \x01(\x08H\x03\x88\x01\x01\x12\x1c\n\x0f\x66reezeAuthority\x18\x05 \x01(\x08H\x04\x88\x01\x01\x12\x14\n\x07holders\x18\x06 \x01(\x03H\x05\x88\x01\x01\x12\x1b\n\x0e\x64\x65ployerWallet\x18\x07 \x01(\tH\x06\x88\x01\x01\x12/\n\x10\x64\x65ployerHoldings\x18\x08 \x01(\x0b\x32\x10.common.DecimalsH\x07\x88\x01\x01\x12\x32\n\tcreatedAt\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x08\x88\x01\x01\x12\x16\n\trenounced\x18\n \x01(\x08H\t\x88\x01\x01\x12)\n\ntopHolders\x18\x0b \x01(\x0b\x32\x10.common.DecimalsH\n\x88\x01\x01\x42\x12\n\x10_burnedLiquidityB\x0f\n\r_pooledCryptoB\x0f\n\r_pooledTokensB\x10\n\x0e_mintAuthorityB\x12\n\x10_freezeAuthorityB\n\n\x08_holdersB\x11\n\x0f_deployerWalletB\x13\n\x11_deployerHoldingsB\x0c\n\n_createdAtB\x0c\n\n_renouncedB\r\n\x0b_topHolders\"\xe2\x02\n\nTokenomics\x12,\n\rpriceInCrypto\x18\x01 \x01(\x0b\x32\x10.common.DecimalsH\x00\x88\x01\x01\x12.\n\x0fliquidityCrypto\x18\x02 \x01(\x0b\x32\x10.common.DecimalsH\x01\x88\x01\x01\x12\x35\n\x16initialLiquidityCrypto\x18\x03 \x01(\x0b\x32\x10.common.DecimalsH\x02\x88\x01\x01\x12%\n\x06mktCap\x18\x04 \x01(\x0b\x32\x10.common.DecimalsH\x03\x88\x01\x01\x12\x11\n\x04txns\x18\x05 \x01(\rH\x04\x88\x01\x01\x12%\n\x06volume\x18\x06 \x01(\x0b\x32\x10.common.DecimalsH\x05\x88\x01\x01\x42\x10\n\x0e_priceInCryptoB\x12\n\x10_liquidityCryptoB\x19\n\x17_initialLiquidityCryptoB\t\n\x07_mktCapB\x07\n\x05_txnsB\t\n\x07_volume\"a\n\nAuditReply\x12$\n\x08\x61uditSol\x18\x01 \x01(\x0b\x32\x10.common.AuditSolH\x00\x12$\n\x08\x61uditEth\x18\x02 \x01(\x0b\x32\x10.common.AuditEthH\x00\x42\x07\n\x05\x61udit\"\x84\x01\n\x08\x41uditSol\x12\x15\n\rmintAuthority\x18\x01 \x01(\x08\x12\x17\n\x0f\x66reezeAuthority\x18\x02 \x01(\x08\x12\"\n\x08lpBurned\x18\x03 \x01(\x0b\x32\x10.common.Decimals\x12$\n\ntopHolders\x18\x04 \x01(\x0b\x32\x10.common.Decimals\"t\n\x08\x41uditEth\x12\x18\n\x10verifiedContract\x18\x01 \x01(\x08\x12\x11\n\trenounced\x18\x02 \x01(\x08\x12\x10\n\x08honeypot\x18\x03 \x01(\x08\x12)\n\x0flockedLiquidity\x18\x04 \x01(\x0b\x32\x10.common.Decimals\"\xee\x02\n\x05Order\x12\x14\n\x07orderId\x18\x01 \x01(\tH\x00\x88\x01\x01\x12 \n\x06\x61mount\x18\x02 \x01(\x0b\x32\x10.common.Decimals\x12+\n\namountType\x18\x03 \x01(\x0e\x32\x17.enumeration.AmountType\x12\x1f\n\x04side\x18\x04 \x01(\x0e\x32\x11.enumeration.Side\x12)\n\x04type\x18\x05 \x01(\x0e\x32\x16.enumeration.OrderTypeH\x01\x88\x01\x01\x12*\n\x07trigger\x18\x06 \x01(\x0b\x32\x14.common.OrderTriggerH\x02\x88\x01\x01\x12-\n\x08settings\x18\x07 \x01(\x0b\x32\x1b.common.TransactionSettings\x12-\n\x06status\x18\x08 \x01(\x0e\x32\x18.enumeration.OrderStatusH\x03\x88\x01\x01\x42\n\n\x08_orderIdB\x07\n\x05_typeB\n\n\x08_triggerB\t\n\x07_status\"\\\n\x0cOrderTrigger\x12+\n\x04type\x18\x01 \x01(\x0e\x32\x1d.enumeration.OrderTriggerType\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.common.Decimals\"&\n\x08\x44\x65\x63imals\x12\r\n\x05value\x18\x01 \x01(\x03\x12\x0b\n\x03\x65xp\x18\x02 \x01(\x11\x42\x1a\xaa\x02\x17TT.Gateway.WebApi.Protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\027TT.Gateway.WebApi.Proto'
  _globals['_GENERALREQUEST']._serialized_start=97
  _globals['_GENERALREQUEST']._serialized_end=249
  _globals['_GENERALREPLY']._serialized_start=251
  _globals['_GENERALREPLY']._serialized_end=323
  _globals['_UNSUBSCRIBEREQUEST']._serialized_start=325
  _globals['_UNSUBSCRIBEREQUEST']._serialized_end=366
  _globals['_REQUESTRESULT']._serialized_start=368
  _globals['_REQUESTRESULT']._serialized_end=484
  _globals['_EMPTYREPLY']._serialized_start=486
  _globals['_EMPTYREPLY']._serialized_end=537
  _globals['_ERRORDESCRIPTION']._serialized_start=539
  _globals['_ERRORDESCRIPTION']._serialized_end=651
  _globals['_PAGINGREQUEST']._serialized_start=653
  _globals['_PAGINGREQUEST']._serialized_end=772
  _globals['_KEYPAGINGREQUEST']._serialized_start=774
  _globals['_KEYPAGINGREQUEST']._serialized_end=876
  _globals['_LOCALIZEDTEXT']._serialized_start=878
  _globals['_LOCALIZEDTEXT']._serialized_end=923
  _globals['_TIMEINTERVAL']._serialized_start=925
  _globals['_TIMEINTERVAL']._serialized_end=1006
  _globals['_AUTHTOKENS']._serialized_start=1008
  _globals['_AUTHTOKENS']._serialized_end=1063
  _globals['_TRANSACTIONSETTINGS']._serialized_start=1066
  _globals['_TRANSACTIONSETTINGS']._serialized_end=1618
  _globals['_PRIORITYFEE']._serialized_start=1620
  _globals['_PRIORITYFEE']._serialized_end=1741
  _globals['_ANALYTICSREPLY']._serialized_start=1743
  _globals['_ANALYTICSREPLY']._serialized_end=1864
  _globals['_ANALYTICSETH']._serialized_start=1867
  _globals['_ANALYTICSETH']._serialized_end=2994
  _globals['_ANALYTICSSOL']._serialized_start=2997
  _globals['_ANALYTICSSOL']._serialized_end=3613
  _globals['_TOKENOMICS']._serialized_start=3616
  _globals['_TOKENOMICS']._serialized_end=3970
  _globals['_AUDITREPLY']._serialized_start=3972
  _globals['_AUDITREPLY']._serialized_end=4069
  _globals['_AUDITSOL']._serialized_start=4072
  _globals['_AUDITSOL']._serialized_end=4204
  _globals['_AUDITETH']._serialized_start=4206
  _globals['_AUDITETH']._serialized_end=4322
  _globals['_ORDER']._serialized_start=4325
  _globals['_ORDER']._serialized_end=4691
  _globals['_ORDERTRIGGER']._serialized_start=4693
  _globals['_ORDERTRIGGER']._serialized_end=4785
  _globals['_DECIMALS']._serialized_start=4787
  _globals['_DECIMALS']._serialized_end=4825
# @@protoc_insertion_point(module_scope)