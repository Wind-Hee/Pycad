from __clrclasses__.System import Attribute as _n_0_t_0
from __clrclasses__.System import Type as _n_0_t_1
from __clrclasses__.System import IServiceProvider as _n_0_t_2
from __clrclasses__.System import EventHandler as _n_0_t_3
from __clrclasses__.System import ValueType as _n_0_t_4
from __clrclasses__.System import EventArgs as _n_0_t_5
from __clrclasses__.System import MulticastDelegate as _n_0_t_6
from __clrclasses__.System import ICloneable as _n_0_t_7
from __clrclasses__.System import IntPtr as _n_0_t_8
from __clrclasses__.System import IAsyncResult as _n_0_t_9
from __clrclasses__.System import AsyncCallback as _n_0_t_10
from __clrclasses__.System import IDisposable as _n_0_t_11
from __clrclasses__.System.Collections import ICollection as _n_1_t_0
from __clrclasses__.System.ComponentModel import IContainer as _n_2_t_0
from __clrclasses__.System.ComponentModel import MemberDescriptor as _n_2_t_1
from __clrclasses__.System.ComponentModel import PropertyDescriptorCollection as _n_2_t_2
from __clrclasses__.System.ComponentModel.Design import IDesignerHost as _n_3_t_0
from __clrclasses__.System.IO import Stream as _n_4_t_0
from __clrclasses__.System.Reflection import MemberInfo as _n_5_t_0
from __clrclasses__.System.Runtime.InteropServices import _Attribute as _n_6_t_0
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_7_t_0
import typing
class ComponentSerializationService(object):
    def CreateStore(self) -> SerializationStore:...
    def Deserialize(self, store: SerializationStore, container: _n_2_t_0) -> _n_1_t_0:...
    def Deserialize(self, store: SerializationStore) -> _n_1_t_0:...
    def DeserializeTo(self, store: SerializationStore, container: _n_2_t_0, validateRecycledTypes: bool):...
    def DeserializeTo(self, store: SerializationStore, container: _n_2_t_0):...
    def DeserializeTo(self, store: SerializationStore, container: _n_2_t_0, validateRecycledTypes: bool, applyDefaults: bool):...
    def LoadStore(self, stream: _n_4_t_0) -> SerializationStore:...
    def Serialize(self, store: SerializationStore, value: object):...
    def SerializeAbsolute(self, store: SerializationStore, value: object):...
    def SerializeMember(self, store: SerializationStore, owningObject: object, member: _n_2_t_1):...
    def SerializeMemberAbsolute(self, store: SerializationStore, owningObject: object, member: _n_2_t_1):...
class ContextStack(object):
    @property
    def Current(self) -> object:"""Current { get; } -> object"""
    @property
    def Item(self) -> object:"""Item { get; } -> object"""
    def __init__(self) -> ContextStack:...
    def Append(self, context: object):...
    def Pop(self) -> object:...
    def Push(self, context: object):...
class DefaultSerializationProviderAttribute(_n_0_t_0, _n_6_t_0):
    @property
    def ProviderTypeName(self) -> str:"""ProviderTypeName { get; } -> str"""
    def __init__(self, providerTypeName: str) -> DefaultSerializationProviderAttribute:...
    def __init__(self, providerType: _n_0_t_1) -> DefaultSerializationProviderAttribute:...
class DesignerLoader(object):
    @property
    def Loading(self) -> bool:"""Loading { get; } -> bool"""
    def BeginLoad(self, host: IDesignerLoaderHost):...
    def Dispose(self):...
    def Flush(self):...
class DesignerSerializerAttribute(_n_0_t_0, _n_6_t_0):
    @property
    def SerializerBaseTypeName(self) -> str:"""SerializerBaseTypeName { get; } -> str"""
    @property
    def SerializerTypeName(self) -> str:"""SerializerTypeName { get; } -> str"""
    def __init__(self, serializerTypeName: str, baseSerializerTypeName: str) -> DesignerSerializerAttribute:...
    def __init__(self, serializerTypeName: str, baseSerializerType: _n_0_t_1) -> DesignerSerializerAttribute:...
    def __init__(self, serializerType: _n_0_t_1, baseSerializerType: _n_0_t_1) -> DesignerSerializerAttribute:...
class IDesignerLoaderHost(_n_3_t_0):
    def EndLoad(self, baseClassName: str, successful: bool, errorCollection: _n_1_t_0):...
    def Reload(self):...
class IDesignerLoaderHost2(IDesignerLoaderHost):
    @property
    def CanReloadWithErrors(self) -> bool:"""CanReloadWithErrors { get; set; } -> bool"""
    @property
    def IgnoreErrorsDuringReload(self) -> bool:"""IgnoreErrorsDuringReload { get; set; } -> bool"""
class IDesignerLoaderService():
    def AddLoadDependency(self):...
    def DependentLoadComplete(self, successful: bool, errorCollection: _n_1_t_0):...
    def Reload(self) -> bool:...
class IDesignerSerializationManager(_n_0_t_2):
    @property
    def Context(self) -> ContextStack:"""Context { get; } -> ContextStack"""
    @property
    def Properties(self) -> _n_2_t_2:"""Properties { get; } -> PropertyDescriptorCollection"""
    @property
    def ResolveName(self) -> ResolveNameEventHandler:
        """ResolveName Event: ResolveNameEventHandler"""
    @property
    def SerializationComplete(self) -> _n_0_t_3:
        """SerializationComplete Event: EventHandler"""
    def AddSerializationProvider(self, provider: IDesignerSerializationProvider):...
    def CreateInstance(self, type: _n_0_t_1, arguments: _n_1_t_0, name: str, addToContainer: bool) -> object:...
    def GetInstance(self, name: str) -> object:...
    def GetName(self, value: object) -> str:...
    def GetSerializer(self, objectType: _n_0_t_1, serializerType: _n_0_t_1) -> object:...
    def GetType(self, typeName: str) -> _n_0_t_1:...
    def RemoveSerializationProvider(self, provider: IDesignerSerializationProvider):...
    def ReportError(self, errorInformation: object):...
    def SetName(self, instance: object, name: str):...
class IDesignerSerializationProvider():
    def GetSerializer(self, manager: IDesignerSerializationManager, currentSerializer: object, objectType: _n_0_t_1, serializerType: _n_0_t_1) -> object:...
class IDesignerSerializationService():
    def Deserialize(self, serializationData: object) -> _n_1_t_0:...
    def Serialize(self, objects: _n_1_t_0) -> object:...
class INameCreationService():
    def CreateName(self, container: _n_2_t_0, dataType: _n_0_t_1) -> str:...
    def IsValidName(self, name: str) -> bool:...
    def ValidateName(self, name: str):...
class InstanceDescriptor(object):
    @property
    def Arguments(self) -> _n_1_t_0:"""Arguments { get; } -> ICollection"""
    @property
    def IsComplete(self) -> bool:"""IsComplete { get; } -> bool"""
    @property
    def MemberInfo(self) -> _n_5_t_0:"""MemberInfo { get; } -> MemberInfo"""
    def __init__(self, member: _n_5_t_0, arguments: _n_1_t_0) -> InstanceDescriptor:...
    def __init__(self, member: _n_5_t_0, arguments: _n_1_t_0, isComplete: bool) -> InstanceDescriptor:...
    def Invoke(self) -> object:...
class MemberRelationship(_n_0_t_4):
    Empty: int
    @property
    def IsEmpty(self) -> bool:"""IsEmpty { get; } -> bool"""
    @property
    def Member(self) -> _n_2_t_1:"""Member { get; } -> MemberDescriptor"""
    @property
    def Owner(self) -> object:"""Owner { get; } -> object"""
    def __init__(self, owner: object, member: _n_2_t_1) -> MemberRelationship:...
class MemberRelationshipService(typing.Iterable[MemberRelationship]):
    @property
    def Item(self) -> MemberRelationship:"""Item { get; set; } -> MemberRelationship"""
    def SupportsRelationship(self, source: MemberRelationship, relationship: MemberRelationship) -> bool:...
class ResolveNameEventArgs(_n_0_t_5):
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def Value(self) -> object:"""Value { get; set; } -> object"""
    def __init__(self, name: str) -> ResolveNameEventArgs:...
class ResolveNameEventHandler(_n_0_t_6, _n_0_t_7, _n_7_t_0):
    def __init__(self, object: object, method: _n_0_t_8) -> ResolveNameEventHandler:...
    def BeginInvoke(self, sender: object, e: ResolveNameEventArgs, callback: _n_0_t_10, object: object) -> _n_0_t_9:...
    def EndInvoke(self, result: _n_0_t_9):...
    def Invoke(self, sender: object, e: ResolveNameEventArgs):...
class RootDesignerSerializerAttribute(_n_0_t_0, _n_6_t_0):
    @property
    def Reloadable(self) -> bool:"""Reloadable { get; } -> bool"""
    @property
    def SerializerBaseTypeName(self) -> str:"""SerializerBaseTypeName { get; } -> str"""
    @property
    def SerializerTypeName(self) -> str:"""SerializerTypeName { get; } -> str"""
    def __init__(self, serializerTypeName: str, baseSerializerType: _n_0_t_1, reloadable: bool) -> RootDesignerSerializerAttribute:...
    def __init__(self, serializerType: _n_0_t_1, baseSerializerType: _n_0_t_1, reloadable: bool) -> RootDesignerSerializerAttribute:...
    def __init__(self, serializerTypeName: str, baseSerializerTypeName: str, reloadable: bool) -> RootDesignerSerializerAttribute:...
class SerializationStore(_n_0_t_11):
    @property
    def Errors(self) -> _n_1_t_0:"""Errors { get; } -> ICollection"""
    def Close(self):...
    def Save(self, stream: _n_4_t_0):...