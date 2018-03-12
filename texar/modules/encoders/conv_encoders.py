#
"""
Various convolutional network encoders.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

from texar.modules.encoders.encoder_base import EncoderBase
from texar.core import layers

# pylint: disable=not-context-manager, too-many-arguments

__all__ = [
]

class ConvEncoderBase(EncoderBase):
    """Base class for all conv encoder classes."""
    raise NotImplementedError