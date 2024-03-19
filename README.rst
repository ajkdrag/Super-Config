|docs_badge| |pypi_badge|

.. |docs_badge| image:: https://img.shields.io/github/deployments/ajkdrag/ocrtoolkit/github-pages?label=docs
   :alt: GitHub-Pages deployment status
   :target: https://ajkdrag.github.io/Super-Config

.. |pypi_badge| image:: https://img.shields.io/pypi/v/Super-Config?color=green
   :alt: PyPI - Version
   :target: https://pypi.org/project/Super-Config/


Super-Config
###################################

Config parsing on steroids.


.. contents::
   :local:

Quickstart
==========

Super-Config is available on PyPI and can be installed with `pip <https://pypi.org/project/Super-Config/>`_.

.. code-block:: console

    $ pip install Super-Config

After installing Super-Config you can use it like any other Python module.

Here is a simple example:

.. code-block:: python

    import superconfig as sc
    from superconfig.superconf import SuperConfig


    def main():
        SuperConfig.setup(
            path_default="configs/default.ini", path_custom="configs/dev.yaml"
        )
    
        print(SuperConfig.get("LOCAL_PATHS.path"))
        print(SuperConfig.get("CLOUD_PATHS.path"))
        print(SuperConfig.get("ENVIRONMENT_NAME"))
        val = SuperConfig.get("ENVIRONMENT_ID", dtype=sc.INT)
        print(val, type(val))


Documentation
==============

The `API Reference <https://ajkdrag.github.io/Super-Config/>`_ provides API-level documentation


Examples
=========

Refer the `examples <https://github.com/ajkdrag/Super-Config/tree/master/examples>`_ folder in this repository


Credits
========

- `LayConf repo <https://github.com/davidohana/LayConf>`_
