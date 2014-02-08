django-cached-functions is a library to cache results on functions in on a Django model in the django cache.

Results are cached across models (and hence across requests). Results are
cached based on the object's ``date_modified``, so when an object is saved,
it'll 'expire' the cache.

Installation / Set Up
======================

Installation
------------

    pip install django-cached-functions

Set up
------

 1. Set up the Django Cache

 2. Import the library
        
        from django_cached_functions import cached_function

Usage
-----

 1. On a function you want to cache:

        class MyModel(Model):
            
            @cached_function
            def my_function(self):
                …

Function Arguments
==================

If you give arguments (or keyword arguments) to the function, these will be
taken account of. The results of the function with different arguments will be
cached separately. 

Only other django models, or objects of type ``str``, ``unicode``, ``bool``,
``int`` can be cached.

Skipping the Cache
==================

Some times you may be doing a very important function where accuracy, not
speed, is important.

If you pass ``dont_cache=True`` as a keyword argument to the function, then the
cache will not be used (or updated). The original function will be called and
that result will be returned.

Expiring the cache
==================

The cache is based on the modeld ``date_modified`` field. When that changes,
the old cached functions are no longer used and it will regerate the functions

The ``date_modified`` is not set by this library. One suggestion for this field
is to set ``auto_now=True``.
    
    date_modified = models.DateTimeField(_(u"Date Modified"), default=datetime.utcnow, auto_now=True)

You can also update it with a ``pre_save``/``post_save`` signal.

If your cached function (on model A) depends on another model (B), then your
cache should be invalidated when B is saved. This can be done with a signal
handler on B that will update the ``date_modified`` on A when B is saved.


Licence
=======

This software is released under GNU GPL 3 (or at your option a later version).

TODO
====

*Things to work on*

 * Add a ``timeout`` option allowing one to specify how long the cache should work for.

Other software
==============

This is not an uncommon problem, there is other software out there that does
this sort of thing.

 * [django-method-cache](https://github.com/bryanhelmig/django-method-cache).

   Adds a signal handler to every method save which updates the cache. This
   might not be a good idea for some applications



[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/rory/django-cached-functions/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

