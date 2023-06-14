#include <stdio.h>
#include <Python.h>
# haru-voster
void print_python_bytes(PyObject *p)
{
	char *str;
	Py_ssize_t length, a;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
		printf("  [ERROR] Invalid Bytes Object\n");
	else
	{
		PyBytes_AsStringAndSize(p, &str, &length);
		printf("  size: %lu\n", length);
		printf("  trying string: %s\n", str);
		if (length > 10)
			length = 10;
		else
			length++;
		printf("  first %lu bytes: ", length);
		for (a = 0; a < length - 1; a++)
			printf("%02x ", str[a] & 0xff);
		printf("%02x\n", str[length - 1] & 0xff);
	}
}

void print_python_list(PyObject *p)
{
	Py_ssize_t a;
	PyObject *list;

	if (PyList_Check(p))
	{
		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %lu\n", PyList_Size(p));
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		for (a = 0; a < PyList_Size(p); a++)
		{
			list = PySequence_GetItem(p, a);
			printf("Element %lu: %s\n", a,
					list->ob_type->tp_name);
			if (strcmp(list->ob_type->tp_name, "bytes") == 0)
				print_python_bytes(list);
		}
	}
}
