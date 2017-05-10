# -*- coding: utf-8 -*-

# Modified by Antoine <antoine@van-elstraete.net> to use fancybox
# instead of lightbox.

# Copyright (c) 2016 Kura
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import unicode_literals

from docutils import nodes
from docutils.parsers.rst import directives, Directive


def align(argument):
    """Conversion function for the "align" option."""
    return directives.choice(argument, ('left', 'center', 'right'))


class Lightbox(Directive):
    """
    Create a pure CSS lightbox for images.

    Usage:

        .. lightbox::
            :img: test.png
            :alt: This is a test image
            :caption: A test caption
    """

    required_arguments = 0
    optional_arguments = 3
    option_spec = {
        'img': str,
        'alt': str,
        'caption': str,
    }

    final_argument_whitespace = False
    has_content = False

    def run(self):
        """Run the directive."""
        if 'img' not in self.options:
            raise self.error('Image argument is required.')
        img = self.options['img']
        caption = None
        alt = None

        if 'alt' in self.options:
            alt = self.options['alt']

        if 'caption' in self.options:
            caption = self.options['caption']
        else:
            caption = img.split('/')[-1]

        if alt is not None:
            alt_text = '{} (cliquer pour voir en grand)'.format(alt)
        else:
            alt_text = '(cliquer pour voir en grand)'

        img_id = img.replace('/', '-')
        block = ('''<div>'''
                 '''<a data-fancybox '''
                 '''data-caption="{3}" '''
                 '''href="/images/{0}">'''
                 '''<img src="/images_th/article/{0}" alt="{2}" '''
                 '''class="article-image" /></a>'''
                 '''</div>\n''').format(img, img_id, alt_text, caption)
        return [nodes.raw('', block, format='html'), ]


def register():
    """Register the directive."""
    directives.register_directive('lightbox', Lightbox)
