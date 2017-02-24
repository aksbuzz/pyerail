|block| PyeRail : eRail python wrapper
=============================================

.. |block| image:: http://api.erail.in/images/eRail196x196.png
  :width: 20px
  :height: 20px

|build|  |repo|  |version|  |format|  |grade|  |coverage|

.. |build| image:: https://travis-ci.org/aksbuzz/PyeRail.svg?branch=master
    :target: https://travis-ci.org/aksbuzz/PyeRail


.. |repo| image:: https://img.shields.io/badge/source-GitHub-blue.svg?maxAge=3600
   :target: https://github.com/aksbuzz/pyerail


.. |versions| image:: https://img.shields.io/pypi/v/pyerail.svg?maxAge=3600
   :target: https://pypi.python.org/pypi/pyerail

.. |format| image:: https://img.shields.io/pypi/format/pyerail.svg?maxAge=3600
   :target: https://pypi.python.org/pypi/pyerail

.. |grade| image:: https://img.shields.io/codacy/grade/9b8c7da6887c4195b9e960cb04b59a91/master.svg?maxAge=3600
   :target: https://www.codacy.com/app/aksbuzz/pyerail/dashboard

.. |coverage| image:: https://img.shields.io/codacy/coverage/9b8c7da6887c4195b9e960cb04b59a91/master.svg?maxAge=3600
   :target: https://www.codacy.com/app/aksbuzz/pyerail/files


**What is it?**
****************

PyeRail is a Python wrapper for the eRail web API.

It allows quick and easy comsumption of eRail API from your Python applicatuon.

PyeRail reqires Python 3.


**Install**
***********

You can install pyerail using:

.. code ::

	$ pip3 install pyerail

Build from source

.. code ::
	
	$ git clone https://github.com/aksbuzz/PyeRail.git

	$ cd PyeRail

	$ make


**Usage**
*********

*API Key*
^^^^^^^^^
For access to the eRail API you would need a API Key.

You can get the API Key from here http://api.erail.in/

*Using the module*
^^^^^^^^^^^^^^^^^^

Creating an instance object of class

.. code :: python
	
	>>> from pyerail import Erail
	>>> eRail = Erail(api_key)

Getting details of given PNR number

.. code :: python
	
	>>> eRail.pnr(your_pnr_number)


In any case the object returns
	
	"status" and "result"


**Examples**
************

You can find example usage in the examples folder.

**Contribution**
****************

Contributions are welcome!.

**Documentation**
*****************

Documentation at http://api.erail.in/

**Todo**
********

- Add Python 2 support
- Add detailed documentation
