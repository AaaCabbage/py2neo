#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Copyright 2011-2014, Nigel Small
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


from py2neo import Node, Rel
from py2neo.http.batch import BatchError


def test_can_push_node(graph):
    alice = Node(name="Alice")
    graph.create(alice)
    alice.properties["age"] = 33
    graph.push(alice)
    node_id = alice._id
    Node.cache.clear()
    node = graph.node(node_id)
    assert node.properties["age"] == 33


def test_cannot_push_empty_list_property(graph):
    alice = Node(name="Alice")
    graph.create(alice)
    alice.properties["faults"] = []
    try:
        graph.push(alice)
    except BatchError:
        assert True
    else:
        assert False


def test_can_push_rel(graph):
    a, b, ab = graph.create({}, {}, (0, "KNOWS", 1))
    rel = ab.rel
    rel.properties["since"] = 1999
    graph.push(rel)
    rel_id = rel._id
    Rel.cache.clear()
    rel = graph.relationship(rel_id).rel
    assert rel.properties["since"] == 1999


def test_cannot_push_none(graph):
    try:
        graph.push(None)
    except TypeError:
        assert True
    else:
        assert False
