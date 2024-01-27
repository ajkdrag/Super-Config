Super-Config
###################################

Config parsing on steroids.


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

Refer the example snippet: ``examples/quickstart.py``

The `API Reference <http://superconfig.readthedocs.io>`_ provides API-level documentation.
