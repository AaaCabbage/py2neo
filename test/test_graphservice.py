#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Copyright 2011-2017, Nigel Small
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

from __future__ import absolute_import

from py2neo.graph import GraphService

from test.util import GraphTestCase


class GraphServiceTestCase(GraphTestCase):

    def test_same_uri_gives_same_instance(self):
        uri = "bolt://localhost:7687/"
        dbms_1 = GraphService(uri)
        dbms_2 = GraphService(uri)
        assert dbms_1 is dbms_2

    def test_dbms_equality(self):
        uri = "bolt://localhost:7687/"
        dbms_1 = GraphService(uri)
        dbms_2 = GraphService(uri)
        assert dbms_1 == dbms_2
        assert hash(dbms_1) == hash(dbms_2)

    def test_dbms_is_not_equal_to_non_dbms(self):
        uri = "bolt://localhost:7687/"
        graph_service = GraphService(uri)
        assert graph_service != object()

    def test_dbms_metadata(self):
        assert self.graph_service.kernel_start_time
        assert self.graph_service.kernel_version
        assert self.graph_service.store_creation_time
        assert self.graph_service.store_id
        assert self.graph_service.primitive_counts
        assert self.graph_service.store_file_sizes
        assert self.graph_service.config

    def test_database_name(self):
        _ = self.graph_service.database_name

    def test_store_directory(self):
        _ = self.graph_service.store_directory

    def test_kernel_version(self):
        version = self.graph_service.kernel_version
        assert isinstance(version, tuple)
        assert 3 <= len(version) <= 4
        assert isinstance(version[0], int)
        assert isinstance(version[1], int)
        assert isinstance(version[2], int)

    def test_can_get_list_of_databases(self):
        databases = list(self.graph_service)
        assert databases == ["data"]

    def test_can_get_dictionary_of_databases(self):
        databases = dict(self.graph_service)
        assert len(databases) == 1
        assert databases["data"] is self.graph
