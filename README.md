Django show_urls formatter
==========================

Beautify the output of `manage.py show_urls`.

The `show_urls` option is added to `manage.py` via the [django-extensions](http://django-extensions.readthedocs.org/en/latest/)
module.

The command `manage.py show_urls` displays all of the url matching routes for the project. However,
the output is not very nice since it is not formatted. This little script puts the data in columns,
thus the output is much easier to read IMO.

Before
------

Normal usage:

    $ ./manage.py show_urls

![before](https://raw.githubusercontent.com/jabbalaci/django-show_urls-formatter/master/assets/before.jpg)

After
-----

Usage of the beautifier:

    $ ./manage.py show_urls | fmt.py

![after](https://raw.githubusercontent.com/jabbalaci/django-show_urls-formatter/master/assets/after.jpg)

About
-----

* Author:  Laszlo Szathmary, 2014 (<jabba.laci@gmail.com>)
* Website: <https://pythonadventures.wordpress.com>
* GitHub:  <https://github.com/jabbalaci/django-show_urls-formatter>
