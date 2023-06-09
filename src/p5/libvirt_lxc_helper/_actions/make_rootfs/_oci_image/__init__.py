#!/usr/bin/env python3
# -*- coding: utf-8 -*-

assert "__main__" != __name__


def _private():
    from .... import _common as _common_module

    _make_lazy_getter = _common_module.module_helpers.lazy_attributes.make_getter

    class _Result(object):
        lazy_getter = _make_lazy_getter(dictionary = {
            "Digest": lambda module: module.digest.Class,
            "Class": lambda module: getattr(module, "_class").Class,
            "make": lambda module: getattr(module, "_class").make
        })

    return _Result


_private = _private()

__all__ = _private.lazy_getter.keys
__date__ = None
__author__ = None
__version__ = None
__credits__ = None
_fields = tuple()
__bases__ = tuple()


def __getattr__(name: str): return _private.lazy_getter(name = name)
