from __clrclasses__.System import Array as _n_0_t_0
from __clrclasses__.System import Type as _n_0_t_1
from __clrclasses__.System import IntPtr as _n_0_t_2
from __clrclasses__.System import Attribute as _n_0_t_3
from __clrclasses__.System import Enum as _n_0_t_4
from __clrclasses__.System import IComparable as _n_0_t_5
from __clrclasses__.System import IFormattable as _n_0_t_6
from __clrclasses__.System import IConvertible as _n_0_t_7
from __clrclasses__.System import IDisposable as _n_0_t_8
from __clrclasses__.System.CodeDom import CodeCompileUnit as _n_1_t_0
from __clrclasses__.System.CodeDom import CodeExpression as _n_1_t_1
from __clrclasses__.System.CodeDom import CodeTypeMember as _n_1_t_2
from __clrclasses__.System.CodeDom import CodeNamespace as _n_1_t_3
from __clrclasses__.System.CodeDom import CodeStatement as _n_1_t_4
from __clrclasses__.System.CodeDom import CodeTypeDeclaration as _n_1_t_5
from __clrclasses__.System.CodeDom import CodeTypeReference as _n_1_t_6
from __clrclasses__.System.CodeDom import CodeObject as _n_1_t_7
from __clrclasses__.System.Collections import CollectionBase as _n_2_t_0
from __clrclasses__.System.Collections import IList as _n_2_t_1
from __clrclasses__.System.Collections import ICollection as _n_2_t_2
from __clrclasses__.System.Collections.Generic import IDictionary as _n_3_t_0
from __clrclasses__.System.Collections.Specialized import StringCollection as _n_4_t_0
from __clrclasses__.System.ComponentModel import Component as _n_5_t_0
from __clrclasses__.System.ComponentModel import IComponent as _n_5_t_1
from __clrclasses__.System.ComponentModel import TypeConverter as _n_5_t_2
from __clrclasses__.System.IO import TextWriter as _n_6_t_0
from __clrclasses__.System.IO import TextReader as _n_6_t_1
from __clrclasses__.System.Reflection import Assembly as _n_7_t_0
from __clrclasses__.System.Runtime.InteropServices import _Attribute as _n_8_t_0
from __clrclasses__.System.Security.Policy import Evidence as _n_9_t_0
import typing
class CodeCompiler(CodeGenerator, ICodeGenerator, ICodeCompiler):
    pass
class CodeDomProvider(_n_5_t_0, _n_5_t_1):
    @property
    def FileExtension(self) -> str:"""FileExtension { get; } -> str"""
    @property
    def LanguageOptions(self) -> LanguageOptions:"""LanguageOptions { get; } -> LanguageOptions"""
    def CompileAssemblyFromDom(self, options: CompilerParameters, compilationUnits: _n_0_t_0[_n_1_t_0]) -> CompilerResults:...
    def CompileAssemblyFromFile(self, options: CompilerParameters, fileNames: _n_0_t_0[str]) -> CompilerResults:...
    def CompileAssemblyFromSource(self, options: CompilerParameters, sources: _n_0_t_0[str]) -> CompilerResults:...
    def CreateCompiler(self) -> ICodeCompiler:...
    def CreateEscapedIdentifier(self, value: str) -> str:...
    def CreateGenerator(self, fileName: str) -> ICodeGenerator:...
    def CreateGenerator(self, output: _n_6_t_0) -> ICodeGenerator:...
    def CreateGenerator(self) -> ICodeGenerator:...
    def CreateParser(self) -> ICodeParser:...
    @staticmethod
    def CreateProvider(language: str) -> CodeDomProvider:...
    @staticmethod
    def CreateProvider(language: str, providerOptions: _n_3_t_0[str, str]) -> CodeDomProvider:...
    def CreateValidIdentifier(self, value: str) -> str:...
    def GenerateCodeFromCompileUnit(self, compileUnit: _n_1_t_0, writer: _n_6_t_0, options: CodeGeneratorOptions):...
    def GenerateCodeFromExpression(self, expression: _n_1_t_1, writer: _n_6_t_0, options: CodeGeneratorOptions):...
    def GenerateCodeFromMember(self, member: _n_1_t_2, writer: _n_6_t_0, options: CodeGeneratorOptions):...
    def GenerateCodeFromNamespace(self, codeNamespace: _n_1_t_3, writer: _n_6_t_0, options: CodeGeneratorOptions):...
    def GenerateCodeFromStatement(self, statement: _n_1_t_4, writer: _n_6_t_0, options: CodeGeneratorOptions):...
    def GenerateCodeFromType(self, codeType: _n_1_t_5, writer: _n_6_t_0, options: CodeGeneratorOptions):...
    @staticmethod
    def GetAllCompilerInfo() -> _n_0_t_0[CompilerInfo]:...
    @staticmethod
    def GetCompilerInfo(language: str) -> CompilerInfo:...
    def GetConverter(self, type: _n_0_t_1) -> _n_5_t_2:...
    @staticmethod
    def GetLanguageFromExtension(extension: str) -> str:...
    def GetTypeOutput(self, type: _n_1_t_6) -> str:...
    @staticmethod
    def IsDefinedExtension(extension: str) -> bool:...
    @staticmethod
    def IsDefinedLanguage(language: str) -> bool:...
    def IsValidIdentifier(self, value: str) -> bool:...
    def Parse(self, codeStream: _n_6_t_1) -> _n_1_t_0:...
    def Supports(self, generatorSupport: GeneratorSupport) -> bool:...
class CodeGenerator(ICodeGenerator):
    def GenerateCodeFromMember(self, member: _n_1_t_2, writer: _n_6_t_0, options: CodeGeneratorOptions):...
    @staticmethod
    def IsValidLanguageIndependentIdentifier(value: str) -> bool:...
    @staticmethod
    def ValidateIdentifiers(e: _n_1_t_7):...
class CodeGeneratorOptions(object):
    @property
    def BlankLinesBetweenMembers(self) -> bool:"""BlankLinesBetweenMembers { get; set; } -> bool"""
    @property
    def BracingStyle(self) -> str:"""BracingStyle { get; set; } -> str"""
    @property
    def ElseOnClosing(self) -> bool:"""ElseOnClosing { get; set; } -> bool"""
    @property
    def IndentString(self) -> str:"""IndentString { get; set; } -> str"""
    @property
    def Item(self) -> object:"""Item { get; set; } -> object"""
    @property
    def VerbatimOrder(self) -> bool:"""VerbatimOrder { get; set; } -> bool"""
    def __init__(self) -> CodeGeneratorOptions:...
class CodeParser(ICodeParser):
    pass
class CompilerError(object):
    @property
    def Column(self) -> int:"""Column { get; set; } -> int"""
    @property
    def ErrorNumber(self) -> str:"""ErrorNumber { get; set; } -> str"""
    @property
    def ErrorText(self) -> str:"""ErrorText { get; set; } -> str"""
    @property
    def FileName(self) -> str:"""FileName { get; set; } -> str"""
    @property
    def IsWarning(self) -> bool:"""IsWarning { get; set; } -> bool"""
    @property
    def Line(self) -> int:"""Line { get; set; } -> int"""
    def __init__(self, fileName: str, line: int, column: int, errorNumber: str, errorText: str) -> CompilerError:...
    def __init__(self) -> CompilerError:...
class CompilerErrorCollection(_n_2_t_0, _n_2_t_1, typing.Iterable[CompilerError]):
    @property
    def HasErrors(self) -> bool:"""HasErrors { get; } -> bool"""
    @property
    def HasWarnings(self) -> bool:"""HasWarnings { get; } -> bool"""
    def __init__(self, value: _n_0_t_0[CompilerError]) -> CompilerErrorCollection:...
    def __init__(self, value: CompilerErrorCollection) -> CompilerErrorCollection:...
    def __init__(self) -> CompilerErrorCollection:...
    def AddRange(self, value: CompilerErrorCollection):...
    def AddRange(self, value: _n_0_t_0[CompilerError]):...
class CompilerInfo(object):
    @property
    def CodeDomProviderType(self) -> _n_0_t_1:"""CodeDomProviderType { get; } -> Type"""
    @property
    def IsCodeDomProviderTypeValid(self) -> bool:"""IsCodeDomProviderTypeValid { get; } -> bool"""
    def CreateDefaultCompilerParameters(self) -> CompilerParameters:...
    def CreateProvider(self) -> CodeDomProvider:...
    def CreateProvider(self, providerOptions: _n_3_t_0[str, str]) -> CodeDomProvider:...
    def GetExtensions(self) -> _n_0_t_0[str]:...
    def GetLanguages(self) -> _n_0_t_0[str]:...
class CompilerParameters(object):
    @property
    def CompilerOptions(self) -> str:"""CompilerOptions { get; set; } -> str"""
    @property
    def CoreAssemblyFileName(self) -> str:"""CoreAssemblyFileName { get; set; } -> str"""
    @property
    def EmbeddedResources(self) -> _n_4_t_0:"""EmbeddedResources { get; } -> StringCollection"""
    @property
    def Evidence(self) -> _n_9_t_0:"""Evidence { get; set; } -> Evidence"""
    @property
    def GenerateExecutable(self) -> bool:"""GenerateExecutable { get; set; } -> bool"""
    @property
    def GenerateInMemory(self) -> bool:"""GenerateInMemory { get; set; } -> bool"""
    @property
    def IncludeDebugInformation(self) -> bool:"""IncludeDebugInformation { get; set; } -> bool"""
    @property
    def LinkedResources(self) -> _n_4_t_0:"""LinkedResources { get; } -> StringCollection"""
    @property
    def MainClass(self) -> str:"""MainClass { get; set; } -> str"""
    @property
    def OutputAssembly(self) -> str:"""OutputAssembly { get; set; } -> str"""
    @property
    def ReferencedAssemblies(self) -> _n_4_t_0:"""ReferencedAssemblies { get; } -> StringCollection"""
    @property
    def TempFiles(self) -> TempFileCollection:"""TempFiles { get; set; } -> TempFileCollection"""
    @property
    def TreatWarningsAsErrors(self) -> bool:"""TreatWarningsAsErrors { get; set; } -> bool"""
    @property
    def UserToken(self) -> _n_0_t_2:"""UserToken { get; set; } -> IntPtr"""
    @property
    def WarningLevel(self) -> int:"""WarningLevel { get; set; } -> int"""
    @property
    def Win32Resource(self) -> str:"""Win32Resource { get; set; } -> str"""
    def __init__(self, assemblyNames: _n_0_t_0[str], outputName: str) -> CompilerParameters:...
    def __init__(self, assemblyNames: _n_0_t_0[str]) -> CompilerParameters:...
    def __init__(self) -> CompilerParameters:...
    def __init__(self, assemblyNames: _n_0_t_0[str], outputName: str, includeDebugInformation: bool) -> CompilerParameters:...
class CompilerResults(object):
    @property
    def CompiledAssembly(self) -> _n_7_t_0:"""CompiledAssembly { get; set; } -> Assembly"""
    @property
    def Errors(self) -> CompilerErrorCollection:"""Errors { get; } -> CompilerErrorCollection"""
    @property
    def Evidence(self) -> _n_9_t_0:"""Evidence { get; set; } -> Evidence"""
    @property
    def NativeCompilerReturnValue(self) -> int:"""NativeCompilerReturnValue { get; set; } -> int"""
    @property
    def Output(self) -> _n_4_t_0:"""Output { get; } -> StringCollection"""
    @property
    def PathToAssembly(self) -> str:"""PathToAssembly { get; set; } -> str"""
    @property
    def TempFiles(self) -> TempFileCollection:"""TempFiles { get; set; } -> TempFileCollection"""
    def __init__(self, tempFiles: TempFileCollection) -> CompilerResults:...
class Executor(object):
    @staticmethod
    def ExecWait(cmd: str, tempFiles: TempFileCollection):...
    @staticmethod
    def ExecWaitWithCapture(userToken: _n_0_t_2, cmd: str, currentDir: str, tempFiles: TempFileCollection, outputName: str, errorName: str) -> int:...
    @staticmethod
    def ExecWaitWithCapture(userToken: _n_0_t_2, cmd: str, tempFiles: TempFileCollection, outputName: str, errorName: str) -> int:...
    @staticmethod
    def ExecWaitWithCapture(cmd: str, currentDir: str, tempFiles: TempFileCollection, outputName: str, errorName: str) -> int:...
    @staticmethod
    def ExecWaitWithCapture(cmd: str, tempFiles: TempFileCollection, outputName: str, errorName: str) -> int:...
class GeneratedCodeAttribute(_n_0_t_3, _n_8_t_0):
    @property
    def Tool(self) -> str:"""Tool { get; } -> str"""
    @property
    def Version(self) -> str:"""Version { get; } -> str"""
    def __init__(self, tool: str, version: str) -> GeneratedCodeAttribute:...
class GeneratorSupport(_n_0_t_4, _n_0_t_5, _n_0_t_6, _n_0_t_7):
    ArraysOfArrays: int
    AssemblyAttributes: int
    ChainedConstructorArguments: int
    ComplexExpressions: int
    DeclareDelegates: int
    DeclareEnums: int
    DeclareEvents: int
    DeclareIndexerProperties: int
    DeclareInterfaces: int
    DeclareValueTypes: int
    EntryPointMethod: int
    GenericTypeDeclaration: int
    GenericTypeReference: int
    GotoStatements: int
    MultidimensionalArrays: int
    MultipleInterfaceMembers: int
    NestedTypes: int
    ParameterAttributes: int
    PartialTypes: int
    PublicStaticMembers: int
    ReferenceParameters: int
    Resources: int
    ReturnTypeAttributes: int
    StaticConstructors: int
    TryCatchStatements: int
    value__: int
    Win32Resources: int
class ICodeCompiler():
    def CompileAssemblyFromDom(self, options: CompilerParameters, compilationUnit: _n_1_t_0) -> CompilerResults:...
    def CompileAssemblyFromDomBatch(self, options: CompilerParameters, compilationUnits: _n_0_t_0[_n_1_t_0]) -> CompilerResults:...
    def CompileAssemblyFromFile(self, options: CompilerParameters, fileName: str) -> CompilerResults:...
    def CompileAssemblyFromFileBatch(self, options: CompilerParameters, fileNames: _n_0_t_0[str]) -> CompilerResults:...
    def CompileAssemblyFromSource(self, options: CompilerParameters, source: str) -> CompilerResults:...
    def CompileAssemblyFromSourceBatch(self, options: CompilerParameters, sources: _n_0_t_0[str]) -> CompilerResults:...
class ICodeGenerator():
    def CreateEscapedIdentifier(self, value: str) -> str:...
    def CreateValidIdentifier(self, value: str) -> str:...
    def GenerateCodeFromCompileUnit(self, e: _n_1_t_0, w: _n_6_t_0, o: CodeGeneratorOptions):...
    def GenerateCodeFromExpression(self, e: _n_1_t_1, w: _n_6_t_0, o: CodeGeneratorOptions):...
    def GenerateCodeFromNamespace(self, e: _n_1_t_3, w: _n_6_t_0, o: CodeGeneratorOptions):...
    def GenerateCodeFromStatement(self, e: _n_1_t_4, w: _n_6_t_0, o: CodeGeneratorOptions):...
    def GenerateCodeFromType(self, e: _n_1_t_5, w: _n_6_t_0, o: CodeGeneratorOptions):...
    def GetTypeOutput(self, type: _n_1_t_6) -> str:...
    def IsValidIdentifier(self, value: str) -> bool:...
    def Supports(self, supports: GeneratorSupport) -> bool:...
    def ValidateIdentifier(self, value: str):...
class ICodeParser():
    def Parse(self, codeStream: _n_6_t_1) -> _n_1_t_0:...
class IndentedTextWriter(_n_6_t_0, _n_0_t_8):
    DefaultTabString: int
    @property
    def Indent(self) -> int:"""Indent { get; set; } -> int"""
    @property
    def InnerWriter(self) -> _n_6_t_0:"""InnerWriter { get; } -> TextWriter"""
    def __init__(self, writer: _n_6_t_0) -> IndentedTextWriter:...
    def __init__(self, writer: _n_6_t_0, tabString: str) -> IndentedTextWriter:...
    def WriteLineNoTabs(self, s: str):...
class LanguageOptions(_n_0_t_4, _n_0_t_5, _n_0_t_6, _n_0_t_7):
    CaseInsensitive: int
    _None: int
    value__: int
class TempFileCollection(_n_2_t_2, _n_0_t_8):
    @property
    def BasePath(self) -> str:"""BasePath { get; } -> str"""
    @property
    def KeepFiles(self) -> bool:"""KeepFiles { get; set; } -> bool"""
    @property
    def TempDir(self) -> str:"""TempDir { get; } -> str"""
    def __init__(self, tempDir: str) -> TempFileCollection:...
    def __init__(self) -> TempFileCollection:...
    def __init__(self, tempDir: str, keepFiles: bool) -> TempFileCollection:...
    def AddExtension(self, fileExtension: str) -> str:...
    def AddExtension(self, fileExtension: str, keepFile: bool) -> str:...
    def AddFile(self, fileName: str, keepFile: bool):...
    def Delete(self):...