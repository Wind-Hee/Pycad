import __clrclasses__.System.Configuration.Assemblies as Assemblies
from __clrclasses__.System import Type as _n_0_t_0
from __clrclasses__.System import SystemException as _n_0_t_1
from __clrclasses__.System import Exception as _n_0_t_2
from __clrclasses__.System import ICloneable as _n_0_t_3
from __clrclasses__.System import Attribute as _n_0_t_4
from __clrclasses__.System import UriIdnScope as _n_0_t_5
from __clrclasses__.System import GenericUriParserOptions as _n_0_t_6
from __clrclasses__.System import MulticastDelegate as _n_0_t_7
from __clrclasses__.System import IntPtr as _n_0_t_8
from __clrclasses__.System import IAsyncResult as _n_0_t_9
from __clrclasses__.System import AsyncCallback as _n_0_t_10
from __clrclasses__.System import EventArgs as _n_0_t_11
from __clrclasses__.System import Enum as _n_0_t_12
from __clrclasses__.System import IComparable as _n_0_t_13
from __clrclasses__.System import IFormattable as _n_0_t_14
from __clrclasses__.System import IConvertible as _n_0_t_15
from __clrclasses__.System.Collections import IEnumerable as _n_1_t_0
from __clrclasses__.System.Collections import ICollection as _n_1_t_1
from __clrclasses__.System.Collections import Hashtable as _n_1_t_2
from __clrclasses__.System.Collections import IDictionary as _n_1_t_3
from __clrclasses__.System.Collections.Specialized import NameValueCollection as _n_2_t_0
from __clrclasses__.System.ComponentModel import INotifyPropertyChanged as _n_3_t_0
from __clrclasses__.System.ComponentModel import CancelEventArgs as _n_3_t_1
from __clrclasses__.System.Configuration.Internal import IConfigErrorInfo as _n_4_t_0
from __clrclasses__.System.Configuration.Provider import ProviderBase as _n_5_t_0
from __clrclasses__.System.Configuration.Provider import ProviderCollection as _n_5_t_1
from __clrclasses__.System.Runtime.InteropServices import _Attribute as _n_6_t_0
from __clrclasses__.System.Runtime.InteropServices import _Exception as _n_6_t_1
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_7_t_0
from __clrclasses__.System.Runtime.Serialization import IDeserializationCallback as _n_7_t_1
from __clrclasses__.System.Xml import XmlNode as _n_8_t_0
from __clrclasses__.System.Xml import XmlDocument as _n_8_t_1
from __clrclasses__.System.Xml import XmlTextReader as _n_8_t_2
from __clrclasses__.System.Xml.XPath import IXPathNavigable as _n_9_t_0
import typing
class ApplicationScopedSettingAttribute(SettingAttribute, _n_6_t_0):
    def __init__(self) -> ApplicationScopedSettingAttribute:...
class ApplicationSettingsBase(SettingsBase, _n_3_t_0):
    @property
    def SettingsKey(self) -> str:"""SettingsKey { get; set; } -> str"""
    @property
    def SettingChanging(self) -> SettingChangingEventHandler:
        """SettingChanging Event: SettingChangingEventHandler"""
    @property
    def SettingsLoaded(self) -> SettingsLoadedEventHandler:
        """SettingsLoaded Event: SettingsLoadedEventHandler"""
    @property
    def SettingsSaving(self) -> SettingsSavingEventHandler:
        """SettingsSaving Event: SettingsSavingEventHandler"""
    def GetPreviousVersion(self, propertyName: str) -> object:...
    def Reload(self):...
    def Reset(self):...
    def Upgrade(self):...
class ApplicationSettingsGroup(ConfigurationSectionGroup):
    def __init__(self) -> ApplicationSettingsGroup:...
class AppSettingsReader(object):
    def __init__(self) -> AppSettingsReader:...
    def GetValue(self, key: str, type: _n_0_t_0) -> object:...
class ClientSettingsSection(ConfigurationSection):
    @property
    def Settings(self) -> SettingElementCollection:"""Settings { get; } -> SettingElementCollection"""
    def __init__(self) -> ClientSettingsSection:...
class ConfigurationException(_n_0_t_1, _n_7_t_0, _n_6_t_1):
    @property
    def BareMessage(self) -> str:"""BareMessage { get; } -> str"""
    @property
    def Filename(self) -> str:"""Filename { get; } -> str"""
    @property
    def Line(self) -> int:"""Line { get; } -> int"""
    def __init__(self, message: str, inner: _n_0_t_2, filename: str, line: int) -> ConfigurationException:...
    def __init__(self, message: str, filename: str, line: int) -> ConfigurationException:...
    def __init__(self, message: str, inner: _n_0_t_2, node: _n_8_t_0) -> ConfigurationException:...
    def __init__(self, message: str, node: _n_8_t_0) -> ConfigurationException:...
    def __init__(self, message: str, inner: _n_0_t_2) -> ConfigurationException:...
    def __init__(self, message: str) -> ConfigurationException:...
    def __init__(self) -> ConfigurationException:...
    @staticmethod
    def GetXmlNodeFilename(node: _n_8_t_0) -> str:...
    @staticmethod
    def GetXmlNodeLineNumber(node: _n_8_t_0) -> int:...
class ConfigurationSettings(object):
    @property
    def AppSettings(self) -> _n_2_t_0:"""AppSettings { get; } -> NameValueCollection"""
    @staticmethod
    def GetConfig(sectionName: str) -> object:...
class ConfigXmlDocument(_n_8_t_1, _n_0_t_3, _n_1_t_0, _n_9_t_0, _n_4_t_0, typing.Iterable[_n_8_t_-1]):
    def __init__(self) -> ConfigXmlDocument:...
    def LoadSingleElement(self, filename: str, sourceReader: _n_8_t_2):...
class DefaultSettingValueAttribute(_n_0_t_4, _n_6_t_0):
    @property
    def Value(self) -> str:"""Value { get; } -> str"""
    def __init__(self, value: str) -> DefaultSettingValueAttribute:...
class DictionarySectionHandler(IConfigurationSectionHandler):
    def __init__(self) -> DictionarySectionHandler:...
class IApplicationSettingsProvider():
    def GetPreviousVersion(self, context: SettingsContext, property: SettingsProperty) -> SettingsPropertyValue:...
    def Reset(self, context: SettingsContext):...
    def Upgrade(self, context: SettingsContext, properties: SettingsPropertyCollection):...
class IConfigurationSectionHandler():
    def Create(self, parent: object, configContext: object, section: _n_8_t_0) -> object:...
class IConfigurationSystem():
    def GetConfig(self, configKey: str) -> object:...
    def Init(self):...
class IdnElement(ConfigurationElement):
    @property
    def Enabled(self) -> _n_0_t_5:"""Enabled { get; set; } -> UriIdnScope"""
    def __init__(self) -> IdnElement:...
class IgnoreSectionHandler(IConfigurationSectionHandler):
    def __init__(self) -> IgnoreSectionHandler:...
class IPersistComponentSettings():
    @property
    def SaveSettings(self) -> bool:"""SaveSettings { get; set; } -> bool"""
    @property
    def SettingsKey(self) -> str:"""SettingsKey { get; set; } -> str"""
    def LoadComponentSettings(self):...
    def ResetComponentSettings(self):...
    def SaveComponentSettings(self):...
class IriParsingElement(ConfigurationElement):
    @property
    def Enabled(self) -> bool:"""Enabled { get; set; } -> bool"""
    def __init__(self) -> IriParsingElement:...
class ISettingsProviderService():
    def GetSettingsProvider(self, property: SettingsProperty) -> SettingsProvider:...
class LocalFileSettingsProvider(SettingsProvider, IApplicationSettingsProvider):
    def __init__(self) -> LocalFileSettingsProvider:...
class NameValueFileSectionHandler(IConfigurationSectionHandler):
    def __init__(self) -> NameValueFileSectionHandler:...
class NameValueSectionHandler(IConfigurationSectionHandler):
    def __init__(self) -> NameValueSectionHandler:...
class NoSettingsVersionUpgradeAttribute(_n_0_t_4, _n_6_t_0):
    def __init__(self) -> NoSettingsVersionUpgradeAttribute:...
class SchemeSettingElement(ConfigurationElement):
    @property
    def GenericUriParserOptions(self) -> _n_0_t_6:"""GenericUriParserOptions { get; } -> GenericUriParserOptions"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    def __init__(self) -> SchemeSettingElement:...
class SchemeSettingElementCollection(ConfigurationElementCollection, _n_1_t_1, typing.Iterable[SchemeSettingElement]):
    @property
    def Item(self) -> SchemeSettingElement:"""Item { get; } -> SchemeSettingElement"""
    def __init__(self) -> SchemeSettingElementCollection:...
    def IndexOf(self, element: SchemeSettingElement) -> int:...
class SettingAttribute(_n_0_t_4, _n_6_t_0):
    def __init__(self) -> SettingAttribute:...
class SettingChangingEventArgs(_n_3_t_1):
    @property
    def NewValue(self) -> object:"""NewValue { get; } -> object"""
    @property
    def SettingClass(self) -> str:"""SettingClass { get; } -> str"""
    @property
    def SettingKey(self) -> str:"""SettingKey { get; } -> str"""
    @property
    def SettingName(self) -> str:"""SettingName { get; } -> str"""
    def __init__(self, settingName: str, settingClass: str, settingKey: str, newValue: object, cancel: bool) -> SettingChangingEventArgs:...
class SettingChangingEventHandler(_n_0_t_7, _n_0_t_3, _n_7_t_0):
    def __init__(self, object: object, method: _n_0_t_8) -> SettingChangingEventHandler:...
    def BeginInvoke(self, sender: object, e: SettingChangingEventArgs, callback: _n_0_t_10, object: object) -> _n_0_t_9:...
    def EndInvoke(self, result: _n_0_t_9):...
    def Invoke(self, sender: object, e: SettingChangingEventArgs):...
class SettingElement(ConfigurationElement):
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def SerializeAs(self) -> SettingsSerializeAs:"""SerializeAs { get; set; } -> SettingsSerializeAs"""
    @property
    def Value(self) -> SettingValueElement:"""Value { get; set; } -> SettingValueElement"""
    def __init__(self, name: str, serializeAs: SettingsSerializeAs) -> SettingElement:...
    def __init__(self) -> SettingElement:...
class SettingElementCollection(ConfigurationElementCollection, _n_1_t_1):
    def __init__(self) -> SettingElementCollection:...
    def Add(self, element: SettingElement):...
    def Clear(self):...
    def Get(self, elementKey: str) -> SettingElement:...
    def Remove(self, element: SettingElement):...
class SettingsAttributeDictionary(_n_1_t_2, _n_1_t_3, _n_7_t_0, _n_7_t_1, _n_0_t_3):
    def __init__(self, attributes: SettingsAttributeDictionary) -> SettingsAttributeDictionary:...
    def __init__(self) -> SettingsAttributeDictionary:...
class SettingsBase(object):
    @property
    def Context(self) -> SettingsContext:"""Context { get; } -> SettingsContext"""
    @property
    def IsSynchronized(self) -> bool:"""IsSynchronized { get; } -> bool"""
    @property
    def Item(self) -> object:"""Item { get; set; } -> object"""
    @property
    def Properties(self) -> SettingsPropertyCollection:"""Properties { get; } -> SettingsPropertyCollection"""
    @property
    def PropertyValues(self) -> SettingsPropertyValueCollection:"""PropertyValues { get; } -> SettingsPropertyValueCollection"""
    @property
    def Providers(self) -> SettingsProviderCollection:"""Providers { get; } -> SettingsProviderCollection"""
    def Initialize(self, context: SettingsContext, properties: SettingsPropertyCollection, providers: SettingsProviderCollection):...
    def Save(self):...
    @staticmethod
    def Synchronized(settingsBase: SettingsBase) -> SettingsBase:...
class SettingsContext(_n_1_t_2, _n_1_t_3, _n_7_t_0, _n_7_t_1, _n_0_t_3):
    def __init__(self) -> SettingsContext:...
class SettingsDescriptionAttribute(_n_0_t_4, _n_6_t_0):
    @property
    def Description(self) -> str:"""Description { get; } -> str"""
    def __init__(self, description: str) -> SettingsDescriptionAttribute:...
class SettingsGroupDescriptionAttribute(_n_0_t_4, _n_6_t_0):
    @property
    def Description(self) -> str:"""Description { get; } -> str"""
    def __init__(self, description: str) -> SettingsGroupDescriptionAttribute:...
class SettingsGroupNameAttribute(_n_0_t_4, _n_6_t_0):
    @property
    def GroupName(self) -> str:"""GroupName { get; } -> str"""
    def __init__(self, groupName: str) -> SettingsGroupNameAttribute:...
class SettingsLoadedEventArgs(_n_0_t_11):
    @property
    def Provider(self) -> SettingsProvider:"""Provider { get; } -> SettingsProvider"""
    def __init__(self, provider: SettingsProvider) -> SettingsLoadedEventArgs:...
class SettingsLoadedEventHandler(_n_0_t_7, _n_0_t_3, _n_7_t_0):
    def __init__(self, object: object, method: _n_0_t_8) -> SettingsLoadedEventHandler:...
    def BeginInvoke(self, sender: object, e: SettingsLoadedEventArgs, callback: _n_0_t_10, object: object) -> _n_0_t_9:...
    def EndInvoke(self, result: _n_0_t_9):...
    def Invoke(self, sender: object, e: SettingsLoadedEventArgs):...
class SettingsManageability(_n_0_t_12, _n_0_t_13, _n_0_t_14, _n_0_t_15):
    Roaming: int
    value__: int
class SettingsManageabilityAttribute(_n_0_t_4, _n_6_t_0):
    @property
    def Manageability(self) -> SettingsManageability:"""Manageability { get; } -> SettingsManageability"""
    def __init__(self, manageability: SettingsManageability) -> SettingsManageabilityAttribute:...
class SettingsProperty(object):
    @property
    def Attributes(self) -> SettingsAttributeDictionary:"""Attributes { get; } -> SettingsAttributeDictionary"""
    @property
    def DefaultValue(self) -> object:"""DefaultValue { get; set; } -> object"""
    @property
    def IsReadOnly(self) -> bool:"""IsReadOnly { get; set; } -> bool"""
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def PropertyType(self) -> _n_0_t_0:"""PropertyType { get; set; } -> Type"""
    @property
    def Provider(self) -> SettingsProvider:"""Provider { get; set; } -> SettingsProvider"""
    @property
    def SerializeAs(self) -> SettingsSerializeAs:"""SerializeAs { get; set; } -> SettingsSerializeAs"""
    @property
    def ThrowOnErrorDeserializing(self) -> bool:"""ThrowOnErrorDeserializing { get; set; } -> bool"""
    @property
    def ThrowOnErrorSerializing(self) -> bool:"""ThrowOnErrorSerializing { get; set; } -> bool"""
    def __init__(self, propertyToCopy: SettingsProperty) -> SettingsProperty:...
    def __init__(self, name: str, propertyType: _n_0_t_0, provider: SettingsProvider, isReadOnly: bool, defaultValue: object, serializeAs: SettingsSerializeAs, attributes: SettingsAttributeDictionary, throwOnErrorDeserializing: bool, throwOnErrorSerializing: bool) -> SettingsProperty:...
    def __init__(self, name: str) -> SettingsProperty:...
class SettingsPropertyCollection(_n_1_t_0, _n_0_t_3, _n_1_t_1, typing.Iterable[SettingsProperty]):
    @property
    def Item(self) -> SettingsProperty:"""Item { get; } -> SettingsProperty"""
    def __init__(self) -> SettingsPropertyCollection:...
    def Add(self, property: SettingsProperty):...
    def Clear(self):...
    def Remove(self, name: str):...
    def SetReadOnly(self):...
class SettingsPropertyIsReadOnlyException(_n_0_t_2, _n_7_t_0, _n_6_t_1):
    def __init__(self) -> SettingsPropertyIsReadOnlyException:...
    def __init__(self, message: str, innerException: _n_0_t_2) -> SettingsPropertyIsReadOnlyException:...
    def __init__(self, message: str) -> SettingsPropertyIsReadOnlyException:...
class SettingsPropertyNotFoundException(_n_0_t_2, _n_7_t_0, _n_6_t_1):
    def __init__(self) -> SettingsPropertyNotFoundException:...
    def __init__(self, message: str, innerException: _n_0_t_2) -> SettingsPropertyNotFoundException:...
    def __init__(self, message: str) -> SettingsPropertyNotFoundException:...
class SettingsPropertyValue(object):
    @property
    def Deserialized(self) -> bool:"""Deserialized { get; set; } -> bool"""
    @property
    def IsDirty(self) -> bool:"""IsDirty { get; set; } -> bool"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def Property(self) -> SettingsProperty:"""Property { get; } -> SettingsProperty"""
    @property
    def PropertyValue(self) -> object:"""PropertyValue { get; set; } -> object"""
    @property
    def SerializedValue(self) -> object:"""SerializedValue { get; set; } -> object"""
    @property
    def UsingDefaultValue(self) -> bool:"""UsingDefaultValue { get; } -> bool"""
    def __init__(self, property: SettingsProperty) -> SettingsPropertyValue:...
class SettingsPropertyValueCollection(_n_1_t_0, _n_0_t_3, _n_1_t_1, typing.Iterable[SettingsPropertyValue]):
    @property
    def Item(self) -> SettingsPropertyValue:"""Item { get; } -> SettingsPropertyValue"""
    def __init__(self) -> SettingsPropertyValueCollection:...
    def Add(self, property: SettingsPropertyValue):...
    def Clear(self):...
    def Remove(self, name: str):...
    def SetReadOnly(self):...
class SettingsPropertyWrongTypeException(_n_0_t_2, _n_7_t_0, _n_6_t_1):
    def __init__(self) -> SettingsPropertyWrongTypeException:...
    def __init__(self, message: str, innerException: _n_0_t_2) -> SettingsPropertyWrongTypeException:...
    def __init__(self, message: str) -> SettingsPropertyWrongTypeException:...
class SettingsProvider(_n_5_t_0):
    @property
    def ApplicationName(self) -> str:"""ApplicationName { get; set; } -> str"""
    def GetPropertyValues(self, context: SettingsContext, collection: SettingsPropertyCollection) -> SettingsPropertyValueCollection:...
    def SetPropertyValues(self, context: SettingsContext, collection: SettingsPropertyValueCollection):...
class SettingsProviderAttribute(_n_0_t_4, _n_6_t_0):
    @property
    def ProviderTypeName(self) -> str:"""ProviderTypeName { get; } -> str"""
    def __init__(self, providerType: _n_0_t_0) -> SettingsProviderAttribute:...
    def __init__(self, providerTypeName: str) -> SettingsProviderAttribute:...
class SettingsProviderCollection(_n_5_t_1, _n_1_t_0, _n_1_t_1, typing.Iterable[SettingsProvider]):
    def __init__(self) -> SettingsProviderCollection:...
class SettingsSavingEventHandler(_n_0_t_7, _n_0_t_3, _n_7_t_0):
    def __init__(self, object: object, method: _n_0_t_8) -> SettingsSavingEventHandler:...
    def BeginInvoke(self, sender: object, e: _n_3_t_1, callback: _n_0_t_10, object: object) -> _n_0_t_9:...
    def EndInvoke(self, result: _n_0_t_9):...
    def Invoke(self, sender: object, e: _n_3_t_1):...
class SettingsSerializeAs(_n_0_t_12, _n_0_t_13, _n_0_t_14, _n_0_t_15):
    Binary: int
    ProviderSpecific: int
    String: int
    value__: int
    Xml: int
class SettingsSerializeAsAttribute(_n_0_t_4, _n_6_t_0):
    @property
    def SerializeAs(self) -> SettingsSerializeAs:"""SerializeAs { get; } -> SettingsSerializeAs"""
    def __init__(self, serializeAs: SettingsSerializeAs) -> SettingsSerializeAsAttribute:...
class SettingValueElement(ConfigurationElement):
    @property
    def ValueXml(self) -> _n_8_t_0:"""ValueXml { get; set; } -> XmlNode"""
    def __init__(self) -> SettingValueElement:...
class SingleTagSectionHandler(IConfigurationSectionHandler):
    def __init__(self) -> SingleTagSectionHandler:...
class SpecialSetting(_n_0_t_12, _n_0_t_13, _n_0_t_14, _n_0_t_15):
    ConnectionString: int
    value__: int
    WebServiceUrl: int
class SpecialSettingAttribute(_n_0_t_4, _n_6_t_0):
    @property
    def SpecialSetting(self) -> SpecialSetting:"""SpecialSetting { get; } -> SpecialSetting"""
    def __init__(self, specialSetting: SpecialSetting) -> SpecialSettingAttribute:...
class UriSection(ConfigurationSection):
    @property
    def Idn(self) -> IdnElement:"""Idn { get; } -> IdnElement"""
    @property
    def IriParsing(self) -> IriParsingElement:"""IriParsing { get; } -> IriParsingElement"""
    @property
    def SchemeSettings(self) -> SchemeSettingElementCollection:"""SchemeSettings { get; } -> SchemeSettingElementCollection"""
    def __init__(self) -> UriSection:...
class UserScopedSettingAttribute(SettingAttribute, _n_6_t_0):
    def __init__(self) -> UserScopedSettingAttribute:...
class UserSettingsGroup(ConfigurationSectionGroup):
    def __init__(self) -> UserSettingsGroup:...