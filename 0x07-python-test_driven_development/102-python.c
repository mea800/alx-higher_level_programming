#include <stdio.h>
#include <string.h>
#include <Python.h>

/**
 * print_python_string - prints information about a Python string object
 * @p: pointer to a Python string object
 *
 * This function prints information about a Python string object, including its
 * type, length, and value. If the input object is not a string, it prints an error
 * message and returns.
 */
void print_python_string(PyObject *p)
{
	PyObject *str, *repr;

	(void)repr;
	printf("[.] string object info\n");
	// Check if the input object is a string
	if (strcmp(p->ob_type->tp_name, "str"))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	// Determine if the string is compact ascii or compact unicode
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	// Get the length and value of the string
	repr = PyObject_Repr(p);
	str = PyUnicode_AsEncodedString(p, "utf-8", "~E~");
	printf("  length: %ld\n", PyUnicode_GET_SIZE(p));
	printf("  value: %s\n", PyBytes_AsString(str));
}
