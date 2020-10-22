import jpype
# This import adds asposecell's bundled JAR files to the classpath
import asposecells
import jpype.imports


jpype.startJVM(convertStrings=False)

import java.lang.System

print(java.lang.System.getProperty("java.class.path"))

# boom
from com.aspose.cells import Workbook

print("Imports worked OK")
