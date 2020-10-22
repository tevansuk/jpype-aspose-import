# Display import problems with JPype 1+ / Aspose JAR files

This repo is just a demo for problems when importing classes from Aspose JAR files
using JPype 1+.

To run:

```
pipenv sync
pipenv run python import.py
```

or if you prefer:

```
python -m venv env
env/bin/pip install -r requirements.txt
env/bin/python import.py
```

Checkout branch use-jpype-0.7 for a working version using jpype 0.7.5


## With JPype 1.1.1

```
/home/tevans/.local/share/virtualenvs/jpype-aspose-import-2E_xYuW9/lib/python3.8/site-packages/asposecells/lib/aspose-cells-20.2.jar:/home/tevans/.local/share/virtualenvs/jpype-aspose-import-2E_xYuW9/lib/python3.8/site-packages/asposecells/lib/bcprov-jdk15on-160.jar:/home/tevans/.local/share/virtualenvs/jpype-aspose-import-2E_xYuW9/lib/python3.8/site-packages/asposecells/lib/JavaClassBridge.jar
Traceback (most recent call last):
  File "org.jpype.JPypeContext.java", line -1, in org.jpype.JPypeContext.callMethod
  File "Method.java", line 566, in java.lang.reflect.Method.invoke
  File "DelegatingMethodAccessorImpl.java", line 43, in jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke
  File "NativeMethodAccessorImpl.java", line 62, in jdk.internal.reflect.NativeMethodAccessorImpl.invoke
  File "NativeMethodAccessorImpl.java", line -2, in jdk.internal.reflect.NativeMethodAccessorImpl.invoke0
  File "Class.java", line 315, in java.lang.Class.forName
  File "Class.java", line -2, in java.lang.Class.forName0
  File "ClassLoader.java", line 522, in java.lang.ClassLoader.loadClass
  File "ClassLoader.java", line 589, in java.lang.ClassLoader.loadClass
  File "URLClassLoader.java", line 471, in java.net.URLClassLoader.findClass
Exception: Java Exception

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/tevans/.local/share/virtualenvs/jpype-aspose-import-2E_xYuW9/lib/python3.8/site-packages/jpype/imports.py", line 200, in find_spec
    cls = _jpype.JClass("java.lang.Class").forName(name)
java.lang.ClassNotFoundException: java.lang.ClassNotFoundException: com.aspose

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "import.py", line 14, in <module>
    from com.aspose.cells import Workbook
  File "/home/tevans/.local/share/virtualenvs/jpype-aspose-import-2E_xYuW9/lib/python3.8/site-packages/jpype/imports.py", line 204, in find_spec
    raise ImportError("Failed to import '%s'" % name) from ex
ImportError: Failed to import 'com.aspose'
```

## With JPype 0.7.5

```
/home/tevans/.local/share/virtualenvs/jpype-aspose-import-2E_xYuW9/lib/python3.8/site-packages/asposecells/lib/aspose-cells-20.2.jar:/home/tevans/.local/share/virtualenvs/jpype-aspose-import-2E_xYuW9/lib/python3.8/site-packages/asposecells/lib/bcprov-jdk15on-160.jar:/home/tevans/.local/share/virtualenvs/jpype-aspose-import-2E_xYuW9/lib/python3.8/site-packages/asposecells/lib/JavaClassBridge.jar
Imports worked OK
```
