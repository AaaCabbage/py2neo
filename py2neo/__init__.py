#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Copyright 2011-2015, Nigel Small
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


__author__ = "Nigel Small <nigel@py2neo.org>"
__copyright__ = "2011-2015, Nigel Small"
__email__ = "nigel@py2neo.org"
__license__ = "Apache License, Version 2.0"
__package__ = "py2neo"
__version__ = "3b1"

PRODUCT = ("py2neo", __version__)


from py2neo.types import *
from py2neo.env import *
from py2neo.ext import *
from py2neo.database import *
from py2neo.http import *
from py2neo.packages.httpstream.watch import watch
from py2neo.status import Finished, GraphError
