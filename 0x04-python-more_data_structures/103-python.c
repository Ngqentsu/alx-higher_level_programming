#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints bytes info
 * @p: Python Object
 */
void print_python_bytes(PyObject *p)
{
	char *bytes;
	long int i, limit;
	Py_ssize_t size = PyBytes_Size(p);

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
        bytes = ((PyBytesObject *)p)->ob_sval;

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  first %ld bytes:", limit);

	for (i = 0; i < limit; i++)
		if (bytes[i] >= 0)
			printf(" %02x", bytes[i]);
		else
			printf(" %02x", 256 + bytes[i]);

	printf("\n");
}

/**
 * print_python_list - Prints list info
 * @p: Python Object
 */
void print_python_list(PyObject *p)
{
	long int i;
	Py_ssize_t size = PyList_Size(p);
	PyObject *object;

	size = ((PyVarObject *)(p))->ob_size;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n",((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		object = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);

	}
}
