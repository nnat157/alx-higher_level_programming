#!/usr/bin/python3
"""
Module that handles
the multiplication of
two matrices
"""


def matrix_mul(m_a, m_b):
    """
    Function that multiplies two matrices
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for element_a in m_a:
        if not isinstance(element_a, list):
            raise TypeError("m_a must be a list of lists")
    for element_b in m_b:
        if not isinstance(element_b, list):
            raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
            raise TypeError("m_a can't be empty")
    flag = 0
    for element_a in m_a:
        if element_a == []:
            flag = 1
            continue
        flag = 0
        break
    if flag == 1:
        raise TypeError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
            raise TypeError("m_b can't be empty")
    flag = 0
    for element_b in m_b:
        if element_b == []:
            flag = 1
            continue
        flag = 0
        break
    if flag == 1:
        raise TypeError("m_b can't be empty")
    for element_a in m_a:
        for num in element_a:
            if not (isinstance(num, int) or isinstance(num, float)):
                raise TypeError("m_a should contain only integers or floats")
    for element_b in m_b:
        for num in element_b:
            if not (isinstance(num, int) or isinstance(num, float)):
                raise TypeError("m_b should contain only integers or floats")
    i = 0
    for i in range(len(m_a) - 1):
        i += 1
        if len(m_a) > 1 and len(m_a[i]) != len(m_a[i - 1]):
            raise TypeError("each row of m_a must be of the same size")
    i = 0
    for i in range(len(m_b) - 1):
        i += 1
        if len(m_b) > 1 and len(m_b[i]) != len(m_b[i - 1]):
            raise TypeError("each row of m_b must be of the same size")

    m_c = [[0 for j in range(len(m_b[0]))] for i in range(len(m_a))]
    if len(m_a[0]) is not len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    # iterating by row of m_a
    for i in range(len(m_a)):
        # iterating by column of m_b
        for j in range(len(m_b[0])):
            # iterating by rows of m_b
            for k in range(len(m_b)):
                m_c[i][j] += m_a[i][k] * m_b[k][j]
    return m_c
